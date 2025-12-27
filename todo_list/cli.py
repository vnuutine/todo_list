import service


def main_menu():
    while True:
        pass


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

handle_add_task()