# Console Todo App 👾

A simple command-line todo application that manages tasks entirely in memory.

## ✨Features

- Add new todo items
- View all todo items
- Mark todo items as complete
- Update todo item descriptions
- Delete todo items
- All data stored in memory only (no persistence)

## 🎥 Live Demo

[![Watch Demo](https://img.shields.io/badge/%F0%9F%8E%A5_Watch_Now-9146FF?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/1qjc6v6Op5sQH2Jy9ikDNHkJo_W2k74mx/view?usp=sharing)

## Requirements

- Python 3.13+

## Usage

1. Run the application:
   ```bash
   python src/cli/main.py
   ```

2. The application will start and show a prompt:
   ```
   todo>
   ```

3. Use the following commands:
   - `add "description"` - Add a new todo
   - `list` or `view` - View all todos
   - `complete <id>` - Mark a todo as complete
   - `update <id> "new description"` - Update a todo description
   - `delete <id>` - Delete a todo
   - `help` - Show help information
   - `exit` or `quit` - Exit the application

## Example

```
todo> add "Buy groceries"
Added todo: [○] 1: Buy groceries

todo> add "Walk the dog"
Added todo: [○] 2: Walk the dog

todo> list
Total todos: 2
[○] 1: Buy groceries
[○] 2: Walk the dog

todo> complete 1
Marked todo 1 as complete

todo> list
Total todos: 2
[✓] 1: Buy groceries
[○] 2: Walk the dog

todo> exit
Goodbye!
```

## Project Structure

```
src/
├── models/
│   └── todo_item.py     # Todo item data model
├── services/
│   └── todo_manager.py  # Core business logic
├── cli/
│   └── main.py          # Console interface and main application loop
└── lib/
    └── utils.py         # Utility functions
```

## Development

The application follows a layered architecture:
- **Models**: Data structures (TodoItem)
- **Services**: Business logic (TodoManager)
- **CLI**: User interface (TodoApp)
- **Lib**: Utility functions (IdGenerator)

## Testing

To run the application manually:
1. Start the application: `python src/cli/main.py`
2. Test each command as described above

## 🙌 Contributing

I welcome contributions to make this Console Python Todo App even better!  

**📌 Guidelines:**  
- Follow the existing project structure (`src/models`, `src/services`, `src/cli`, `src/lib`).  
- Ensure new features or fixes maintain the in-memory architecture.  
- Keep code clean, modular, and well-commented.  
- Add examples or test steps if you add new commands or functionality.  

**🐞 Reporting Issues:**  
- Found a bug or unexpected behavior? Open an issue on GitHub with a clear description and steps to reproduce it.  

**✨ Pull Requests:**  
- Fork the repository, make your changes, and submit a pull request.  
- Include a concise description of what you added, fixed, or improved.  
- Make sure your code passes manual testing for all commands.  

⭐ If you find this project useful, give it a star on GitHub to show your support!
