import json
import os
import pygame.image

import assets.pack.default.block.blocks as block
import assets.pack.default.color.color_pack as color

pack = "default"
COLORS = color.COLORS
BLOCKS = block.BLOCKS
window_settings_raw = ""
with open(f"assets/pack/{pack}/window/window_settings.json", "r") as f:
    window_settings_raw = f.read()
window_settings = json.loads(window_settings_raw)
icon = pygame.image.load(window_settings["icon"])