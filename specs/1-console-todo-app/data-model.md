# Data Model: Console Todo App

## Todo Item Entity

### Attributes
- **id**: Unique identifier (integer or string) - automatically generated
- **description**: Text description of the task (string, required)
- **completed**: Boolean indicating completion status (boolean, default: False)
- **created_at**: Timestamp when the task was created (datetime, optional for this implementation)

### Validation Rules
- **description**: Must not be empty or consist only of whitespace
- **id**: Must be unique within the current session
- **completed**: Can only be True or False

### State Transitions
- **Incomplete → Complete**: When user marks task as complete
- **Complete → Incomplete**: When user marks task as incomplete (if this functionality is implemented)

## In-Memory Storage Structure

### Data Container
- **todo_list**: List/array of Todo Item objects
- **next_id**: Integer counter to assign unique IDs to new items

### Operations
- **Add**: Append new Todo Item to the list
- **Delete**: Remove Todo Item from the list by ID
- **Update**: Modify existing Todo Item properties by ID
- **View**: Retrieve Todo Item(s) from the list by criteria
- **Mark Complete**: Update the completed status of a Todo Item by ID

## Relationships
- No relationships needed as this is a single-entity application
- All operations are self-contained within the Todo Item structure