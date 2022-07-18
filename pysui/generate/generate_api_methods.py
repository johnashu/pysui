import requests, re
from pysui.includes.config import *
from pysui.tools import file_op


def camel_to_snake(string):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()


def create_api_data(fn: str) -> None:
    api_data = requests.get(api_url).json()
    file_op.save_json(fn, api_data)


def open_api_data(fn: str, show: bool = False) -> dict:
    api_data = file_op.open_json(fn)
    if show:
        for x in api_data["methods"]:
            log.info(x["name"])
    return api_data


def build_method(
    method: dict,
    template: str,
    snake_case: bool = True,
    api_doc_link: str = "https://docs.sui.io/build/json-rpc",
) -> str:
    method_name = method.get("name")
    func = (
        camel_to_snake(method_name.split("_")[-1])
        if snake_case
        else method_name.split("_")[-1]
    )
    desc = (
        " ".join(func.title().split("_"))
        if not method.get("description")
        else method.get("description")
    )
    params = method.get("params")
    args_desc = ""
    for a in params:
        t = a.get("schema").get("type")
        args_desc += f"{a['name']}: :obj: {'' if not t else f'`{t}`'}\n\t"
    params = [x["name"] for x in params]
    args = params = ", ".join(params)
    if args:
        args += ", "

    returns = method.get("result").get("name")
    completed = template.format(
        func, args, desc, args_desc, returns, api_doc_link, method_name, params
    )
    return completed


def create_file(
    fn: str, methods: list, imports_constants: str, method_blank: str
) -> None:
    _file_str = ""
    _file_str += imports_constants

    for x in methods:
        _file_str += build_method(x, method_blank)
    file_op.save_file(fn, _file_str)
