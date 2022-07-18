from pysui.includes.setup._envs import Envs
from pysui.includes.setup._logging import start_logger
from pysui.includes.setup._paths import *
import sys

sys.dont_write_bytecode = True

verbose = False

envs = Envs()
log = start_logger(verbose=verbose)

version = "1.0.0"

api_url = "https://raw.githubusercontent.com/MystenLabs/sui/main/crates/sui-open-rpc/spec/openrpc.json"
api_data_fn = "api_data"
