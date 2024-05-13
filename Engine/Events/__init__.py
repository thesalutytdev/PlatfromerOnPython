import Mods

class Events:
    def on_load(self):
        Mods.on_load()
        print("[Events] On load event worked")
    def on_world_gen(self):
        Mods.on_world_gen()
        print("[Events] On world generation event worked")
    def on_world_regen(self):
        Mods.on_world_regen()
        print("[Events] On world regeneration event worked")