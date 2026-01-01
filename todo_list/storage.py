from pathlib import Path
import json

root_dir = Path(__file__).resolve().parent.parent
path_location = root_dir / "data" / "storage.json"

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
        json.dump(tasks, f, indent=4)