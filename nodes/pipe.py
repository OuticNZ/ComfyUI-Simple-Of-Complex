import sys
import comfy.sd
from enum import Enum


class CLASSES(Enum):
    SOC_PIPE_PARAMETERS = 'SoCPipeParameters'

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

class SoCParameters2Pipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {},
            "optional": {  
                    "SoCPipeParameters": (CLASSES.SOC_PIPE_PARAMETERS.value,),     
                    "modelname": STRING_INPUT,
                    "path_name": STRING_INPUT,
                    "sampler_name": any,
                    "scheduler": any,
                    "scheduler_name": any,
                    "postive_prompt": STRING_INPUT,
                    "negative_prompt": STRING_INPUT,
                    "seed": INT_INPUT,
                    "batch_count": INT_INPUT,
                    "steps": INT_INPUT,
                    "CFG": FLOAT_INPUT,
                    "image_width": INT_INPUT,
                    "image_height": INT_INPUT,
                    "stage1_scale_factor": FLOAT_INPUT,
                    "stage2_scale_factor": FLOAT_INPUT
                    }
                }

    CATEGORY = "SimpleOfComplex/Pipe"
    RETURN_TYPES = (CLASSES.SOC_PIPE_PARAMETERS.value,)

    FUNCTION = "execute"

    def execute(self, SoCPipeParameters=None, model_name=None, path_name=None, sampler=None, scheduler=None,scheduler_name=None, postive_prompt=None, negative_prompt=None, seed=None, batch_count=None, steps=None, CFG=None, image_width=None, image_height=None, stage1_scale_factor=None, stage2_scale_factor=None):
        model_name_original = None
        path_name_original = None
        sampler_original = None
        scheduler_original = None
        scheduler_name_original = None
        postive_prompt_original = None
        negative_prompt_original = None
        seed_original = None 
        batch_count_original = None
        steps_original = None
        CFG_original = None
        image_width_original = None
        image_height_original = None
        stage1_scale_factor_original = None
        stage2_scale_factor_original = None

        if SoCPipeParameters != None:
            model_name_original, path_name_original, sampler_original, scheduler_original, scheduler_name_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original, stage1_scale_factor_original, stage2_scale_factor_original = SoCPipeParameters

        SoCPipeParametersMod = []

        SoCPipeParametersMod.append(model_name if model_name is not None else model_name_original)
        SoCPipeParametersMod.append(path_name if path_name is not None else path_name_original)
        SoCPipeParametersMod.append(sampler if sampler is not None else sampler_original)
        SoCPipeParametersMod.append(scheduler if scheduler is not None else scheduler_original)
        SoCPipeParametersMod.append(scheduler_name if scheduler_name is not None else scheduler_name_original)
        SoCPipeParametersMod.append(postive_prompt if postive_prompt is not None else postive_prompt_original)
        SoCPipeParametersMod.append(negative_prompt if negative_prompt is not None else negative_prompt_original)
        SoCPipeParametersMod.append(seed if seed is not None else seed_original)
        SoCPipeParametersMod.append(batch_count if batch_count is not None else batch_count_original)
        SoCPipeParametersMod.append(steps if steps is not None else steps_original)
        SoCPipeParametersMod.append(CFG if CFG is not None else CFG_original)
        SoCPipeParametersMod.append(image_width if image_width is not None else image_width_original)
        SoCPipeParametersMod.append(image_height if image_height is not None else image_height_original)
        SoCPipeParametersMod.append(stage1_scale_factor if stage1_scale_factor is not None else stage1_scale_factor_original)
        SoCPipeParametersMod.append(stage2_scale_factor if stage2_scale_factor is not None else stage2_scale_factor_original)

        return (SoCPipeParametersMod,)


class SoCPipe2Parameters:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "SoCPipeParameters": (CLASSES.SOC_PIPE_PARAMETERS.value,),
            },
            "optional": {
            }
        }

    CATEGORY = "SimpleOfComplex/Pipe"
    RETURN_TYPES = (CLASSES.SOC_PIPE_PARAMETERS.value, STRING, STRING, any, any, any, STRING, STRING, INT, INT, INT, FLOAT, INT, INT,FLOAT, FLOAT)
    RETURN_NAMES = ("SoCPipeParameters", "modelname", "path_name", "sampler_name", "scheduler", "scheduler_name", "postive_prompt", "negative_prompt", "seed", "batch_count", "steps", "CFG", "image_height", "image_width", "stage1_scale_factor", "stage2_scale_factor")

    FUNCTION = "execute"

    def execute(self, SoCPipeParameters=None, ):
        model_name_original, path_name_original, sampler_original, scheduler_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original, stage1_scale_factor_original, stage2_scale_factor_original = SoCPipeParameters
        return SoCPipeParameters, model_name_original, path_name_original, sampler_original, scheduler_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original, stage1_scale_factor_original, stage2_scale_factor_original