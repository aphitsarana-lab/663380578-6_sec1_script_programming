# Week 8: OOP Fundamentals & Refactoring the CLI Task Manager

The CLI Task Manager rewritten with **Object-Oriented Programming**:
a `Task` class for one task, and a `TaskManager` class that owns the list of tasks,
saves them to `data/tasks.json`, and performs every operation.

## How to Run

```bash
cd week8/my-oop-task-manager
python3 main.py                      # run the CLI (Windows: python main.py)
python3 -m unittest discover -v      # run the unit tests
```

Uses only the Python standard library, so there is nothing to install.

```
--- OOP Task Manager Menu ---
1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit
```

## Class Design

| Class | Attributes | Methods |
|-------|------------|---------|
| `Task` | `id`, `description`, `completed` | `mark_complete()`, `to_dict()`, `from_dict()`, `__str__()`, `__repr__()` |
| `TaskManager` | `filename`, `tasks`, `next_id` | `add_task()`, `list_tasks()`, `complete_task()`, `delete_task()`, `get_task()`, `_load_tasks()`, `_save_tasks()` |

## OOP Concepts Used

- **Class / Object**: `Task(1, "Read book")` creates one Task object.
- **Constructor (`__init__`)**: sets each object's attributes; `TaskManager.__init__` also loads saved tasks.
- **Encapsulation**: `main.py` only calls `TaskManager` methods. The file handling is hidden in `_load_tasks()` / `_save_tasks()`.
- **Special methods**: `__str__` prints a readable task, `__repr__` is used for debugging.
- **Class method**: `Task.from_dict()` builds a Task from data loaded from JSON.

## Before vs After (Refactoring)

| Procedural (before) | OOP (after) |
|---------------------|-------------|
| Tasks stored as plain dictionaries | Each task is a `Task` object |
| Separate functions plus a global list | `TaskManager` keeps the list and its operations together |
| Load/save code mixed with menu code | Load/save hidden inside `TaskManager` |

## Project Structure

```
my-oop-task-manager/
├── src/
│   ├── __init__.py
│   ├── task.py           # Task class
│   └── task_manager.py   # TaskManager class
├── data/
│   └── tasks.json        # saved tasks
├── tests/
│   └── test_task_manager.py
├── main.py               # CLI menu
├── .gitignore
└── README.md
```
