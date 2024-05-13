import assets.pack.current.pack_resources as pack

class Block:
    mod_blocks = {}
    def create(self, name: str, color: tuple):
        pack.BLOCKS.update({name: color})
        self.mod_blocks.update({name: color})

class Color:
    mod_colors = {}
    def create(self, name: str, color: tuple):
        pack.COLORS.update({name: color})
        self.mod_colors.update({name: color})