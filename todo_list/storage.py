from pathlib import Path
import json

path_location = Path(r"/Users/ville/Documents/Projects/Python/todo_list/data/storage.json")

def load_all_tasks():
    path_exists = path_location.exists()
    
    if path_exists == False:
        with open(path_location, "x") as r:
            json.dump([], r)
            return []
    
    else:
        with open(path_location) as f:
            return json.load(f)