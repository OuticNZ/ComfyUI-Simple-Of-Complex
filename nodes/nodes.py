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

    def textswitch2way(self, text1,text2):

        if text1 is None or text1 == "":
            if text2 is None or text2 == "":
                return ("",)
            else:
                return (text2,)
        else:
            return (text1,)