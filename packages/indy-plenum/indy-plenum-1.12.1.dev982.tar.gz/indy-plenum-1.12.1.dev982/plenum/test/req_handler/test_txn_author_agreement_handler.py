import pytest as pytest

from plenum.common.util import get_utc_epoch
from storage.kv_in_memory import KeyValueStorageInMemory

from common.serializers.serialization import config_state_serializer
from plenum.common.constants import ROLE, STEWARD, NYM, TARGET_NYM, TXN_TYPE, TXN_AUTHOR_AGREEMENT, \
    TXN_AUTHOR_AGREEMENT_TEXT, TXN_AUTHOR_AGREEMENT_VERSION, TRUSTEE, DOMAIN_LEDGER_ID, TXN_AUTHOR_AGREEMENT_DIGEST, \
    TXN_AUTHOR_AGREEMENT_RETIREMENT_TS, TXN_AUTHOR_AGREEMENT_RATIFICATION_TS, TXN_METADATA, TXN_METADATA_TIME
from plenum.common.exceptions import UnauthorizedClientRequest, InvalidClientRequest
from plenum.common.request import Request
from plenum.common.txn_util import reqToTxn, get_payload_data, append_txn_metadata
from plenum.server.database_manager import DatabaseManager
from plenum.server.request_handlers.static_taa_helper import StaticTAAHelper
from plenum.server.request_handlers.txn_author_agreement_handler import TxnAuthorAgreementHandler
from plenum.server.request_handlers.utils import nym_to_state_key, encode_state_value
from plenum.test.req_handler.helper import update_nym, create_taa_txn, check_taa_in_state
from plenum.test.testing_utils import FakeSomething
from state.pruning_state import PruningState
from state.state import State


@pytest.fixture(scope="function", params=[1, None, "without"])
def retired_time(request):
    return request.param


@pytest.fixture(scope="function")
def set_aml(txn_author_agreement_handler):
    txn_author_agreement_handler.state.set(StaticTAAHelper.state_path_taa_aml_latest(),
                                           encode_state_value("value", "seqNo", "txnTime",
                                                              serializer=config_state_serializer))


def test_static_validation(txn_author_agreement_handler, taa_request):
    txn_author_agreement_handler.static_validation(taa_request)


def test_dynamic_validation(txn_author_agreement_handler, taa_request, set_aml):
    txn_author_agreement_handler.dynamic_validation(taa_request)


def test_dynamic_validation_without_aml(txn_author_agreement_handler, taa_request):
    with pytest.raises(InvalidClientRequest,
                       match="TAA txn is forbidden until TAA AML is set. Send TAA AML first."):
        txn_author_agreement_handler.dynamic_validation(taa_request)


def test_dynamic_validation_add_with_retired(txn_author_agreement_handler, domain_state,
                                         taa_request, set_aml, retired_time):

    taa_request.operation[TXN_AUTHOR_AGREEMENT_RETIREMENT_TS] = retired_time
    if retired_time == "without":
        taa_request.operation.pop(TXN_AUTHOR_AGREEMENT_RETIREMENT_TS, None)
        retired_time = None

    if retired_time:
        with pytest.raises(InvalidClientRequest,
                           match="Cannot create a transaction author agreement with a 'retirement_ts' field."):
            txn_author_agreement_handler.dynamic_validation(taa_request)
    else:
        txn_author_agreement_handler.dynamic_validation(taa_request)


def test_dynamic_validation_update_last_taa_with_retired(txn_author_agreement_handler, domain_state,
                                         taa_request, set_aml, retired_time):

    txn, digest, state_data = create_taa_txn(taa_request)
    txn_author_agreement_handler.update_state(txn, None, taa_request)
    taa_request.operation[TXN_AUTHOR_AGREEMENT_RETIREMENT_TS] = retired_time
    if retired_time == "without":
        taa_request.operation.pop(TXN_AUTHOR_AGREEMENT_RETIREMENT_TS, None)
        txn_author_agreement_handler.dynamic_validation(taa_request)
    else:
        with pytest.raises(InvalidClientRequest,
                           match="The latest transaction author agreement cannot be retired"):
            txn_author_agreement_handler.dynamic_validation(taa_request)


def test_dynamic_validation_update_with_retired_taa_off(txn_author_agreement_handler, domain_state,
                                         taa_request, set_aml, retired_time):

    txn, digest, state_data = create_taa_txn(taa_request)
    txn_author_agreement_handler.update_state(txn, None, taa_request)
    txn_author_agreement_handler.state.remove(StaticTAAHelper.state_path_taa_latest())
    taa_request.operation[TXN_AUTHOR_AGREEMENT_RETIREMENT_TS] = retired_time
    if retired_time == "without":
        taa_request.operation.pop(TXN_AUTHOR_AGREEMENT_RETIREMENT_TS, None)
        txn_author_agreement_handler.dynamic_validation(taa_request)
    else:
        with pytest.raises(InvalidClientRequest,
                           match="Retirement date cannot be changed when TAA enforcement is disabled."):
            txn_author_agreement_handler.dynamic_validation(taa_request)


def test_dynamic_validation_add_with_text(txn_author_agreement_handler, domain_state,
                                          taa_request, set_aml):
    # Validate adding TAA with text
    taa_request.operation[TXN_AUTHOR_AGREEMENT_TEXT] = "text"
    txn_author_agreement_handler.dynamic_validation(taa_request)

    # Validate adding TAA without text
    taa_request.operation.pop(TXN_AUTHOR_AGREEMENT_TEXT, None)
    with pytest.raises(InvalidClientRequest,
                       match="Cannot create a transaction author agreement without a 'text' field."):
        txn_author_agreement_handler.dynamic_validation(taa_request)


@pytest.mark.parametrize("second_text", ["text1", "text2", "without"])
def test_dynamic_validation_update_with_text(txn_author_agreement_handler, domain_state,
                                         taa_request, set_aml, second_text):

    # Add a TAA
    first_text = "text1"
    taa_request.operation[TXN_AUTHOR_AGREEMENT_TEXT] = first_text
    txn, digest, state_data = create_taa_txn(taa_request)
    txn_author_agreement_handler.update_state(txn, None, taa_request)

    # Prepare the TAA for update
    taa_request.operation[TXN_AUTHOR_AGREEMENT_TEXT] = second_text
    if first_text == "without":
        taa_request.operation.pop(TXN_AUTHOR_AGREEMENT_TEXT, None)
        second_text = None

    # Validate the second TAA
    if second_text and first_text != second_text:
        with pytest.raises(InvalidClientRequest,
                           match="Changing a text of existing transaction author agreement is forbidden"):
            txn_author_agreement_handler.dynamic_validation(taa_request)
    else:
        txn_author_agreement_handler.dynamic_validation(taa_request)


def test_dynamic_validation_from_steward(txn_author_agreement_handler, domain_state,
                                         taa_request, set_aml):
    identifier = "test_identifier"
    update_nym(domain_state, identifier, STEWARD)
    taa_request._identifier = identifier
    with pytest.raises(UnauthorizedClientRequest,
                       match="Only trustee can update transaction author agreement and AML"):
        txn_author_agreement_handler.dynamic_validation(taa_request)


def test_dynamic_validation_with_not_unique_version(txn_author_agreement_handler, taa_request, set_aml):
    txn = reqToTxn(taa_request)
    txn_author_agreement_handler.update_state(txn, None, taa_request)
    txn_author_agreement_handler.dynamic_validation(taa_request)
    taa_request.operation[TXN_AUTHOR_AGREEMENT_TEXT] = ""
    with pytest.raises(InvalidClientRequest,
                       match="Changing a text of existing transaction author agreement is forbidden"):
        txn_author_agreement_handler.dynamic_validation(taa_request)


def test_update_state(txn_author_agreement_handler, taa_request):
    txn, digest, state_data = create_taa_txn(taa_request)

    txn_author_agreement_handler.update_state(txn, None, taa_request)

    check_taa_in_state(handler=txn_author_agreement_handler,
                       digest=digest,
                       version=state_data[0][TXN_AUTHOR_AGREEMENT_VERSION],
                       state_data=state_data)
    assert txn_author_agreement_handler.state.get(
        StaticTAAHelper.state_path_taa_latest(), isCommitted=False) == digest.encode()


def test_update_state_one_by_one(txn_author_agreement_handler, taa_request, retired_time):
    txn, digest, state_data = create_taa_txn(taa_request)
    state_value, seq_no, txn_time_first = state_data
    payload = get_payload_data(txn)
    txn_time_second = get_utc_epoch()

    # update state
    txn_author_agreement_handler.update_state(txn, None, None)
    if retired_time and retired_time != "without":
        payload[TXN_AUTHOR_AGREEMENT_RETIREMENT_TS] = retired_time
        state_value[TXN_AUTHOR_AGREEMENT_RETIREMENT_TS] = retired_time
    txn[TXN_METADATA][TXN_METADATA_TIME] = txn_time_second
    txn_author_agreement_handler.update_state(txn, None, None)

    assert txn_author_agreement_handler.get_from_state(
        StaticTAAHelper.state_path_taa_digest(digest)) == (state_value, seq_no, txn_time_second)
