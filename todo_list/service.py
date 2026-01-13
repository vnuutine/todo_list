from todo_list import storage
from todo_list.models import Task
from dataclasses import asdict

def get_all_tasks():
    task_list = []
    task_dicts = storage.load_all_tasks()  
    for task_dict in task_dicts:
        task = Task(**task_dict)
        task_list.append(task)
    return task_list
    
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
    task_list = []
    for task in tasks:
        task_dicts = asdict(task)
        task_list.append(task_dicts)
    
    storage.save_all_tasks(task_list)
    

def get_exact_task(taskid):
    task_list = get_all_tasks()
    for task in task_list:
        if task.id == taskid:
            return task
    raise ValueError("ValueError: id inputted is not found!")

def mark_task_done(taskid):
    task_list = get_all_tasks()
    task_found = False
    for task in task_list:
        if task.id == taskid:
            task.status = "done"
            task_found = True
            break
    if not task_found:
        raise ValueError("ValueError: id inputted is not found!")
    
    list_of_dicts = []
    for task in task_list:
        task_dicts = asdict(task)
        list_of_dicts.append(task_dicts)

    storage.save_all_tasks(list_of_dicts)


def edit_task(taskid, title=None, notes=None, priority=None):
    task_list = get_all_tasks()
    task_found = False
    for task in task_list: 
        if task.id == taskid:
            task_found = True
            break
    if not task_found:
        raise ValueError("ValueError: id inputted is not found!")
    
    if title is not None:
        task.title = title
    if notes is not None:
        task.notes = notes
    if priority:
        if priority not in ["low", "medium", "high"]:
            raise ValueError(f"Priority must be 'low', 'medium', or 'high', got '{priority}'")
        task.priority = priority

    list_of_dicts = []
    for task in task_list:
        task_dicts = asdict(task)
        list_of_dicts.append(task_dicts)

    storage.save_all_tasks(list_of_dicts)

def delete_task(taskid):
    task_list = get_all_tasks()
    task_found = False
    for task in task_list:
        if task.id == taskid:
            task_found = True
            break
    if not task_found:
        raise ValueError("ValueError: id inputted is not found!")
    
    task_list.remove(task)

    list_of_dicts = []
    for task in task_list:
        task_dicts = asdict(task)
        list_of_dicts.append(task_dicts)

    storage.save_all_tasks(list_of_dicts)