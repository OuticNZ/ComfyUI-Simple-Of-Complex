import sys

class SoCParameters2Pipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
               
        return {
            "required": {},
            "optional": {  
                    "SoCPipeParameters": ("SoCPipeParameters",),     
                    "model_name": ("STRING", {"default": ""}),
                    "path_name": ("STRING", {"default": ""}),
                    "sampler_name": ("STRING", {"default": ""}),
                    "scheduler_name": ("STRING", {"default": ""}),
                    "postive_prompt": ("STRING", {"default": ""}),
                    "negative_prompt": ("STRING", {"default": ""}),
                    "seed": ("INT", {"default": 1,"min": -sys.maxsize,"max": sys.maxsize,"step": 1}),
                    "batch_count": ("INT", {"default": 1,"min": -sys.maxsize,"max": sys.maxsize,"step": 1}),
                    "steps": ("INT", {"default": 1,"min": -sys.maxsize,"max": sys.maxsize,"step": 1}),
                    "CFG": ("FLOAT", {"default": 1,"min": -sys.float_info.max,"max": sys.float_info.max,"step": 0.01}),
                    "image_width": ("INT", {"default": 1,"min": -sys.maxsize,"max": sys.maxsize,"step": 1}),
                    "image_height": ("INT", {"default": 1,"min": -sys.maxsize,"max": sys.maxsize,"step": 1}),
                    }
                }

    CATEGORY = "SimpleOfComplex/Pipe"
    RETURN_TYPES = ("SoCPipeParameters",)

    FUNCTION = "execute"

    def execute(self, SoCPipeParameters=None, model_name=None, path_name=None, sampler_name=None, scheduler_name=None, postive_prompt=None, negative_prompt=None, seed=None, batch_count=None, steps=None, CFG=None, image_width=None, image_height=None):
        model_name_original = None
        path_name_original = None
        sampler_name_original = None
        scheduler_name_original = None
        postive_prompt_original = None
        negative_prompt_original = None
        seed_original = None 
        batch_count_original = None
        steps_original = None
        CFG_original = None
        image_width_original = None
        image_height_original = None

        if SoCPipeParameters != None:
            model_name_original, path_name_original, sampler_name_original, scheduler_name_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original = SoCPipeParameters

        SoCPipeParametersMod = []

        SoCPipeParametersMod.append(model_name if model_name is not None else model_name_original)
        SoCPipeParametersMod.append(path_name if path_name is not None else path_name_original)
        SoCPipeParametersMod.append(sampler_name if sampler_name is not None else sampler_name_original)
        SoCPipeParametersMod.append(scheduler_name if scheduler_name is not None else scheduler_name_original)
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
    RETURN_TYPES = ("SoCPipeParameters", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "INT", "INT", "INT", "FLOAT", "INT", "INT",)
    RETURN_NAMES = ("SoCPipeParameters", "model_name", "path_name", "sampler_name", "scheduler_name", "postive_prompt", "negative_prompt", "seed", "batch_count", "steps", "CFG", "image_height", "image_width")

    FUNCTION = "execute"

    def execute(self, SoCPipeParameters=None, ):
        model_name_original, path_name_original, sampler_name_original, scheduler_name_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original = SoCPipeParameters
        return SoCPipeParameters, model_name_original, path_name_original, sampler_name_original, scheduler_name_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original