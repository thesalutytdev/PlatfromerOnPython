import json

import Engine
import Engine.Video.Sprites

Sprites = Engine.Video.Sprites.Sprites
Game = Engine.config.Game
Screen = Engine.config.Screen

class Player:
    name = ""
    global inserted_name
    inserted_name = ""
    save_file = ""
    raw_save = ""
    current_level = 0
    experience = 0
    saves_path = ""
    player = {
        "name": name,
        "current_level": current_level,
        "experience": experience
    }

    def __init__(self, user_name: str, user_save_file_path: str):
        self.name = user_name
        self.inserted_name = user_name
        if user_save_file_path.endswith(Engine.SAVES_FORMAT):
            self.saves_path = user_save_file_path
        else:
            self.saves_path = user_save_file_path + ".json"
        try:
            with open(self.saves_path, "r") as f:
                self.raw_save = f.read()
            self.save_file = json.loads(self.raw_save)
            self.experience = self.save_file["experience"]
            self.current_level = self.save_file["current_level"]
        except FileNotFoundError as ex:
            print(ex)
            return

    def game_saver(self):
        self.player = {
            "name": self.name,
            "current_level": self.current_level,
            "experience": self.experience
        }
        with open(self.saves_path, "w") as f:
            json.dump(self.player, f)
    def next_level(self):
        self.current_level += 1
    def set_level(self, level: int):
        self.current_level = level
    def get_level(self):
        return self.current_level
    def set_exp(self, exp: int):
        self.experience = exp
    def get_exp(self):
        return self.experience
    def create_sprite(self):
        Sprites.create(Sprites, Screen.colors.get('red'), 100, 100)