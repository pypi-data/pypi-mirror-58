"""
Allows functions to be called in a seperate thread and executed in FIFO order.

To Use:
    from threaded_task_executor import Task_Queue, Task
"""
from .task_queue import Task_Queue
from .task import Task
from .queue_peek import Queue_Peek

__all__ = ["Task_Queue", "Task", "Queue_Peek"]
__version__ = "1.1"
__author__ = "enchant97"
