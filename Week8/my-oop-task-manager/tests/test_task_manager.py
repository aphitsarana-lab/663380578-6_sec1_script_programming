# my-oop-task-manager/tests/test_task_manager.py
import os
import sys
import tempfile
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from task import Task
from task_manager import TaskManager


class TestTask(unittest.TestCase):
    def test_new_task_is_pending(self):
        task = Task(1, "Read book")
        self.assertFalse(task.completed)
        self.assertIn("Pending", str(task))

    def test_mark_complete(self):
        task = Task(1, "Read book")
        task.mark_complete()
        self.assertTrue(task.completed)
        self.assertIn("Completed", str(task))

    def test_dict_round_trip(self):
        task = Task(3, "Write code", True)
        copy = Task.from_dict(task.to_dict())
        self.assertEqual((copy.id, copy.description, copy.completed), (3, "Write code", True))


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.file = os.path.join(self.tmp.name, "tasks.json")

    def tearDown(self):
        self.tmp.cleanup()

    def test_add_complete_delete(self):
        m = TaskManager(self.file)
        m.add_task("A")
        m.add_task("B")
        self.assertEqual([t.id for t in m.tasks], [1, 2])
        self.assertTrue(m.complete_task(1))
        self.assertTrue(m.get_task(1).completed)
        self.assertTrue(m.delete_task(2))
        self.assertFalse(m.delete_task(99))
        self.assertEqual(len(m.tasks), 1)

    def test_empty_description_rejected(self):
        m = TaskManager(self.file)
        self.assertIsNone(m.add_task("   "))
        self.assertEqual(m.tasks, [])

    def test_tasks_persist_between_runs(self):
        m = TaskManager(self.file)
        m.add_task("Saved task")
        m.complete_task(1)
        m2 = TaskManager(self.file)
        self.assertEqual(len(m2.tasks), 1)
        self.assertTrue(m2.tasks[0].completed)
        self.assertEqual(m2.add_task("Next").id, 2)


if __name__ == "__main__":
    unittest.main()
