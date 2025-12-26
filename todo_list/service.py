import storage
from models import Task
from dataclasses import asdict

def get_all_tasks():
    tasks_list = []
    task_dicts = storage.load_all_tasks()  
    for task_dict in task_dicts:
        task = Task(**task_dict)
        tasks_list.append(task)
    return tasks_list
    
def add_task(title, notes="", priority="normal"):
    tasks = get_all_tasks()
    
    if tasks == []:
        next_id = 1
    else:
        max_id = 0
        for task in tasks:
            if task.id > max_id:
                max_id = task.id
        next_id = max_id + 1

    new_task = Task(next_id, title, notes, priority)
    tasks.append(new_task)
    tasks_list = []
    for task in tasks:
        task_dicts = asdict(task)
        tasks_list.append(task_dicts)
    
    storage.save_all_tasks(tasks_list)
    