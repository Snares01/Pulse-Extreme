import sys, os

ASSETS = {
    "style": ["style.css"],
    # fonts
    "roboto_light": ["assets", "Roboto-Light.ttf"],
    "roboto_medium": ["assets", "Roboto-Medium.ttf"],
    # toggles
    "toggle_off": ["assets", "toggle_off.png"],
    "toggle_off_disabled": ["assets", "toggle_off_disabled.png"],
    "toggle_on": ["assets", "toggle_on.png"],
    "toggle_on_disabled": ["assets", "toggle_on_disabled.png"],
    # logo / window icons
    "corner_logo": ["assets", "pulse_corner_logo.png"],
    "icon_logo": ["assets", "pulse_icon_logo.png"],
    "license_key": ["assets", "license_key.png"],
    # icons (keys correspond to titles in constants.py)
    "CPU": ["assets", "icons", "cpu.png"],
    "Memory": ["assets", "icons", "memory.png"],
    "Network": ["assets", "icons", "network.png"],
    "Services": ["assets", "icons", "services.png"],
    "GPU": ["assets", "icons", "gpu.png"],
    "General": ["assets", "icons", "general.png"],
    "Debloat": ["assets", "icons", "debloat.png"],
    "Latency": ["assets", "icons", "latency.png"],
    "Input": ["assets", "icons", "input.png"],
    "Power": ["assets", "icons", "power.png"],
}

# Gets path from asset name (key in ASSETS)
def get_path(asset_name) -> str:
    # Get base dir
    if getattr(sys, 'frozen', False):
        asset_path = sys._MEIPASS
    else:
        asset_path = os.path.dirname(os.path.abspath(__file__))
    # Make file path
    for path_segment in ASSETS[asset_name]:
        asset_path = os.path.join(asset_path, path_segment)
    
    return asset_path.replace("\\", "/") # Backslashes break f-strings

# Turns a relative path into executable path, if needed
def get_batch_path(rel_path) -> str:
    if getattr(sys, 'frozen', False):
        asset_path = sys._MEIPASS
        prev_path_segment = ""
        # Make file path
        for path_segment in rel_path.split("/"):
            # Skip subfolder of batch since pyinstaller "flattens" the folder
            if prev_path_segment != "batch":
                asset_path = os.path.join(asset_path, path_segment)
            prev_path_segment = path_segment
    else:
        asset_path = os.path.dirname(os.path.abspath(__file__))
        # Make file path
        for path_segment in rel_path.split("/"):
            asset_path = os.path.join(asset_path, path_segment)
    
    return asset_path.replace("\\", "/")