# Threaded Task Executor
Allows functions to be called in a seperate thread and executed in FIFO order.
## Possible Uses:
- For serial communication where send/recv order matters
- Run background tasks in tkinter easily, without freezing gui
- Any application where background tasks are required to be executed in order
## Gettings Started:
### Installing
```
pip install threaded-task-executor
```
### Importing
```python
from threaded_task_executor import Task_Queue, Task
```
### How To Use
```python
tasks = Task_Queue()
tasks.add_task(Task(print, args=("test 1")))
tasks.add_task(Task(print, args=("test 2")))
```
When this is run it should start the thread
and execute the tasks in FIFO order.

## Documentation:
```python
Task(func, callback=None, task_name="", args=(), kwargs={})
```
- func : the function that will be called when executed
- callback : function that will be run when the task has started and finished
    - callback("STARTED", task_name)
    - callback("FINISHED", task_name)
- task_name : the name of the task
- args : tuple of arguments that will be given to the function
- kwargs : dict of keyword arguments that will be given to the function

```python
Task_Queue(daemon=None)
```
- daemon : (True, False, None) : Whether main thread has to wait for thread to finish before stopping main thread
- add_task(new_task) : Adds a new task obj, if there is no threads running will start one
- get_current_task() : Allows for the current task that is executing to be returned
- tasks_left() : Returns the number of tasks left to be completed, includes currently executing task if any.
- add_from_func(callback, task_name) : used as a decorator which acts as add_task()

## Updates:
### 1.1
- New decorator method that allows for adding to a Task_Queue obj
### 1.0
First version
