# Python Package to Interact with the SUI BlockChain

***To generate methods from API Json Data*** 

*run*
`./gen_methods.py`

This will generate a file named `./pysui/methods/rpc_methods.py`

**Create a .env file and locate in the folder**

```
_default_endpoint=http://<NODE_ADDRESS>:9000
_default_timeout=30
```

**Example Program**

```python
from pysui.methods import rpc_methods
from pysui.includes.config import *

sui_rpc ='https://gateway.devnet.sui.io:443'
_default_endpoint = sui_rpc
# _default_endpoint = envs._default_endpoint
_default_timeout = envs._default_timeout

count = rpc_methods.get_recent_transactions(
    10, endpoint=_default_endpoint, timeout=_default_timeout
)
print(count)

tx = count[0][1]
get_tx = rpc_methods.get_transaction(
    tx,
    endpoint=_default_endpoint,
    timeout=_default_timeout,
)
print(get_tx)

```
