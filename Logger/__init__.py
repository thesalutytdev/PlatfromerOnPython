import datetime

global log_file
log_file = ""
def log(message: str):
    final_message = f"[{datetime.UTC}] {message}"
    with open(log_file, "a") as f:
        f.write(final_message)
    print(final_message)
def set_log_file(path: str):
    global log_file
    log_file = path