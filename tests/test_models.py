import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'todo_list'))
from models import Task


def test_creating_task():
    task = Task(id=2, title="Buy milk", notes="For coffee", priority="high", status="open")
    assert task.id == 2
    assert task.title == "Buy milk"
    assert task.notes == "For coffee"
    assert task.priority == "high"
    assert task.status == "open"