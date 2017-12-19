# Created for BADS 2018
# See README.md for details
# This is python3

"""
The Queue class represents a first-in-first-out (FIFO)
queue of generic items.
It supports the usual enqueue and dequeue
operations, along with methods for peeking at the first item,
testing if the queue is empty, and iterating through the items in FIFO order
This implementation uses a singly linked list with a nested class for the linked-list nodes
The enqueue, dequeue, peek, size, and is_empty operations all take constant time in the worst case
"""


class Queue:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0

    def enqueue(self, item):
        old_last = self._last
        self._last = self.Node(item, None)
        if self.is_empty():
            self._first = self._last
        else:
            old_last.next = self._last
        self._n += 1

    def dequeue(self):
        if not self.is_empty():
            item = self._first.item
            self._first = self._first.next
            self._n -= 1
            if self.is_empty():
                self._last = None
            return item

    def is_empty(self):
        return self._first is None

    def size(self):
        return self._n

    def peek(self):
        return self._first.item

    def __iter__(self):
        curr = self._first
        while curr is not None:
            yield curr.item
            curr = curr.next


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')

    while not queue.is_empty():
        print(queue.dequeue())