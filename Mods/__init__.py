import Engine.JSON
import Mods.examplemod

Json = Engine.JSON.JSON
Game = Engine.Game
Screen = Engine.Screen
mods = [examplemod]
def init_mods():
    examplemod.main()
def on_load():
    init_mods()
    print("Mods initialized")
    print("Mods: ")
    for i in mods:
        print(f""" {i.modName} v.{i.modVersion} ({i.modId})
 | Description: {i.modDesc}
 | Authors: {i.modAuthors}
 | Credits: {i.modCredits}
 | Website: {i.modWebsite}
 | Mod Resources: {i.modResources}
 | Update tracker: {i.modUpdateTracker}\n""")
    Json.new_json_file(Json, "blocks", Game.blocks, "game_cash/")
    Json.new_json_file(Json, "colors", Screen.colors, "game_cash/")
def on_world_gen():
    examplemod.on_world_gen()
def on_world_regen():
    examplemod.on_world_regen()
def on_world_generated():
    examplemod.on_world_generated()
def mod_page_printer(modId: str):
    for i in mods:
        if i.modId == modId:
            print(f"""{i.modName} v.{i.modVersion} ({i.modId})
 | Description: {i.modDesc}
 | Authors: {i.modAuthors}
 | Credits: {i.modCredits}
 | Website: {i.modWebsite}
 | Mod Resources: {i.modResources}
 | Update tracker: {i.modUpdateTracker}\n""")