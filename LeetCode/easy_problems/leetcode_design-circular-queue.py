class MyCircularQueue:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = []
        self.size = k
        self.head = None
        self.tail = None

    def enQueue(self, value: 'int') -> 'bool':
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.queue) != self.size:
            self.queue.append(value)
            self.tail = value

            if len(self.queue) == 1:
                self.head = value

            return True
        else:
            return False

    def deQueue(self) -> 'bool':
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.queue:
            return False

        if len(self.queue) == 1:
            self.queue.pop(0)
            self.head = None
            self.tail = None

            return True

        elif len(self.queue) == 2:
            self.queue.pop(0)
            self.head = self.tail

            return True

        else:
            self.queue.pop(0)
            self.head = self.queue[0]

            return True

    def Front(self) -> 'int':
        """
        Get the front item from the queue.
        """
        if not self.queue:
            return -1

        return self.head

    def Rear(self) -> 'int':
        """
        Get the last item from the queue.
        """
        if not self.queue:
            return -1

        return self.tail

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular queue is empty or not.
        """
        if self.queue:
            return False
        else:
            return True

    def isFull(self) -> 'bool':
        """
        Checks whether the circular queue is full or not.
        """
        if len(self.queue) == self.size:
            return True
        else:
            return False


# test cases
# circularQueue = MyCircularQueue(3)
# circularQueue.enQueue(1)  # return true
# circularQueue.enQueue(2)  # return true
# circularQueue.enQueue(3)  # return true
# circularQueue.enQueue(4)  # return false, the queue is full
# circularQueue.Rear()  # return 3
# circularQueue.isFull()  # return true
# circularQueue.deQueue()  # return true
# circularQueue.enQueue(4)  # return true
# circularQueue.Rear()  # return 4