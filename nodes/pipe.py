class SoCPipeToParamters:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"optional": {  
                    "SoCPipeParamters": ("SoCPipeParamters",),     
                    "model_name": ("STRING", {"multiline": False, "default": ""}),
                    "path_name": ("STRING", {"multiline": False, "default": ""}),
                    "sampler_name": ("STRING", {"multiline": False, "default": ""}),
                    "scheduler_name": ("STRING", {"multiline": False, "default": ""}),
                    "postive_prompt": ("STRING", {"multiline": False, "default": ""}),
                    "negative_prompt": ("STRING", {"multiline": False, "default": ""}),
                    "seed": int,
                    "batch_count": int,
                    "steps": int,
                    "CFG": float,
                    "image_width": int,
                    "image_height": int,
                    }
                }

    CATEGORY = "SimpleOfComplex/Pipe"
    RETURN_TYPES = ("SoCPipeParamters",)

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


class SoCPipeFromParamters:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "SoCPipeParamters": ("SoCPipeParamters",),
            },
            "optional": {
            }
        }

    CATEGORY = "SimpleOfComplex/Pipe"
    RETURN_TYPES = ("SoCPipeParamters", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", int, int, int, float, int, int,)
    RETURN_NAMES = ("SoCPipeParamters", "model_name", "path_name", "sampler_name", "scheduler_name", "postive_prompt", "negative_prompt", "seed", "batch_count", "steps", "CFG", "image_height", "image_width")

    FUNCTION = "execute"

    def execute(self, SoCPipeParameters=None, ):
        model_name_original, path_name_original, sampler_name_original, scheduler_name_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original = SoCPipeParameters
        return SoCPipeParameters, model_name_original, path_name_original, sampler_name_original, scheduler_name_original, postive_prompt_original, negative_prompt_original,seed_original,batch_count_original,steps_original,CFG_original,image_width_original, image_height_original