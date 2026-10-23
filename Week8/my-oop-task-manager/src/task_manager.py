# my-oop-task-manager/src/task_manager.py
import json
import os

from task import Task


class TaskManager:
    """
    Manages a collection of Task objects and saves/loads them from a JSON file.
    """

    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self._load_tasks()

    # ---------- File handling (internal) ----------
    def _load_tasks(self):
        """Load tasks from the JSON file and turn them into Task objects."""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(item) for item in data]
            if self.tasks:
                self.next_id = max(task.id for task in self.tasks) + 1
        except (json.JSONDecodeError, KeyError):
            print("Warning: tasks file is corrupted. Starting with an empty list.")
            self.tasks = []
            self.next_id = 1

    def _save_tasks(self):
        """Save all Task objects to the JSON file."""
        folder = os.path.dirname(self.filename)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4, ensure_ascii=False)

    # ---------- Public operations ----------
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def add_task(self, description):
        description = description.strip()
        if not description:
            print("Task description cannot be empty.")
            return None
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        self._save_tasks()
        print(f"Task '{description}' added with ID {task.id}.")
        return task

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n--- Your Tasks ---")
        for task in self.tasks:
            print(task)
        print("------------------")

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task is None:
            print(f"Task with ID {task_id} not found.")
            return False
        task.mark_complete()
        self._save_tasks()
        print(f"Task {task_id} marked as complete.")
        return True

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task is None:
            print(f"Task with ID {task_id} not found.")
            return False
        self.tasks.remove(task)
        self._save_tasks()
        print(f"Task {task_id} deleted.")
        return True
