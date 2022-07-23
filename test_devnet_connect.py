import datetime
from pysui.methods import rpc_methods
from pysui.includes.config import *
from pysui import rpc
from pysui.rpc.exceptions import RPCError
import json
from time import sleep

# server wallet
wallet = "0x23beb41b7c55e126750f2077c02b32cdfa62631d"

# novel rebel drift castle brain visual moon among tonight matrix fade pact
wallet1 = "0x2c53ba8163f740bb278194ac799f79275fe8dc6a"
# theme pelican doll deal olympic popular labor miracle device normal other beef
wallet2 = "0x0e430e75317ac6dafe691495ede6283d7da0cb8d"

token = envs.token
_default_timeout = envs._default_timeout
_default_endpoint = envs._default_endpoint
sui_devnet = "https://gateway.devnet.sui.io:443"
ext_sign_url = envs.ext_sign_url


def sync(wallet):
    # # Will only work with sui_devnet atm
    rpc_methods.sync_account_state(
        wallet, endpoint=sui_devnet, timeout=_default_timeout
    )


def do_count(num=10):
    count = rpc_methods.get_recent_transactions(
        num, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"Count  ::  {count}\n")
    return count


def do_get_tx(tx):
    get_tx = rpc_methods.get_transaction(
        tx,
        endpoint=_default_endpoint,
        timeout=_default_timeout,
    )
    log.info(f"GET TX  ::  {get_tx}\n")
    return tx


def get_owned(wallet, _default_endpoint=_default_endpoint):
    owned = rpc_methods.get_objects_owned_by_address(
        wallet, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"Owned  ::  {owned}\n")
    return owned


def get_signed(address: str, tx: str):
    import requests

    # # test request
    headers = {"token": token}
    params = {"signed_txns": [{"owner_address": address, "tx_bytes": tx}]}

    log.info(
        f"Sending to build command\n\tsui keytool sign --address {address}  --data {tx}\n"
    )
    # send request
    response = requests.post(ext_sign_url, params=json.dumps(params), headers=headers)
    log.info(f"Signed Response  ::  {response.json()}\n")

    return response.json()


def send_sui_tx(
    signer: str,
    recipient: str,
    sui_object_id: str,
    gas_budget: int,
    amount: int,
    _default_endpoint=sui_devnet,
) -> bool:
    # 1, Create a transaction to transfer a Sui coin from one address to another:#

    tx = rpc_methods.transfer_sui(
        signer,
        sui_object_id,
        gas_budget,
        recipient,
        amount,
        endpoint=_default_endpoint,
        timeout=_default_timeout,
    )
    log.info(f"TX response  ::  {tx}\n")

    # # 2, Sign the transaction using the Sui signtool#
    # f"sui keytool sign --address {signer} --data {tx['txBytes']}"
    # signed_txn, pub_key = '',''
    tx_bytes = tx["txBytes"]
    signed_txns = get_signed(signer, tx_bytes)

    # # 3, Execute the transaction using the transaction data, signature and public key.#
    for x in signed_txns:
        res = rpc_methods.execute_transaction(
            tx_bytes,
            x.get("signed_txn"),
            x.get("pub_key"),
            endpoint=_default_endpoint,
            timeout=_default_timeout,
        )
        log.info(f"Sent Response  ::  {res}\n")


def send_sui(num_req, wallet, wallet1, amount, _gas_budget=100):

    st = datetime.datetime.now()

    for i, _ in enumerate(range(num_req)):
        owned = get_owned(wallet, _default_endpoint=sui_devnet)
        try:
            sui_object_id = owned[0]["objectId"]
            send_sui_tx(wallet, wallet1, sui_object_id, _gas_budget, amount)
            pass
        except RPCError as e:
            log.error(e)
        except Exception as e:
            log.error(f"FAILED on .something else.. : {e}")

    et = datetime.datetime.now()
    log.info(f"Time ::  {et-st} for {num_req} calls")


def send_obj_tx(
    _from: str,
    _to: str,
    _object_id: str,
    _gas_object_id: str,
    _gas_budget: int,
    _default_endpoint=sui_devnet,
) -> bool:
    # 1, Create a transaction to transfer a Sui coin from one address to another:#

    tx = rpc_methods.transfer_sui(
        _from,
        _object_id,
        _gas_object_id,
        _gas_budget,
        _to,
        endpoint=_default_endpoint,
        timeout=_default_timeout,
    )
    log.info(f"TX response  ::  {tx}\n")

    # # 2, Sign the transaction using the Sui signtool#
    # f"sui keytool sign --address {_from} --data {tx['txBytes']}"
    # signed_txn, pub_key = '',''
    tx_bytes = tx["txBytes"]
    signed_txns = get_signed(_from, tx_bytes)

    # # 3, Execute the transaction using the transaction data, signature and public key.#
    for x in signed_txns:
        res = rpc_methods.execute_transaction(
            tx_bytes,
            x.get("signed_txn"),
            x.get("pub_key"),
            endpoint=_default_endpoint,
            timeout=_default_timeout,
        )
        log.info(f"Sent Response  ::  {res}\n")


def send_obj(num_req, wallet, wallet1, _gas_budget=20):

    st = datetime.datetime.now()

    for i, _ in enumerate(range(num_req)):

        owned = get_owned(wallet, _default_endpoint=sui_devnet)
        try:
            _object_id = owned[0]["objectId"]
            _gas_object_id = owned[1]["objectId"]
            send_obj_tx(wallet, wallet1, _object_id, _gas_object_id, _gas_budget)
            pass
        except RPCError as e:
            log.error(e)
        except Exception as e:
            log.error(f"FAILED on .something else.. : {e}")

    et = datetime.datetime.now()
    log.info(f"Time ::  {et-st} for {num_req} calls")


def get_from_to(wallet):
    _from = rpc_methods.get_transactions_from_address(
        wallet2, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"Data FROM [{wallet}]\n{_from}\n")

    _to = rpc_methods.get_transactions_to_address(
        wallet2, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"Data TO [{wallet}]\n{_to}\n")


def do_get_object(obj):
    res = rpc_methods.get_object(
        obj, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"Data for Object  ::  {obj}\n{res}\n")


def get_total_tx():
    total = rpc_methods.get_total_transaction_number(
        endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"total tx count = {total}\n")
    return total


def get_owned_by_object(obj):
    res = rpc_methods.get_objects_owned_by_object(
        obj, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"Data owned by Object  ::  {obj}\n{res}\n")


def get_tx_in_range(
    start,
    end,
):
    res = rpc_methods.get_transactions_in_range(
        start, end, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"Range {start} - {end}\n{res}\n")


def tx_by_input(obj):
    res = rpc_methods.get_transactions_by_input_object(
        obj, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"TX by Input for Object  ::  {obj}\n{res}\n")


def tx_by_mutated(obj):
    res = rpc_methods.get_transactions_by_mutated_object(
        obj, endpoint=_default_endpoint, timeout=_default_timeout
    )
    log.info(f"TX by mutated Object  ::  {obj}\n{res}\n")


if __name__ == "__main__":
    num_req = 100
    gas = 100
    amount = 100
    SLEEP = 1
    do_send_coins = True

    RUNS = 10

    for i in range(RUNS):
        log.info(f"Run:  {i+1}\n")
        sync(wallet)
        count = do_count()
        tx = count[0][1]
        do_get_tx(tx)
        owned = get_owned(wallet)
        obj = owned[0]["objectId"]
        get_from_to(wallet)
        do_get_object(obj)
        t = get_total_tx()
        get_owned_by_object(obj)
        get_tx_in_range(t - 10, t)
        tx_by_input(obj)
        tx_by_mutated(obj)

        # Only if signing is setup.
        if do_send_coins:
            # send_obj(num_req, wallet, wallet2, _gas_budget=gas)
            send_sui(num_req, wallet, wallet1, amount, _gas_budget=gas)
        sleep(SLEEP)
    log.info(f"Completed {RUNS}..\n")
