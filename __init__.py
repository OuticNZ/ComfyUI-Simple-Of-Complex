from .nodes.nodes import *
#from .nodes.pipe import *

NODE_CLASS_MAPPINGS = { 
    "Text Switch 2 Way": TextSwitch2Way,
    "Prompt Tidy": PromptTidy,
    #"Pipe To Parameters": SoCParameters2Pipe,
    #"Pipe From Parameters": SoCPipe2Parameters,
    }
    
print("\033[34mComfyUI Simple of Complex Nodes: \033[92mLoaded\033[0m")