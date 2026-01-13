import service
from models import Task

def main_menu():
    while True:
        print("----------")
        print("Choose action")
        print("1. Add new task")
        print("2. View your tasks")
        print("3. Mark task done")
        print("4. Edit task")
        print("5. Delete task")
        print("Press 'Q' to quit")
        print("----------")
        choice = input("Input: ").strip().lower()

        if choice == "1":
            title, notes, priority = handle_add_task()
            service.add_task(title, notes, priority)
            print(f"New task: {title} added")
            print("----------")
        
        if choice == "2":
            task_list = service.get_all_tasks()
            while True:
                print("----------")
                print("Select the tasks you want to see:")
                print("1. All open tasks")
                print("2. All done tasks")
                print("3. Exact task by id")
                print("4. Filtered by priority")
                print("Press 'Q' to return to main menu")
                print("----------")
                user_choice = input("Input: ").strip().lower()
                
                if user_choice == "q":
                    break
                
                if user_choice == "1":
                    open_found = False
                    for task in task_list:
                        if task.status == "open":
                            open_found = True
                            print("TaskID", task.id, "Title:", task.title, "Notes:", task.notes, "Priority:", task.priority, "Status:", task.status, "Created at:", task.created_at)
                            print("----------")
                    if not open_found:
                        print("No tasks currently open")
                        print("----------")
                    input("Press enter to continue ")
                
                if user_choice == "2":
                    done_found = False
                    for task in task_list:
                        if task.status == "done":
                            done_found = True
                            print("TaskID", task.id, "Title:", task.title, "Notes:", task.notes, "Priority:", task.priority, "Status:", task.status, "Created at:", task.created_at, "Completed at:", task.completed_at)
                            print("----------")
                    if not done_found:
                        print("No tasks done yet")
                        print("----------")
                    input("Press enter to continue ")

                if user_choice == "3":
                    while True:
                        exact_id = input("Input the task id (Press 'Q' to exit): ").strip().lower()
                        if exact_id == "q":
                            break
                        try:
                            task = service.get_exact_task(int(exact_id))
                            print("TaskID", task.id, "Title:", task.title, "Notes:", task.notes, "Priority:", task.priority, "Status:", task.status, "Created at:", task.created_at, "Completed at:", task.completed_at)
                            print("----------")
                        except ValueError:
                            print("ValueError: id inputted is not valid, try again")

                if user_choice == "4":
                    priority_found = False
                    while True:
                        print("Choose priority to filter with ('low', 'normal' or 'high')")
                        chosen_priority = input("Input (Press 'Q' to exit): ").strip().lower()
                        if chosen_priority == "q":
                            break
                        
                        if chosen_priority in {'low' ,'normal', 'high'}:
                            for task in task_list:
                                if task.priority == chosen_priority:
                                    priority_found = True
                                    print("TaskID", task.id, "Title:", task.title, "Notes:", task.notes, "Priority:", task.priority, "Status:", task.status, "Created at:", task.created_at, "Completed at:", task.completed_at)
                                    print("----------")
                        
                        if not priority_found:
                            print("No tasks with selected priority found")
                            print("----------")
                        
                        if chosen_priority not in {'low', 'normal', 'high'}:
                            print("ValueError: Priority must be 'low', 'normal' or 'high'")
                            print("----------")
        
        if choice == "3":
            while True:
                taskid = input("Input task id-number of the task to mark done (Press 'Q' to exit): ").strip().lower()
                if taskid == "q":
                    break
                else:
                    try:
                        service.mark_task_done(int(taskid))
                        print(f"Task {taskid} marked as done")
                        break
                    except ValueError:
                        print("ValueError: id inputted is not valid, try again")
                        print("----------")

        if choice == "4":
            while True:
                taskid = input("Input task id-number of the task to edit (Press 'Q' to exit): ").strip().lower()
                if taskid == "q":
                    break
                else:
                    try:
                        service.get_exact_task(int(taskid))
                        title, notes, priority = edit_menu()
                        service.edit_task(int(taskid), title, notes, priority)
                        print(f"Task {taskid} edited")
                        print("----------")
                        break
                    except ValueError: 
                        print("ValueError: id inputted is not valid, try again")
                        print("----------")
            
        if choice == "5":
            while True:
                taskid = input("Input task id-number which to delete (Press 'Q' to exit): ").strip().lower()
                if taskid == "q":
                    break
                else:
                    try:
                        service.delete_task(int(taskid))
                        print(f"Task {taskid} deleted")
                        print("----------")
                        break
                    except ValueError:
                        print("ValueError: id inputted is not valid, try again")
                        print("----------")

        if choice == "q":
            print("Program will quit")
            print("----------")
            break

        else:
            continue


def handle_add_task():
    title = input("Please input a new task: ")
    while True:
        choice = input("Add notes or change priority? Y/N: ").strip().lower()
        if choice == "y":
            notes = input("Please input your notes: ")
            break
        if choice == "n":
            return title, None, None
        else:
            print("ValueError: Incorrect choice, choose for Y or N")
            print("----------")
            continue
    while True:
        choice_two = input("Change priority? Y/N: ").strip().lower()
        if choice_two == "y":
            priority = input("Please choose priority from 'low', 'normal' or 'high: ").strip().lower()
            if priority in {"low", "normal", "high"}:
                return title, notes, priority
            else:
                print("ValueError: Priority must be 'low', 'normal' or 'high'")
                print("----------")
                continue
        if choice_two == "n":
            return title, notes, None
        else:
            print("ValueError: Incorrect choice, choose for Y or N")
            print("----------")
            continue


def edit_menu():
    title = None
    notes = None
    priority = None

    while True:
        what_to_edit = input("Input what to edit: 1. Title - 2. Notes - 3. Priority - 4. Save edits: ")

        if what_to_edit == "1":
            title = input("Input new title: ")
            continue
        
        if what_to_edit == "2":
            notes = input("Input new notes: ")
            continue
        
        if what_to_edit == "3":
            priority = input("Input new priority (low, normal or high): ")
            print("----------")
            if priority not in {"low", "normal", "high"}:
                print("ValueError: Priority has to be from 'low', 'normal' or 'high'")
                print("Priority value not changed, try again!")
                print("----------")
                priority = None
                continue
            continue
        
        if what_to_edit == "4":
            return title, notes, priority
        
        else:
            print("ValueError: Input a valid choice from the options")
            print("----------")
            continue

if __name__ == "__main__":
    main_menu()