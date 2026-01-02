# Quickstart: Console Todo App

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Install dependencies (if any) using your preferred method
3. Clone or download the project repository

## Running the Application

1. Navigate to the project directory
2. Execute the main application file:
   ```bash
   python src/cli/main.py
   ```

## Using the Application

Once the application is running, you will see a command prompt where you can enter commands:

### Available Commands

- **Add a new todo**: `add "Description of your task"`
- **View all todos**: `list` or `view`
- **Mark a todo as complete**: `complete <id>`
- **Update a todo description**: `update <id> "New description"`
- **Delete a todo**: `delete <id>`
- **Exit the application**: `exit` or `quit`

### Example Workflow

1. Add a new task: `add "Write documentation"`
2. View your tasks: `list`
3. Mark the task as complete: `complete 1`
4. Update a task: `update 1 "Complete documentation"`
5. Delete a task: `delete 1`
6. Exit: `exit`

## Expected Output

The application will display:
- Success messages when operations complete
- Error messages when invalid commands or parameters are provided
- Formatted list of todos when viewing tasks