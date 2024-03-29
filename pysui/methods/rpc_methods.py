from pysui.rpc.request import rpc_request
from pysui.exceptions.exceptions import (
    TxConfirmationTimedoutError,
    InvalidRPCReplyError,
)

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
    the gas budget, the transaction will fail if the gas cost exceed the budget

    Parameters
    ----------
        signer: :obj:  [ the transaction signer's Sui address ]
        single_transaction_params: :obj: `array`  [ list of transaction request parameters ]
        gas: :obj:  [ gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided ]
        gas_budget: :obj: `integer`  [ the gas budget, the transaction will fail if the gas cost exceed the budget ]
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
    tx_bytes,
    flag,
    signature,
    pub_key,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
) -> list:
    """
    signer's public key, as base-64 encoded string

    Parameters
    ----------
        tx_bytes: :obj:  [ transaction data bytes, as base-64 encoded string ]
        flag: :obj:  [ Flag of the signature scheme that is used. ]
        signature: :obj:  [ transaction signature, as base-64 encoded string ]
        pub_key: :obj:  [ signer's public key, as base-64 encoded string ]
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
    params = [tx_bytes, flag, signature, pub_key]
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
    the matching events' timestamp will be before the specified end time

    Parameters
    ----------
        event_type: :obj: `string`  [ the event type, e.g. '0x2::devnet_nft::MintNFTEvent' ]
        count: :obj: `integer`  [ maximum size of the result ]
        start_time: :obj: `integer`  [ the matching events' timestamp will be after the specified start time ]
        end_time: :obj: `integer`  [ the matching events' timestamp will be before the specified end time ]
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
    the matching events' timestamp will be before the specified end time

    Parameters
    ----------
        package: :obj:  [ the Move package ID ]
        module: :obj: `string`  [ the module name ]
        count: :obj: `integer`  [ maximum size of the result ]
        start_time: :obj: `integer`  [ the matching events' timestamp will be after the specified start time ]
        end_time: :obj: `integer`  [ the matching events' timestamp will be before the specified end time ]
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
    the matching events' timestamp will be before the specified end time

    Parameters
    ----------
        object: :obj:  [ the object ID ]
        count: :obj: `integer`  [ maximum size of the result ]
        start_time: :obj: `integer`  [ the matching events' timestamp will be after the specified start time ]
        end_time: :obj: `integer`  [ the matching events' timestamp will be before the specified end time ]
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
    the matching events' timestamp will be before the specified end time

    Parameters
    ----------
        owner: :obj:  [ the owner's Sui address ]
        count: :obj: `integer`  [ maximum size of the result ]
        start_time: :obj: `integer`  [ the matching events' timestamp will be after the specified start time ]
        end_time: :obj: `integer`  [ the matching events' timestamp will be before the specified end time ]
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
    the matching events' timestamp will be before the specified end time

    Parameters
    ----------
        sender: :obj:  [ the sender's Sui address ]
        count: :obj: `integer`  [ maximum size of the result ]
        start_time: :obj: `integer`  [ the matching events' timestamp will be after the specified start time ]
        end_time: :obj: `integer`  [ the matching events' timestamp will be before the specified end time ]
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
    digest of the transaction, as base-64 encoded string

    Parameters
    ----------
        digest: :obj:  [ digest of the transaction, as base-64 encoded string ]
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
    the ID of the queried object

    Parameters
    ----------
        object_id: :obj:  [ the ID of the queried object ]
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
    the owner's Sui address

    Parameters
    ----------
        address: :obj:  [ the owner's Sui address ]
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
    the ID of the owner object

    Parameters
    ----------
        object_id: :obj:  [ the ID of the owner object ]
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
    the id of the object

    Parameters
    ----------
        object_id: :obj:  [ the id of the object ]
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
    maximum size of the result

    Parameters
    ----------
        count: :obj: `integer`  [ maximum size of the result ]
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
    Return the total number of transactions known to the server.

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
    the digest of the queried transaction

    Parameters
    ----------
        digest: :obj:  [ the digest of the queried transaction ]
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
    the ID of the input object

    Parameters
    ----------
        object: :obj:  [ the ID of the input object ]
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
    the move function name, e.g. `mint`

    Parameters
    ----------
        package: :obj:  [ the Move package ID, e.g. `0x2` ]
        module: :obj: `string`  [ the Move module name, e.g. `devnet_nft` ]
        function: :obj: `string`  [ the move function name, e.g. `mint` ]
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
    the ID of the mutated object

    Parameters
    ----------
        object: :obj:  [ the ID of the mutated object ]
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
    the sender's Sui address

    Parameters
    ----------
        addr: :obj:  [ the sender's Sui address ]
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
    the matching transactions' sequence number will be less than the ending sequence number

    Parameters
    ----------
        start: :obj: `integer`  [ the matching transactions' sequence number will be greater than or equals to the starting sequence number ]
        end: :obj: `integer`  [ the matching transactions' sequence number will be less than the ending sequence number ]
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
    the recipient's Sui address

    Parameters
    ----------
        addr: :obj:  [ the recipient's Sui address ]
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
    the gas budget, the transaction will fail if the gas cost exceed the budget

    Parameters
    ----------
        signer: :obj:  [ the transaction signer's Sui address ]
        primary_coin: :obj:  [ the coin object to merge into, this coin will remain after the transaction ]
        coin_to_merge: :obj:  [ the coin object to be merged, this coin will be destroyed, the balance will be added to `primary_coin` ]
        gas: :obj:  [ gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided ]
        gas_budget: :obj: `integer`  [ the gas budget, the transaction will fail if the gas cost exceed the budget ]
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
    the gas budget, the transaction will fail if the gas cost exceed the budget

    Parameters
    ----------
        signer: :obj:  [ the transaction signer's Sui address ]
        package_object_id: :obj:  [ the Move package ID, e.g. `0x2` ]
        module: :obj: `string`  [ the Move module name, e.g. `devnet_nft` ]
        function: :obj: `string`  [ the move function name, e.g. `mint` ]
        type_arguments: :obj: `array`  [ the type arguments of the Move function ]
        arguments: :obj: `array`  [ the arguments to be passed into the Move function, in [SuiJson](https://docs.sui.io/build/sui-json) format ]
        gas: :obj:  [ gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided ]
        gas_budget: :obj: `integer`  [ the gas budget, the transaction will fail if the gas cost exceed the budget ]
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
    the gas budget, the transaction will fail if the gas cost exceed the budget

    Parameters
    ----------
        sender: :obj:  [ the transaction signer's Sui address ]
        compiled_modules: :obj: `array`  [ the compiled bytes of a move module, the ]
        gas: :obj:  [ gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided ]
        gas_budget: :obj: `integer`  [ the gas budget, the transaction will fail if the gas cost exceed the budget ]
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
    the gas budget, the transaction will fail if the gas cost exceed the budget

    Parameters
    ----------
        signer: :obj:  [ the transaction signer's Sui address ]
        coin_object_id: :obj:  [ the coin object to be spilt ]
        split_amounts: :obj: `array`  [ the amounts to split out from the coin ]
        gas: :obj:  [ gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided ]
        gas_budget: :obj: `integer`  [ the gas budget, the transaction will fail if the gas cost exceed the budget ]
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
    the filter criteria of the event stream, see the [Sui docs](https://docs.sui.io/build/pubsub#event-filters) for detailed examples.

    Parameters
    ----------
        filter: :obj:  [ the filter criteria of the event stream, see the [Sui docs](https://docs.sui.io/build/pubsub#event-filters) for detailed examples. ]
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
    the Sui address to be synchronized

    Parameters
    ----------
        address: :obj:  [ the Sui address to be synchronized ]
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
    the recipient's Sui address

    Parameters
    ----------
        signer: :obj:  [ the transaction signer's Sui address ]
        object_id: :obj:  [ the ID of the object to be transferred ]
        gas: :obj:  [ gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided ]
        gas_budget: :obj: `integer`  [ the gas budget, the transaction will fail if the gas cost exceed the budget ]
        recipient: :obj:  [ the recipient's Sui address ]
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
    gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided

    Parameters
    ----------
        signer: :obj:  [ the transaction signer's Sui address ]
        sui_object_id: :obj:  [  ]
        gas_budget: :obj: `integer`  [ the gas budget, the transaction will fail if the gas cost exceed the budget ]
        recipient: :obj:  [  ]
        amount: :obj: `integer`  [ gas object to be used in this transaction, the gateway will pick one from the signer's possession if not provided ]
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
