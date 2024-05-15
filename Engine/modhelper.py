import Engine.Video
import World
import assets.pack.current.pack_resources as pack

mod_layers = {}
mod_blocks = {}
mod_colors = {}

class Block:
    game_blocks = pack.BLOCKS
    def create(self, name: str, color: tuple):
        pack.BLOCKS.update({name: color})
        mod_blocks.update({name: color})

class Color:
    game_colors = pack.COLORS
    def create(self, name: str, color: tuple):
        pack.COLORS.update({name: color})
        mod_colors.update({name: color})
class Layer:
    custom_layer = {}
    generated: list
    def create(self, name: str, layer_level: int, height: int, width: int, blocks: list, save_to: str):
        self.custom_layer.update({
            "name": name,
            "layer_level": layer_level,
            "width": height,
            "height": width,
            "blocks": blocks,
            "save_to": save_to
        })
        mod_layers.update({
            name: {
                "width": height,
                "height": width,
                "blocks": blocks,
                "save_to": save_to
            }
        })
        World.Layer.new(World.Layer, self.custom_layer)
    def generate(self):
        self.generated = World.generate_custom_layer(custom_layer=self.custom_layer)
        return self.generated
    def draw(self):
        Engine.Video.draw_layer(layer=self.generated)
    def draw(self, layer: list):
        Engine.Video.draw_layer(layer=layer)