import Engine.modhelper as modhelp

modId = "example"
modName = "Example Mod"
modVersion = "1.0"
authors = "TheSALUTYT"
modDesc = "Just example mod"
modCredits = "I love players of my game"
modWebsite = "https://www.no.site.com"
modUpdateTracker = "https://i.dont.have.it.com"
modInfo = {
    "modId": modId,
    "name": modName,
    "version": modVersion,
    "authors": authors,
    "optional": {
        "description": modDesc,
        "credits": modCredits,
        "website": modWebsite,
        "updateTracker": modUpdateTracker
    }
}
def main():
    blocks = modhelp.Block
    color = modhelp.Color

    blocks.create(blocks, "example_mod_block", (100, 100, 100))
    color.create(color, "example_mod_color", (100, 100, 100))
def on_world_gen():
    print("[ExampleMod] Enjoy your world ^-^")
def on_world_regen():
    print("[ExampleMod] Enjoy your new world ^-^")