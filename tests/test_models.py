import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'todo_list'))
from models import Task


def test_creating_task():
    task = Task(title="Buy milk", priority="high")
    assert task.title == "Buy milk"