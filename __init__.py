from .nodes.variables_injector import VariablesInjector
from .nodes.auto_resize import AutoImageResize
from .nodes.fast_group_link import GroupLink

NODE_CLASS_MAPPINGS = {
    "VariablesInjector": VariablesInjector,
    "AutoImageResize": AutoImageResize,
    "GroupLink": GroupLink
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VariablesInjector": "🔄 Variables Injector",
    "AutoImageResize": "📐 Auto Image Resize",
    "GroupLink": "🔗 Group Link"
}

WEB_DIRECTORY = "./web/js"

print("\033[34mComfyUI Finetuners: \033[92mLoaded\033[0m")
