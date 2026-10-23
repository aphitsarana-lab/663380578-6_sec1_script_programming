# my-oop-task-manager/src/task.py


class Task:
    """
    Represents a single task (one object = one task).
    """

    def __init__(self, task_id, description, completed=False):
        self.id = task_id
        self.description = description
        self.completed = completed

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert the Task object to a dictionary (for saving to JSON)."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from a dictionary (when loading from JSON)."""
        return cls(data["id"], data["description"], data.get("completed", False))

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"ID: {self.id} | Description: {self.description} | Status: {status}"

    def __repr__(self):
        return f"Task(id={self.id}, description={self.description!r}, completed={self.completed})"
