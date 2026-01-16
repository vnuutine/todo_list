import sys
import pytest

from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'todo_list'))

from todo_list.models import Task

@pytest.fixture
def sample_tasks():
    return [
        Task(id=1, title="Test task 1", priority="normal", status="open"),
        Task(id=2, title="Test task 2", priority="low", status="done"),
        Task(id=3, title="Test task 3", priority="high", status="open")
    ]


def test_add_task():
    pass