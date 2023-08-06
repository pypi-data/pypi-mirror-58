"""
Used to allow for function and their arguments to be stored.
"""

__all__ = ["Task"]

class Task:
    """
    Class used to store function that will be executed

    args:
        func : the function that will be executes
        callback : function that will run when processing has started and finished, callback("STARTED", "taskname")
        task_name : the name of the task which will be used in the callback
        args : any arguments that will be passed in the function
        kwargs : any kwargs that will be passed in the function
    """
    def __init__(self, func, callback=None, task_name="", args=(), kwargs={}):
        self.__func = func
        self.__callback = callback
        self.__task_name = task_name
        self.__args = args
        self.__kwargs = kwargs

    def execute(self):
        """
        Executes the task
        """
        if self.__callback:
            self.__callback("STARTED", self.__task_name)
            self.__func(*self.__args, **self.__kwargs)
            self.__callback("FINISHED", self.__task_name)
        else:
            self.__func(*self.__args, **self.__kwargs)
