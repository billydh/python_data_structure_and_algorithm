class MovingAverage:

    def __init__(self, size: 'int'):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.head = None
        self.tail = None
        self.queue = []
        self.cumsum = 0

    def next(self, val: 'int') -> 'float':
        self.cumsum += val

        if len(self.queue) < self.size:
            self.queue.append(val)
        else:
            self.cumsum -= self.queue[0]
            self.queue.pop(0)
            self.queue.append(val)

        return self.cumsum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)