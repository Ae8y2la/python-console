# Todo App API Contracts

## Command Interface Contracts

### Add Todo Command
- **Command**: `add "description text"`
- **Input**: String description (non-empty, not just whitespace)
- **Output**: Success message with assigned ID or error message
- **State Change**: New todo item added to in-memory list
- **Validation**: Description must not be empty

### List Todos Command
- **Command**: `list` or `view`
- **Input**: None
- **Output**: Formatted list of all todos with ID, description, and completion status
- **State Change**: None (read-only operation)

### Complete Todo Command
- **Command**: `complete <id>`
- **Input**: Valid todo ID (integer)
- **Output**: Success confirmation or error message
- **State Change**: Todo item's completion status set to True
- **Validation**: ID must exist in current session

### Update Todo Command
- **Command**: `update <id> "new description"`
- **Input**: Valid todo ID (integer) and non-empty description string
- **Output**: Success confirmation or error message
- **State Change**: Todo item's description updated
- **Validation**: ID must exist, description must not be empty

### Delete Todo Command
- **Command**: `delete <id>`
- **Input**: Valid todo ID (integer)
- **Output**: Success confirmation or error message
- **State Change**: Todo item removed from in-memory list
- **Validation**: ID must exist in current session

### Exit Command
- **Command**: `exit` or `quit`
- **Input**: None
- **Output**: None (application terminates)
- **State Change**: Application terminates, in-memory data is lost