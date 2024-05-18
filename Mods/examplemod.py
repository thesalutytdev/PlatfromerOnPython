import json

import Engine.config
import Engine.modhelper as modhelp

modId = "example"
modName = "Example Mod"
modVersion = "1.0"
modAuthors = "TheSALUTYT"
modDesc = "Just example mod"
modCredits = ":heart:"
modWebsite = "https://www.no.site.com"
modUpdateTracker = "https://i.dont.have.it.com"
modResources = "ExampleModPack"
modInfo = {
    "modId": modId,
    "name": modName,
    "version": modVersion,
    "authors": modAuthors,
    "optional": {
        "description": modDesc,
        "credits": modCredits,
        "modResources": modResources,
        "website": modWebsite,
        "updateTracker": modUpdateTracker
    }
}
blocks = modhelp.Block
colors = modhelp.Color
layers = modhelp.Layer
def main():
    blocks.create(blocks, "example_mod_block", (100, 100, 100))
    colors.create(colors, "example_mod_color", (100, 100, 100))
    layers.create(self=layers,
                  name="example_mod_layer",
                  layer_level=10,
                  width=Engine.config.WIDTH / 2,
                  height=Engine.config.HEIGHT / 2,
                  blocks=["example_mod_block", "water"],
                  save_to=Engine.WORLD_SAVES)
def on_world_gen():
    print("[ExampleMod] Enjoy your world ^-^")
def on_world_regen():
    print("[ExampleMod] Enjoy your new world ^-^")
def on_world_generated():
    generated_level = layers.generate(layers)
    layers.draw(self=layers, layer=generated_level)
    print("[ExampleMod] Generated custom layer")
def only_block_generation(layer_info: dict):
    global tile_type
    tile_type = layer_info.get('block')
    WIDTH = layer_info.get('width')
    HEIGHT = layer_info.get('height')
    TILE_SIZE = Engine.config.TILE_SIZE
    TILES_WIDE = WIDTH // TILE_SIZE
    TILES_HIGH = HEIGHT // TILE_SIZE
    layer_data = []
    for y in range(int(TILES_WIDE)):
        row = []
        for x in range(int(TILES_HIGH)):
            row.append(tile_type)
        layer_data.append(row)
    with open(f"{Engine.WORLD_SAVES}{layer_info.get('name')}", "w") as f:
        json.dump(layer_data, f)
    return layer_data