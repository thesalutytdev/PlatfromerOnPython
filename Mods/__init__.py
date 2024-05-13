import Mods.examplemod

mods = [examplemod]
def init_mods():
    examplemod.main()
def on_load():
    init_mods()
    print("Mods initialized")
    print("Mods: ")
    for i in mods:
        print(f" | {i.modName} - {i.modVersion} ({i.modId})")
def on_world_gen():
    examplemod.on_world_gen()

def on_world_regen():
    examplemod.on_world_regen()