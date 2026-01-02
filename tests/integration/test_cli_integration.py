"""
Integration tests for the CLI application.
"""
import io
import sys
from unittest.mock import patch, MagicMock
from src.cli.main import TodoApp


def test_add_and_list_todos():
    """
    Test adding a todo and then listing it.
    """
    app = TodoApp()

    # Add a todo
    app.todo_manager.add("Test task")

    # Verify it exists
    todos = app.todo_manager.list_all()
    assert len(todos) == 1
    assert todos[0].description == "Test task"
    assert not todos[0].completed


def test_complete_todo():
    """
    Test marking a todo as complete.
    """
    app = TodoApp()

    # Add a todo
    todo = app.todo_manager.add("Test task")
    todo_id = todo.id

    # Mark as complete
    success = app.todo_manager.mark_complete(todo_id)
    assert success

    # Verify it's marked as complete
    updated_todo = app.todo_manager.get_by_id(todo_id)
    assert updated_todo is not None
    assert updated_todo.completed


def test_update_todo():
    """
    Test updating a todo description.
    """
    app = TodoApp()

    # Add a todo
    todo = app.todo_manager.add("Original task")
    todo_id = todo.id

    # Update the description
    success = app.todo_manager.update(todo_id, "Updated task")
    assert success

    # Verify the description was updated
    updated_todo = app.todo_manager.get_by_id(todo_id)
    assert updated_todo is not None
    assert updated_todo.description == "Updated task"


def test_delete_todo():
    """
    Test deleting a todo.
    """
    app = TodoApp()

    # Add a todo
    todo = app.todo_manager.add("Test task to delete")
    todo_id = todo.id

    # Verify it exists
    assert app.todo_manager.get_by_id(todo_id) is not None

    # Delete it
    success = app.todo_manager.delete(todo_id)
    assert success

    # Verify it's gone
    assert app.todo_manager.get_by_id(todo_id) is None


def test_todo_counts():
    """
    Test that todo counts work correctly.
    """
    app = TodoApp()

    # Start with no todos
    assert app.todo_manager.count() == 0
    assert app.todo_manager.count_completed() == 0
    assert app.todo_manager.count_pending() == 0

    # Add one pending todo
    app.todo_manager.add("Pending task")
    assert app.todo_manager.count() == 1
    assert app.todo_manager.count_completed() == 0
    assert app.todo_manager.count_pending() == 1

    # Add another pending todo
    app.todo_manager.add("Another pending task")
    assert app.todo_manager.count() == 2
    assert app.todo_manager.count_completed() == 0
    assert app.todo_manager.count_pending() == 2

    # Complete one
    app.todo_manager.mark_complete(1)  # Assuming first todo has ID 1
    assert app.todo_manager.count() == 2
    assert app.todo_manager.count_completed() == 1
    assert app.todo_manager.count_pending() == 1


if __name__ == "__main__":
    # Run the tests
    test_add_and_list_todos()
    print("✓ test_add_and_list_todos passed")

    test_complete_todo()
    print("✓ test_complete_todo passed")

    test_update_todo()
    print("✓ test_update_todo passed")

    test_delete_todo()
    print("✓ test_delete_todo passed")

    test_todo_counts()
    print("✓ test_todo_counts passed")

    print("\nAll integration tests passed!")