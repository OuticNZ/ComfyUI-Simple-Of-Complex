import sys
from enum import Enum

class CLASSES(Enum):
    SOC_PIPE_PARAMETERS = 'SoCPipeParameters'

class TYPES(Enum):
    FLOAT = ("FLOAT", {"default": 1,
                   "min": -sys.float_info.max,
                   "max": sys.float_info.max,
                   "step": 0.01})

    FLOAT_INPUT = ("FLOAT", {"default": 1,
                    "min": -sys.float_info.max,
                    "max": sys.float_info.max,
                    "step": 0.01,
                    "forceInput": True})

    BOOLEAN = ("BOOLEAN", {"default": True})

    BOOLEAN_FALSE = ("BOOLEAN", {"default": False})

    INT = ("INT", {"default": 1,
               "min": -sys.maxsize,
               "max": sys.maxsize,
               "step": 1})

    INT_INPUT = ("INT", {"default": 1,
                "min": -sys.maxsize,
                "max": sys.maxsize,
                "step": 1,
                "forceInput": True})

    STRING = ("STRING", {"default": ""})

    STRING_INPUT = ("STRING", {"default": "",
                           "forceInput": True})

    STRING = ("STRING", {"default": ""})

    STRING_ML = ("STRING", {"multiline": True, "default": ""})

    STRING_WIDGET = ("STRING", {"forceInput": True})

    JSON_WIDGET = ("JSON", {"forceInput": True})

    METADATA_RAW = ("METADATA_RAW", {"forceInput": True})

class AnyType(str):
    """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

    def __eq__(self, _) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return False


any = AnyType("*")