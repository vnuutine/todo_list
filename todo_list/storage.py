from pathlib import Path
import json

path_location = Path(r"/Users/ville/Documents/Projects/Python/todo_list/data/storage.json")

def load_all_tasks():
    if not path_location.exists():
        with open(path_location, "x") as r:
            json.dump([], r)
            return []
    else:
        with open(path_location) as f:
            return json.load(f)
        

def save_all_tasks(tasks):
    with open(path_location, "w") as f:
        json.dump(tasks, f)