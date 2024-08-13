class TextWithContext:

    @classmethod
    def INPUT_TYPES(cls):

        return {"required": {
            "CONTEXT": ("RGTHREE_CONTEXT"),
            "text": ("STRING", {"multiline": False, "default": ""})
        }}
    
    RETURN_TYPES = ("RGTHREE_CONTEXT","STRING", )
    #RETURN_TYPES = ORIG_CTX_RETURN_TYPES
    #RETURN_NAMES = ORIG_CTX_RETURN_NAMES

class TextSwitch2Way:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "text1": ("STRING", {"multiline": False, "default": ""}),
                    "text2": ("STRING", {"multiline": False, "default": ""}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    OUTPUT_NODE = True
    CATEGORY = "SimpleOfComplex/Switch"

    def execute(self, text1,text2):

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
    FUNCTION = "execute"
    OUTPUT_NODE = True
    CATEGORY = "SimpleOfComplex/Prompt"

    def execute(self, prompt):

        prompt1=""
        while not (prompt1 == prompt):
            prompt1=prompt
            prompt=prompt.replace(" ,",",")
            prompt=prompt.replace(", ",",")
            prompt=prompt.replace(",,",",")

        if prompt.startswith(","):
            prompt=prompt[1:]
        
        return (prompt,)