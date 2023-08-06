from collections import deque as _deque
class Queue_Peek:
    """
    Queue that has a 'peek' function
    """
    __items = _deque()

    def empty(self):
        """
        returns bool whether the queue is empty

        TRUE : is empty
        FALSE : is not empty
        """
        if len(self.__items) == 0:
            return True
        else:
            return False

    @property
    def size(self):
        """
        Returns the length of the queue
        """
        return len(self.__items)

    def peek(self):
        """
        returns the next queue item without removing
        """
        if not self.empty():
            return self.__items[0]

    def pop(self):
        """
        returns the next queue item removing it from the queue
        """
        if not self.empty():
            return self.__items.popleft()

    def push(self, new_item):
        """
        adds a new item to the queue
        """
        self.__items.append(new_item)
