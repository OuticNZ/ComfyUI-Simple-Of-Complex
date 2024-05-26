class TextSwitch2Way:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "text1": ("STRING", {"multiline": False, "default": ""}),
                    "text2": ("STRING", {"multiline": False, "default": ""}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "text_switch2way"
    OUTPUT_NODE = True
    CATEGORY = "SimpleOfComplex"

    def text_switch2way(self, text1,text2):

        if text1 is None or text1 == "":
            if text2 is None or text2 == "":
                return ("",)
            else:
                return (text2,)
        else:
            return (text1,)
        
class PromptTidy:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "prompt": ("STRING", {"multiline": False, "default": ""}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "prompt_tidy"
    OUTPUT_NODE = True
    CATEGORY = "SimpleOfComplex"

    def prompt_tidy(self, prompt):

        prompt1=""
        while not (prompt1 == prompt):
            prompt1=prompt
            prompt=prompt.replace(" ,",",")
            prompt=prompt.replace(", ",",")
            prompt=prompt.replace(",,",",")

        if prompt.startswith(","):
            prompt=prompt[1:]
        
        return (prompt,)