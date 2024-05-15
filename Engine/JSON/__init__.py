import json
import datetime

today = datetime.date.today()
date_format = today.strftime("%d/%m/%Y")

class JSON:
    class_prefix = "JSON::"
    out_directory_path = ".../JSON_Data/"
    def to_json(self, data):
        func_prefix = "ToJSON"
        try:
            # f"{self.out_directory_path}/{datetime.datetime.now()}"
            with open(f"log.json", "a") as f:
                json.dump(data, f)
        except:
            with open(f"log.json", "w") as f:
                json.dump(data, f)
        return f"[{self.class_prefix}{func_prefix}] Successfully created JSON file."
    def from_json(self, file_path: str):
        func_prefix = "FromJSON"
        received_data = []
        try:
            with open(file_path, "r") as f:
                received_data = json.loads(f)
        except:
            return f"[{self.class_prefix}{func_prefix}] Invalid file path!"
        return received_data
    def new_json_file(self, file_name: str, data: dict, path):
        if (path):
            with open(f"{path}/{file_name}.json", "w") as f:
                json.dump(data, f)
        else:
            with open(f"{self.out_directory_path}/{file_name}", "w") as f:
                json.dump(data, f)
        return