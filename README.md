# Todo List CLI

A simple command-line todo list application built with Python. This project helps you manage your tasks through an easy-to-use terminal interface.

## Features

- Add new tasks with optional notes and priority levels
- View tasks by status (open/done) or priority
- Edit existing tasks (title, notes, priority)
- Delete tasks you no longer need
- Search for specific tasks by ID
- Automatic timestamps for task creation and completion
- Data persistence using JSON storage

## Requirements

- Python 3.11 or higher

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd todo_list
```

2. Install the package:
```bash
pip install -e .
```

## Usage

After installation, run the application using:

```bash
todo
```

### Main Menu Options

When you start the app, you'll see these options:

1. **Add new task** - Create a new todo item
2. **View your tasks** - Browse and filter your tasks
3. **Mark task done** - Mark an open task to done
4. **Edit task** - Modify an existing task
5. **Delete task** - Remove a task permanently
Q. **Press 'Q' to quit** - Exit the application

### Task Properties

Each task has the following properties:

- **Title** (required) - A short description of your task
- **Notes** (optional) - Additional details or context
- **Priority** (optional) - Set to `low`, `normal`, or `high` (defaults to `normal`)
- **Status** - Automatically set to `open` when created, can be marked as `done`
- **Created at** - Timestamp of when the task was created
- **Completed at** - Timestamp of when the task was marked as done

### Viewing Tasks

The "View your tasks" menu lets you filter tasks in different ways:

- View all open tasks
- View all completed tasks
- Find a specific task by its ID number
- Filter tasks by priority level

### Examples

**Adding a task:**
```
Input: 1
Please input a new task: Buy groceries
Add notes or change priority? Y/N: y
Please input your notes: milk, eggs, bread
Change priority? Y/N: y
Please choose priority from 'low', 'normal' or 'high': high
```

**Viewing open tasks:**
```
Input: 2
Input: 1
(Shows all tasks with status "open")
```

## Project Structure

```
todo_list/
├── todo_list/
│   ├── cli.py        # Command-line interface and user interaction
│   ├── models.py     # Task data model definition
│   ├── service.py    # Business logic for task operations
│   └── storage.py    # JSON file handling for data persistence
├── tests/            # Test files
├── data/             # Storage directory for tasks (created automatically)
├── pyproject.toml    # Project configuration
└── README.md         # This file
```

## Development

### Running Tests

To run the test suite:

```bash
pytest
```

### Installing Development Dependencies

```bash
pip install -e ".[dev]"
```

## Data Storage

Tasks are stored in a JSON file at `data/storage.json`. The file is created automatically when you first run the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Ville Nuutinen
