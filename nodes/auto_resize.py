import torch
from comfy.utils import lanczos

class AutoImageResize:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "desired_width": ("INT", {"default": 1024, "min": 64, "max": 8192, "step": 8}),
            }
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT")
    RETURN_NAMES = ("image", "width", "height")
    FUNCTION = "execute"
    CATEGORY = "finetuners"

    def execute(self, image, desired_width):
        # Get current dimensions
        _, current_height, current_width, _ = image.shape
        
        # Calculate target width and scale factor
        target_width = current_width
        if current_width < 1024 or current_width > 1344:
            target_width = desired_width
            scale_factor = desired_width / current_width
        else:
            # No resize needed
            return (image, current_width, current_height)
            
        # Calculate new height maintaining aspect ratio
        target_height = int(current_height * scale_factor)
        
        # Convert to NCHW for lanczos
        x = image.permute(0, 3, 1, 2)
        
        # Perform lanczos resize
        x = lanczos(x, target_width, target_height)
        
        # Convert back to NHWC
        x = x.permute(0, 2, 3, 1)
        
        return (x, target_width, target_height)
