from .rpc.exceptions import RPCError, RequestsError, RequestsTimeoutError


class InvalidRPCReplyError(RuntimeError):
    """
    Exception raised when RPC call returns unexpected result
    Generally indicates SUI API has been updated & suihmy library needs to be updated as well
    """

    def __init__(self, method, endpoint):
        super().__init__(f"Unexpected reply for {method} from {endpoint}")


class TxConfirmationTimedoutError(AssertionError):
    """
    Exception raised when a transaction is sent to the chain
    But not confirmed during the timeout period specified
    """

    def __init__(self, msg):
        super().__init__(f"{msg}")
