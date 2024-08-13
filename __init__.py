from nodes.context import TextWithContext 
from nodes.prompttidy import PromptTidy
from nodes.textswitch2way import TextSwitch2Way

NODE_CLASS_MAPPINGS = { 
    "Text Switch 2 Way": TextSwitch2Way,
    "Prompt Tidy": PromptTidy,
    "Text With Context": TextWithContext
    #"Pipe To Parameters": SoCParameters2Pipe,
    #"Pipe From Parameters": SoCPipe2Parameters,
    }
    
print("\033[34mComfyUI Simple of Complex Nodes: \033[92mLoaded\033[0m")