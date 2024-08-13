class TextWithContext:

    @classmethod
    def INPUT_TYPES(cls):

        return {"required": {
            "CONTEXT": ("RGTHREE_CONTEXT"),
            "text": ("STRING", {"multiline": False, "default": ""})
        }}
    
    _all_context_input_output_data = {
        "base_ctx": ("base_ctx", "RGTHREE_CONTEXT", "CONTEXT"),
        "text": ("text", "STRING", "TEXT"),
        }

    _original_ctx_inputs_list = [
         "base_ctx", "text"
    ]

    RETURN_TYPES = ("RGTHREE_CONTEXT","STRING", )
    FUNCTION = "convert"
    CATEGORY = "SimpleOfComplex/TextContext"
    OUTPUT_NODE = True
    #RETURN_TYPES = ORIG_CTX_RETURN_TYPES
    #RETURN_NAMES = ORIG_CTX_RETURN_NAMES

    def convert(self, base_ctx=None, **kwargs):  # pylint: disable = missing-function-docstring
        ctx = self.new_context(base_ctx, **kwargs)
        return self.get_orig_context_return_tuple(ctx)

    def new_context(self, base_ctx, **kwargs):
        """Creates a new context from the provided data, with an optional base ctx to start."""
        context = base_ctx if base_ctx is not None else None
        new_ctx = {}
        for key in self._all_context_input_output_data:
            if key == "base_ctx":
                continue
            v = kwargs[key] if key in kwargs else None
            new_ctx[key] = v if v is not None else context[
            key] if context is not None and key in context else None
        return new_ctx
    
    def get_orig_context_return_tuple(self,ctx):
        """Returns a tuple for returning from a node with only the original context keys."""
        return self.get_context_return_tuple(ctx, self._original_ctx_inputs_list)
    
    def get_context_return_tuple(self,ctx, inputs_list=None):
        """Returns a tuple for returning in the order of the inputs list."""
        if inputs_list is None:
            inputs_list = self._all_context_input_output_data.keys()
        tup_list = [
            ctx,
        ]
        for key in inputs_list:
            if key == "base_ctx":
                continue
            tup_list.append(ctx[key] if ctx is not None and key in ctx else None)
        return tuple(tup_list)


