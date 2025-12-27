import service


def main_menu():
    while True:
        print("Choose action")
        print("1. Add new task")
        print("2. View your tasks")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Quit")
        choice = input("What would you like to do: ").strip().lower()

        if choice == "1":
            title, notes, priority = handle_add_task()
            service.add_task(title, notes, priority)
            print(f"New task: {title} added")
        
        if choice == "2":
            pass

        if choice == "3":
            taskid = input("Input task id-number of the task to edit: ")
            try:
                service.get_exact_task(taskid)
                title, notes, priority = edit_menu()
                service.edit_task(int(taskid), title, notes, priority)
                print(f"Task {taskid} edited")
            except ValueError: 
                print("ValueError: id inputted is not valid, try again")
              # TODO : Fix logic, now user sent back to main menu after error (build a loop)  
            
        if choice == "4":
            taskid = input("Input task id-number which to delete: ")
            service.delete_task(int(taskid))
            print(f"Task {taskid} deleted")
            # TODO : Add same kind of logic like in 3, handle errors and loop till correct id or quit

        if choice == "5":
            print("Program will quit")
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
            continue
    while True:
        choice_two = input("Change priority? Y/N: ").strip().lower()
        if choice_two == "y":
            priority = input("Please choose priority from 'low', 'normal' or 'high: ").strip().lower()
            if priority in {"low", "normal", "high"}:
                return title, notes, priority
            else:
                print("ValueError: Priority must be 'low', 'normal' or 'high'")
                continue
        if choice_two == "n":
            return title, notes, None
        else:
            print("ValueError: Incorrect choice, choose for Y or N")
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
            if priority not in {"low", "normal", "high"}:
                print("ValueError: Priority has to be from 'low', 'normal' or 'high'")
                print("Priority value not changed, try again!")
                priority = None
                continue
            continue
        
        if what_to_edit == "4":
            return title, notes, priority
        
        else:
            print("ValueError: Input a valid choice from the options")
            continue

main_menu()