import Mods
import Player


class Events:
    key: str = ""
    def on_load(self):
        Mods.on_load()
        print("[Events] On load event worked")
    def on_world_gen(self):
        Mods.on_world_gen()
        print("[Events] On world generation event worked")
    def on_world_regen(self):
        Mods.on_world_regen()
        print("[Events] On world regeneration event worked")
    def on_world_generated(self):
        Mods.on_world_generated()
        print("[Events] On world generated event worked")
        Player.Player.create_sprite(Player.Player)
    def key_event(self, key: str):
        self.key = key