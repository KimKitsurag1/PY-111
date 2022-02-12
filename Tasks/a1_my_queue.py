"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self._queue=[]  

    def enqueue(self, elem: Any) -> None:
        self._queue.append(elem)
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        print(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if len(self._queue)==0:
            return None
        return self._queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if not isinstance(ind, int):
            raise TypeError
        elif ind > len(self._queue) - 1:
            return None
        return self._queue[ind]
        print(ind)

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self._queue=[]
        return None
