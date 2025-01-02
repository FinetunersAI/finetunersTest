class GroupLink:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {}}
    
    RETURN_TYPES = ()
    FUNCTION = "noop"
    CATEGORY = "finetuners"

    def noop(self):
        return {}
