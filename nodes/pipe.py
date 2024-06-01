import sys
import comfy.sd

FLOAT = ("FLOAT", {"default": 1,
                   "min": -sys.float_info.max,
                   "max": sys.float_info.max,
                   "step": 0.01})

BOOLEAN = ("BOOLEAN", {"default": True})
BOOLEAN_FALSE = ("BOOLEAN", {"default": False})

INT = ("INT", {"default": 1,
               "min": -sys.maxsize,
               "max": sys.maxsize,
               "step": 1})

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
                    "SoCPipeParameters": ("SoCPipeParameters",),     
                    "model_name": STRING,
                    "path_name": STRING,
                    "sampler_name": comfy.samplers.KSampler.SAMPLERS,
                    "scheduler": comfy.samplers.KSampler.SCHEDULERS,
                    "postive_prompt": STRING,
                    "negative_prompt": STRING,
                    "seed": INT,
                    "batch_count": INT,
                    "steps": INT,
                    "CFG": FLOAT,
                    "image_width": INT,
                    "image_height": INT,
                    }
                }

    CATEGORY = "SimpleOfComplex/Pipe"
    RETURN_TYPES = ("SoCPipeParameters",)

    FUNCTION = "execute"

    def execute(self, SoCPipeParameters=None, model_name=None, path_name=None, sampler=None, scheduler=None, postive_prompt=None, negative_prompt=None, seed=None, batch_count=None, steps=None, CFG=None, image_width=None, image_height=None):
        model_name_original = None
        path_name_original = None
        sampler_original = None
        scheduler_original = None
        postive_prompt_original = None
        negative_prompt_original = None
        seed_original = None 
        batch_count_original = None
        steps_original = None
        CFG_original = None
        image_width_original = None
        image_height_original = None

        if SoCPipeParameters != None:
            model_name_original, path_name_original, sampler_original, scheduler_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original = SoCPipeParameters

        SoCPipeParametersMod = []

        SoCPipeParametersMod.append(model_name if model_name is not None else model_name_original)
        SoCPipeParametersMod.append(path_name if path_name is not None else path_name_original)
        SoCPipeParametersMod.append(sampler if sampler is not None else sampler_original)
        SoCPipeParametersMod.append(scheduler if scheduler is not None else scheduler_original)
        SoCPipeParametersMod.append(postive_prompt if postive_prompt is not None else postive_prompt_original)
        SoCPipeParametersMod.append(negative_prompt if negative_prompt is not None else negative_prompt_original)
        SoCPipeParametersMod.append(seed if seed is not None else seed_original)
        SoCPipeParametersMod.append(batch_count if batch_count is not None else batch_count_original)
        SoCPipeParametersMod.append(steps if steps is not None else steps_original)
        SoCPipeParametersMod.append(CFG if CFG is not None else CFG_original)
        SoCPipeParametersMod.append(image_width if image_width is not None else image_width_original)
        SoCPipeParametersMod.append(image_height if image_height is not None else image_height_original)

        return (SoCPipeParametersMod,)


class SoCPipe2Parameters:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "SoCPipeParameters": ("SoCPipeParameters",),
            },
            "optional": {
            }
        }

    CATEGORY = "SimpleOfComplex/Pipe"
    RETURN_TYPES = ("SoCPipeParameters", "STRING", "STRING", comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS, "STRING", "STRING", "INT", "INT", "INT", "FLOAT", "INT", "INT",)
    RETURN_NAMES = ("SoCPipeParameters", "model_name", "path_name", "sampler_name", "scheduler", "postive_prompt", "negative_prompt", "seed", "batch_count", "steps", "CFG", "image_height", "image_width")

    FUNCTION = "execute"

    def execute(self, SoCPipeParameters=None, ):
        model_name_original, path_name_original, sampler_original, scheduler_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original = SoCPipeParameters
        return SoCPipeParameters, model_name_original, path_name_original, sampler_original, scheduler_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original