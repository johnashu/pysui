# Generate Methods from JSON Schema

from pysui.includes.config import join, json_out, api_data_fn
from pysui.generate.generate_api_methods import (
    create_api_data,
    open_api_data,
    create_file,
)
from pysui.generate.template import imports_constants, method_blank


data_fn = join(json_out, api_data_fn)
py_fn = join("pysui", "methods", "rpc_methods.py")

create_api_data(data_fn)
data = open_api_data(data_fn)["methods"]
create_file(py_fn, data, imports_constants, method_blank)
