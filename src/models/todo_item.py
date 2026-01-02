"""
TodoItem model representing a single todo task.
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class TodoItem:
    """
    Represents a single todo item with an ID, description, and completion status.
    """
    id: int
    description: str
    completed: bool = False
    created_at: Optional[datetime] = None

    def __post_init__(self):
        """Validate the TodoItem after initialization."""
        if not self.description or not self.description.strip():
            raise ValueError("Description cannot be empty or just whitespace")

        if self.created_at is None:
            self.created_at = datetime.now()

    def mark_complete(self):
        """Mark this todo item as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark this todo item as incomplete."""
        self.completed = False

    def update_description(self, new_description: str):
        """Update the description of this todo item."""
        if not new_description or not new_description.strip():
            raise ValueError("Description cannot be empty or just whitespace")
        self.description = new_description.strip()

    def __str__(self):
        """String representation of the todo item."""
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.description}"