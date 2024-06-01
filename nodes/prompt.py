#class PromptModify:     

    #
    #  <<QUALITY>><<QUALITY>
    #  <PROMPT>
    #     <POSITIVE>
    #          <QUALITY add="source_9,source_8_up" remove=""/>
    #     </POSITIVE>
    #     <NEGATIVE>
    #          <QUALITY> add="" remove=""/>
    #     </NEGATIVE>
    #  </PROMPT>
    #
    #
    #
    #

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "postive": ("STRING", {"multiline": False, "default": ""}),
                    "negative": ("STRING", {"multiline": False, "default": ""}),
                    "element": ("STRING", {"multiline": False, "default": ""}),
                    "modifers": ("STRING", {"multiline": False, "default": ""}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    OUTPUT_NODE = True
    CATEGORY = "SimpleOfComplex/Prompt"

    def execute(self, positive,negative,element,modifers):
        
        modifier_array = modifers.split("|")
        postive_seg_array = positive.split("<<{element}>>")   #  part1,quality_part,part2
        negative_seg_array = negative.split("<<{element}>>")   #  part1,quality_part,part2
        for modifier_item in modifier_array:
            if modifier_item.startswith("<<POSITIVE:"):
                a_item = modifier_item.replace("<<POSITIVE:","").replace(">>","")
                #source_9,source_8_up
                b_items = a_item.split(",")
                for c_item in b_items:


            if modifier_item.startswith("<<NEGATIVE:"):
                a_item = modifier_item.replace("<<NEGATIVE:","").replace(">>","")
                #-source_cartoon,source_furry
                 
        # <<POSTIVE:source_9,source_8_up>>|<<NEGATIVE:-source_cartoon,source_furry>>
        return("",)