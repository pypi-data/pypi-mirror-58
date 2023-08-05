import json
from typing import List

import jsonpickle
from multipledispatch import dispatch


class FJson:

    @dispatch(list)
    def to_json(self, lst: list) -> List[dict]:
        return [self.to_json(i) for i in lst]

    @dispatch(object)
    def to_json(self, obj) -> dict:
        return json.loads(jsonpickle.encode(obj, unpicklable=False))
