import json


class Player:
    name = "DefaultUser"
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
        self.saves_path = user_save_file_path
        try:
            with open(user_save_file_path, "r") as f:
                self.raw_save = f.read()
            self.save_file = json.loads(self.raw_save)
            self.experience = self.save_file["experience"]
            self.current_level = self.save_file["current_level"]
        except FileNotFoundError as ex:
            return

    def game_saver(self):
        with open(self.saves_path, "w") as f:
            f.write(str(self.player))
