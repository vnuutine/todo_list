import sys
import pytest

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'todo_list'))

from models import Task
from datetime import datetime


def test_task_defaults():
    task = Task(id=1, title="Test task")
    assert task.notes == ""
    assert task.priority == "normal"
    assert task.status == "open"

def test_empty_title_raises_value_error():
    with pytest.raises(ValueError):
        Task(id=1, title="")

def test_whitespace_title_raises_value_error():
    with pytest.raises(ValueError):
        Task(id=1, title="   ")

def test_none_title_raises_value_error():
    with pytest.raises(ValueError):
        Task(id=1, title=None)

def test_invalid_priority_raises_value_error():
    with pytest.raises(ValueError):
        task = Task(id=1, title="Test task", priority="Banana")

def test_invalid_status_raises_value_error():
    with pytest.raises(ValueError):
        task = Task(id=1, title="Test task", status="Banana")

def test_new_task_has_created_at():
    task = Task(id=1, title="Test task")
    assert task.created_at is not None
    assert isinstance(task.created_at, str)

def test_done_task_has_completed_at():
    task = Task(id=1, title="Test task", status="done")
    assert task.completed_at is not None
    assert isinstance(task.completed_at, str)

def test_open_task_has_none_completed_at():
    task = Task(id=1, title="Test task", status="open")
    assert task.completed_at is None