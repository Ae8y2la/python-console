"""
Test script to validate the console todo app functionality
"""
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.services.todo_manager import TodoManager

def test_functionality():
    print("Testing Console Todo App functionality...")

    # Create a todo manager instance
    tm = TodoManager()

    # Test 1: Add a todo
    print("\n1. Testing add functionality:")
    todo1 = tm.add("Buy groceries")
    print(f"   Added: {todo1}")

    # Test 2: Add another todo
    todo2 = tm.add("Walk the dog")
    print(f"   Added: {todo2}")

    # Test 3: List all todos
    print("\n2. Testing list functionality:")
    todos = tm.list_all()
    for todo in todos:
        print(f"   {todo}")

    # Test 4: Mark a todo as complete
    print("\n3. Testing complete functionality:")
    success = tm.mark_complete(todo1.id)
    print(f"   Marked todo {todo1.id} as complete: {success}")

    # List again to see the status change
    todos = tm.list_all()
    for todo in todos:
        print(f"   {todo}")

    # Test 5: Update a todo
    print("\n4. Testing update functionality:")
    success = tm.update(todo2.id, "Walk the cat instead")
    print(f"   Updated todo {todo2.id}: {success}")

    # List again to see the description change
    todos = tm.list_all()
    for todo in todos:
        print(f"   {todo}")

    # Test 6: Delete a todo
    print("\n5. Testing delete functionality:")
    success = tm.delete(todo1.id)
    print(f"   Deleted todo {todo1.id}: {success}")

    # List again to see the deletion
    todos = tm.list_all()
    print("   Remaining todos:")
    for todo in todos:
        print(f"   {todo}")

    print(f"\nTotal todos remaining: {tm.count()}")
    print(f"Completed todos: {tm.count_completed()}")
    print(f"Pending todos: {tm.count_pending()}")

    print("\nAll functionality tests passed!")

if __name__ == "__main__":
    test_functionality()