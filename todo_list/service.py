import storage
from models import Task

def get_all_tasks():
    tasks_list = []
    task_dicts = storage.load_all_tasks()  
    for task_dict in task_dicts:
        task = Task(**task_dict)
        tasks_list.append(task)
    return tasks_list
    
def add_task(title, notes="", priority="normal"):
    # TODO: get_all_tasks() (Get a list of tasks)
    #       Find next available id from tasks and assign it to new task being created
    #       Create a new Task with fields user has given + id
    #       Add it to the list of tasks loaded previously
    #       Send to storage with storage.save_all_tasks(tasks)
    print("Hello, World!")
    