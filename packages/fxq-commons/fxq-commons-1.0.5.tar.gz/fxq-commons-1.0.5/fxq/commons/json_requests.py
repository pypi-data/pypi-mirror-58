from fxq.commons._reflection_utils import _is_list_with_generic, _get_generic, _deserialize_json_list_to, \
    _deserialize_json_object_to
from fxq.commons._requests_adapter import _do_get_json


def get(url, resp_type=None, params=None):
    json = _do_get_json(url, params)
    if _is_list_with_generic(resp_type):
        return _deserialize_json_list_to(json, _get_generic(resp_type))
    else:
        return _deserialize_json_object_to(json, resp_type)
