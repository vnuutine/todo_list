from dataclasses import dataclass
from typing import Literal
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    notes: str = ""
    priority: Literal["low", "normal", "high"] = "normal"
    status: Literal["open", "done"] = "open"
    created_at: str | None = None

    def __post_init__(self):
        self.title = self.title.strip()
        if self.title == "":
            raise ValueError("Invalid task title: title cannot be empty")
        
        self.priority = self.priority.strip().lower()
        if self.priority not in {"low", "normal", "high"}:
            raise ValueError("Invalid task priority: priority has to be 'low', 'normal' or 'high'")
        
        self.status = self.status.strip().lower()
        if self.status not in {"open", "done"}:
            raise ValueError("Invalid task status: status has to be 'open' or 'done'")
        
        if self.created_at is None:
            timestamp = datetime.now()
            self.created_at = timestamp.isoformat()