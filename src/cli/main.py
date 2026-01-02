"""
Main CLI application for the todo console app.
"""
import sys
import argparse
from typing import List
from src.services.todo_manager import TodoManager


class TodoApp:
    """
    Main CLI application class that handles user interaction.
    """
    def __init__(self):
        self.todo_manager = TodoManager()
        self.running = True

    def run(self):
        """
        Run the main application loop.
        """
        print("Welcome to the Todo Console App!")
        print("Available commands: add, list, complete, update, delete, exit")
        print("Type 'help' for more information or 'exit' to quit.\n")

        while self.running:
            try:
                user_input = input("todo> ").strip()
                if not user_input:
                    continue

                command_parts = user_input.split()
                command = command_parts[0].lower()

                if command == 'exit' or command == 'quit':
                    self.handle_exit()
                elif command == 'help':
                    self.handle_help()
                elif command == 'add':
                    self.handle_add(command_parts[1:])
                elif command == 'list' or command == 'view':
                    self.handle_list()
                elif command == 'complete':
                    self.handle_complete(command_parts[1:])
                elif command == 'update':
                    self.handle_update(command_parts[1:])
                elif command == 'delete':
                    self.handle_delete(command_parts[1:])
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")

    def handle_add(self, args: List[str]):
        """
        Handle the add command.
        """
        if len(args) == 0:
            print("Usage: add \"description of the task\"")
            return

        description = " ".join(args)
        # Remove quotes if they exist
        if description.startswith('"') and description.endswith('"'):
            description = description[1:-1]
        elif description.startswith("'") and description.endswith("'"):
            description = description[1:-1]

        try:
            todo = self.todo_manager.add(description)
            print(f"Added todo: {todo}")
        except ValueError as e:
            print(f"Error adding todo: {e}")

    def handle_list(self):
        """
        Handle the list/view command.
        """
        todos = self.todo_manager.list_all()

        if not todos:
            print("No todos found.")
            return

        print(f"Total todos: {len(todos)}")
        for todo in todos:
            status = "✓" if todo.completed else "○"
            print(f"[{status}] {todo.id}: {todo.description}")

    def handle_complete(self, args: List[str]):
        """
        Handle the complete command.
        """
        if len(args) != 1:
            print("Usage: complete <id>")
            return

        try:
            todo_id = int(args[0])
            success = self.todo_manager.mark_complete(todo_id)
            if success:
                print(f"Marked todo {todo_id} as complete")
            else:
                print(f"Todo with ID {todo_id} not found")
        except ValueError:
            print("Usage: complete <id> (id must be a number)")

    def handle_update(self, args: List[str]):
        """
        Handle the update command.
        """
        if len(args) < 2:
            print("Usage: update <id> \"new description\"")
            return

        try:
            todo_id = int(args[0])
            new_description = " ".join(args[1:])
            # Remove quotes if they exist
            if new_description.startswith('"') and new_description.endswith('"'):
                new_description = new_description[1:-1]
            elif new_description.startswith("'") and new_description.endswith("'"):
                new_description = new_description[1:-1]

            success = self.todo_manager.update(todo_id, new_description)
            if success:
                print(f"Updated todo {todo_id}")
            else:
                print(f"Todo with ID {todo_id} not found")
        except ValueError:
            print("Usage: update <id> \"new description\" (id must be a number)")

    def handle_delete(self, args: List[str]):
        """
        Handle the delete command.
        """
        if len(args) != 1:
            print("Usage: delete <id>")
            return

        try:
            todo_id = int(args[0])
            success = self.todo_manager.delete(todo_id)
            if success:
                print(f"Deleted todo {todo_id}")
            else:
                print(f"Todo with ID {todo_id} not found")
        except ValueError:
            print("Usage: delete <id> (id must be a number)")

    def handle_help(self):
        """
        Handle the help command.
        """
        help_text = """
Available commands:
  add "description"     - Add a new todo
  list / view          - View all todos
  complete <id>        - Mark a todo as complete
  update <id> "desc"   - Update a todo's description
  delete <id>          - Delete a todo
  help                 - Show this help message
  exit / quit          - Exit the application
        """
        print(help_text)

    def handle_exit(self):
        """
        Handle the exit command.
        """
        print("Goodbye!")
        self.running = False


def main():
    """
    Main entry point for the application.
    """
    parser = argparse.ArgumentParser(description='Console Todo Application')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Start in interactive mode (default behavior)')

    args = parser.parse_args()

    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()