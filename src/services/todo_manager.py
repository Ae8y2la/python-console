"""
TodoManager service handling all todo-related operations.
"""
from typing import List, Optional
from src.models.todo_item import TodoItem
from src.lib.utils import get_next_id


class TodoManager:
    """
    Core service class that manages all todo operations in memory.
    """
    def __init__(self):
        self.todos: List[TodoItem] = []
        self.id_generator = get_next_id

    def add(self, description: str) -> TodoItem:
        """
        Add a new todo item with the given description.

        Args:
            description: The description of the new todo item

        Returns:
            The created TodoItem with assigned ID
        """
        # Validate description
        if not description or not description.strip():
            raise ValueError("Description cannot be empty or just whitespace")

        # Create new todo item with unique ID
        new_id = get_next_id()
        todo_item = TodoItem(id=new_id, description=description.strip())
        self.todos.append(todo_item)

        return todo_item

    def list_all(self) -> List[TodoItem]:
        """
        Get all todo items.

        Returns:
            List of all todo items
        """
        return self.todos.copy()

    def get_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """
        Get a todo item by its ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The TodoItem if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo item as complete by its ID.

        Args:
            todo_id: The ID of the todo item to mark complete

        Returns:
            True if the item was found and updated, False otherwise
        """
        todo = self.get_by_id(todo_id)
        if todo:
            todo.mark_complete()
            return True
        return False

    def mark_incomplete(self, todo_id: int) -> bool:
        """
        Mark a todo item as incomplete by its ID.

        Args:
            todo_id: The ID of the todo item to mark incomplete

        Returns:
            True if the item was found and updated, False otherwise
        """
        todo = self.get_by_id(todo_id)
        if todo:
            todo.mark_incomplete()
            return True
        return False

    def update(self, todo_id: int, new_description: str) -> bool:
        """
        Update the description of a todo item by its ID.

        Args:
            todo_id: The ID of the todo item to update
            new_description: The new description for the todo item

        Returns:
            True if the item was found and updated, False otherwise
        """
        if not new_description or not new_description.strip():
            raise ValueError("Description cannot be empty or just whitespace")

        todo = self.get_by_id(todo_id)
        if todo:
            todo.update_description(new_description.strip())
            return True
        return False

    def delete(self, todo_id: int) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            todo_id: The ID of the todo item to delete

        Returns:
            True if the item was found and deleted, False otherwise
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def count(self) -> int:
        """
        Get the total number of todo items.

        Returns:
            The count of todo items
        """
        return len(self.todos)

    def count_completed(self) -> int:
        """
        Get the number of completed todo items.

        Returns:
            The count of completed todo items
        """
        return sum(1 for todo in self.todos if todo.completed)

    def count_pending(self) -> int:
        """
        Get the number of pending (not completed) todo items.

        Returns:
            The count of pending todo items
        """
        return sum(1 for todo in self.todos if not todo.completed)