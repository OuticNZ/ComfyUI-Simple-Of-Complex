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