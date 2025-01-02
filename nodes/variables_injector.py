class VariablesInjector:
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "height": 4, "default": "An album in !theme theme"}),  # Text widget for prompt with explicit height
                "var1_name": ("STRING", {"default": "theme"}),   # Text widget for name
                "Var1": ("STRING", {"forceInput": True})  # Connectable string input
            },
            "optional": {
                "var2_name": ("STRING", {"default": ""}),
                "Var2": ("STRING", {"forceInput": True}),
                "var3_name": ("STRING", {"default": ""}),
                "Var3": ("STRING", {"forceInput": True}), 
                "var4_name": ("STRING", {"default": ""}),
                "Var4": ("STRING", {"forceInput": True}),
                "var5_name": ("STRING", {"default": ""}),
                "Var5": ("STRING", {"forceInput": True}),
                "var6_name": ("STRING", {"default": ""}),
                "Var6": ("STRING", {"forceInput": True}),
                "var7_name": ("STRING", {"default": ""}),
                "Var7": ("STRING", {"forceInput": True}),
                "var8_name": ("STRING", {"default": ""}),
                "Var8": ("STRING", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("text",)
    FUNCTION = "inject"
    CATEGORY = "finetuners"
    
    def inject(self, **kwargs):
        result = kwargs['prompt']
        pairs = [
            (kwargs.get('var1_name'), kwargs.get('Var1')),
            (kwargs.get('var2_name'), kwargs.get('Var2')),
            (kwargs.get('var3_name'), kwargs.get('Var3')),
            (kwargs.get('var4_name'), kwargs.get('Var4')),
            (kwargs.get('var5_name'), kwargs.get('Var5')),
            (kwargs.get('var6_name'), kwargs.get('Var6')),
            (kwargs.get('var7_name'), kwargs.get('Var7')),
            (kwargs.get('var8_name'), kwargs.get('Var8')),
        ]
        
        for name, value in pairs:
            if name and value:  # Only process if both name and value are present
                result = result.replace(f"!{name}", value)
        
        return (result,)
