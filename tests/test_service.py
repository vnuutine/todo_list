import pytest
from unittest.mock import patch
from todo_list.models import Task
from todo_list import service

@pytest.fixture
def sample_tasks():
    return [
        Task(id=1, title="Test task 1", priority="normal", status="open"),
        Task(id=2, title="Test task 2", priority="low", status="done"),
        Task(id=3, title="Test task 3", priority="high", status="open")
    ]


def test_add_task(sample_tasks):
    with patch("todo_list.storage.load_all_tasks") as mock_load, \
         patch("todo_list.storage.save_all_tasks") as mock_save:
        
        mock_load.return_value = [
            {"id": 1, "title": "Test task 1", "notes": "", "priority": "normal", "status": "open"},
            {"id": 2, "title": "Test task 2", "notes": "", "priority": "low", "status": "done"}
        ]
        
        service.add_task(title="New task", priority="high")

        assert mock_save.called
        
        saved_tasks = mock_save.call_args[0][0]

        assert len(saved_tasks) == 3
        assert saved_tasks[2]["title"] == "New task"
        assert saved_tasks[2]["priority"] == "high"
        assert saved_tasks[2]["id"] == 3


def test_get_exact_task(sample_tasks):
    with patch("todo_list.storage.load_all_tasks") as mock_load:
        
        mock_load.return_value = [
            {"id": 1, "title": "Test task 1", "notes": "", "priority": "normal", "status": "open"},
            {"id": 2, "title": "Test task 2", "notes": "", "priority": "low", "status": "done"}
        ]

        exact_task = service.get_exact_task(2)

        assert isinstance(exact_task, Task)
        assert exact_task.title == "Test task 2"
        assert exact_task.priority == "low"
        assert exact_task.id == 2


def test_get_exact_task_not_found(sample_tasks):
    with patch("todo_list.storage.load_all_tasks") as mock_load:

        mock_load.return_value = [
            {"id": 1, "title": "Test task 1", "notes": "", "priority": "normal", "status": "open"},
            {"id": 2, "title": "Test task 2", "notes": "", "priority": "low", "status": "done"}
        ]

        with pytest.raises(ValueError):
            exact_task = service.get_exact_task(999)


def test_get_exact_task_is_none(sample_tasks):
    with patch("todo_list.storage.load_all_tasks") as mock_load:

        mock_load.return_value = [
            {"id": 1, "title": "Test task 1", "notes": "", "priority": "normal", "status": "open"},
            {"id": 2, "title": "Test task 2", "notes": "", "priority": "low", "status": "done"}
        ]

        with pytest.raises(ValueError):
            exact_task = service.get_exact_task(None)