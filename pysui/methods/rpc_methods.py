from pysui.rpc.request import rpc_request
from pysui.exceptions import TxConfirmationTimedoutError, InvalidRPCReplyError

_default_endpoint = "http://localhost:9000"
_default_timeout = 30


def batch_transaction(
    signer,
    single_transaction_params,
    gas,
    gas_budget,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Batch Transaction

    Parameters
    ----------
    signer: :obj:
        single_transaction_params: :obj: `array`
        gas: :obj:
        gas_budget: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionBytes

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_batchTransaction"
    params = [signer, single_transaction_params, gas, gas_budget]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def execute_transaction(
    tx_bytes, signature, pub_key, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Execute the transaction using the transaction data, signature and public key.

    Parameters
    ----------
    tx_bytes: :obj:
        signature: :obj:
        pub_key: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionResponse

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_executeTransaction"
    params = [tx_bytes, signature, pub_key]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_events_by_event_type(
    event_type,
    count,
    start_time,
    end_time,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Get Events By Event Type

    Parameters
    ----------
    event_type: :obj: `string`
        count: :obj: `integer`
        start_time: :obj: `integer`
        end_time: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiEventEnvelope>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getEventsByEventType"
    params = [event_type, count, start_time, end_time]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_events_by_module(
    package,
    module,
    count,
    start_time,
    end_time,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Get Events By Module

    Parameters
    ----------
    package: :obj:
        module: :obj: `string`
        count: :obj: `integer`
        start_time: :obj: `integer`
        end_time: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiEventEnvelope>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getEventsByModule"
    params = [package, module, count, start_time, end_time]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_events_by_object(
    object,
    count,
    start_time,
    end_time,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Get Events By Object

    Parameters
    ----------
    object: :obj:
        count: :obj: `integer`
        start_time: :obj: `integer`
        end_time: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiEventEnvelope>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getEventsByObject"
    params = [object, count, start_time, end_time]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_events_by_owner(
    owner,
    count,
    start_time,
    end_time,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Get Events By Owner

    Parameters
    ----------
    owner: :obj:
        count: :obj: `integer`
        start_time: :obj: `integer`
        end_time: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiEventEnvelope>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getEventsByOwner"
    params = [owner, count, start_time, end_time]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_events_by_sender(
    sender,
    count,
    start_time,
    end_time,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Get Events By Sender

    Parameters
    ----------
    sender: :obj:
        count: :obj: `integer`
        start_time: :obj: `integer`
        end_time: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiEventEnvelope>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getEventsBySender"
    params = [sender, count, start_time, end_time]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_events_by_transaction(
    digest, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Events By Transaction

    Parameters
    ----------
    digest: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiEventEnvelope>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getEventsByTransaction"
    params = [digest]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_object(object_id, endpoint=_default_endpoint, timeout=_default_timeout) -> list:
    """
    Return the object information for a specified object

    Parameters
    ----------
    object_id: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    GetObjectDataResponse

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getObject"
    params = [object_id]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_objects_owned_by_address(
    address, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Return the list of objects owned by an address.

    Parameters
    ----------
    address: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiObjectInfo>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getObjectsOwnedByAddress"
    params = [address]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_objects_owned_by_object(
    object_id, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Objects Owned By Object

    Parameters
    ----------
    object_id: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<SuiObjectInfo>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getObjectsOwnedByObject"
    params = [object_id]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_raw_object(
    object_id, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Return the raw BCS serialised move object bytes for a specified object

    Parameters
    ----------
    object_id: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    GetRawObjectDataResponse

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getRawObject"
    params = [object_id]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_recent_transactions(
    count, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Recent Transactions

    Parameters
    ----------
    count: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<(GatewayTxSeqNumber,TransactionDigest)>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getRecentTransactions"
    params = [count]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_total_transaction_number(
    endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Total Transaction Number

    Parameters
    ----------

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    u64

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTotalTransactionNumber"
    params = []
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_transaction(
    digest, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Transaction

    Parameters
    ----------
    digest: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionEffectsResponse

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTransaction"
    params = [digest]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_transactions_by_input_object(
    object, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Transactions By Input Object

    Parameters
    ----------
    object: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<(GatewayTxSeqNumber,TransactionDigest)>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTransactionsByInputObject"
    params = [object]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_transactions_by_move_function(
    package, module, function, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Transactions By Move Function

    Parameters
    ----------
    package: :obj:
        module: :obj: `string`
        function: :obj: `string`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<(GatewayTxSeqNumber,TransactionDigest)>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTransactionsByMoveFunction"
    params = [package, module, function]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_transactions_by_mutated_object(
    object, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Transactions By Mutated Object

    Parameters
    ----------
    object: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<(GatewayTxSeqNumber,TransactionDigest)>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTransactionsByMutatedObject"
    params = [object]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_transactions_from_address(
    addr, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Transactions From Address

    Parameters
    ----------
    addr: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<(GatewayTxSeqNumber,TransactionDigest)>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTransactionsFromAddress"
    params = [addr]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_transactions_in_range(
    start, end, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Transactions In Range

    Parameters
    ----------
    start: :obj: `integer`
        end: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<(GatewayTxSeqNumber,TransactionDigest)>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTransactionsInRange"
    params = [start, end]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def get_transactions_to_address(
    addr, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Get Transactions To Address

    Parameters
    ----------
    addr: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    Vec<(GatewayTxSeqNumber,TransactionDigest)>

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_getTransactionsToAddress"
    params = [addr]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def merge_coins(
    signer,
    primary_coin,
    coin_to_merge,
    gas,
    gas_budget,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Merge Coins

    Parameters
    ----------
    signer: :obj:
        primary_coin: :obj:
        coin_to_merge: :obj:
        gas: :obj:
        gas_budget: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionBytes

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_mergeCoins"
    params = [signer, primary_coin, coin_to_merge, gas, gas_budget]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def move_call(
    signer,
    package_object_id,
    module,
    function,
    type_arguments,
    arguments,
    gas,
    gas_budget,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Execute a Move call transaction by calling the specified function in the module of a given package.

    Parameters
    ----------
    signer: :obj:
        package_object_id: :obj:
        module: :obj: `string`
        function: :obj: `string`
        type_arguments: :obj: `array`
        arguments: :obj: `array`
        gas: :obj:
        gas_budget: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionBytes

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_moveCall"
    params = [
        signer,
        package_object_id,
        module,
        function,
        type_arguments,
        arguments,
        gas,
        gas_budget,
    ]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def publish(
    sender,
    compiled_modules,
    gas,
    gas_budget,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Publish Move module.

    Parameters
    ----------
    sender: :obj:
        compiled_modules: :obj: `array`
        gas: :obj:
        gas_budget: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionBytes

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_publish"
    params = [sender, compiled_modules, gas, gas_budget]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def split_coin(
    signer,
    coin_object_id,
    split_amounts,
    gas,
    gas_budget,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Split Coin

    Parameters
    ----------
    signer: :obj:
        coin_object_id: :obj:
        split_amounts: :obj: `array`
        gas: :obj:
        gas_budget: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionBytes

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_splitCoin"
    params = [signer, coin_object_id, split_amounts, gas, gas_budget]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def subscribe_event(
    filter, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Subscribe Event

    Parameters
    ----------
    filter: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    SuiEventEnvelope

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_subscribeEvent"
    params = [filter]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def sync_account_state(
    address, endpoint=_default_endpoint, timeout=_default_timeout
) -> list:
    """
    Synchronize client state with validators.

    Parameters
    ----------
    address: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    ()

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_syncAccountState"
    params = [address]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def transfer_object(
    signer,
    object_id,
    gas,
    gas_budget,
    recipient,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Create a transaction to transfer an object from one address to another. The object\'s type must allow public transfers

    Parameters
    ----------
    signer: :obj:
        object_id: :obj:
        gas: :obj:
        gas_budget: :obj: `integer`
        recipient: :obj:

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionBytes

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_transferObject"
    params = [signer, object_id, gas, gas_budget, recipient]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e


def transfer_sui(
    signer,
    sui_object_id,
    gas_budget,
    recipient,
    amount,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    Send SUI coin object to a Sui address. The SUI object is also used as the gas object.

    Parameters
    ----------
    signer: :obj:
        sui_object_id: :obj:
        gas_budget: :obj: `integer`
        recipient: :obj:
        amount: :obj: `integer`

    endpoint: :obj:`str`, optional
        Endpoint to send request to
    timeout: :obj:`int`, optional
        Timeout in seconds

    Returns
    -------
    TransactionBytes

    Raises
    ------
    InvalidRPCReplyError
        If received unknown result from endpoint

    API Reference
    -------------
    https://docs.sui.io/build/json-rpc
    """
    method = "sui_transferSui"
    params = [signer, sui_object_id, gas_budget, recipient, amount]
    try:
        return rpc_request(method, params=params, endpoint=endpoint, timeout=timeout)[
            "result"
        ]
    except KeyError as e:
        raise InvalidRPCReplyError(method, endpoint) from e
