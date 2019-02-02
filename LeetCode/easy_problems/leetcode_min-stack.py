class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            if x <= self.min_val[-1]:
                self.min_val.append(x)
        else:
            self.min_val.append(x)

        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.min_val[-1]:
            self.min_val.pop()

        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val[-1]


# test cases
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.getMin()
# minStack.pop()
# minStack.top()
# minStack.getMin()

# minStack = MinStack()
# minStack.push(0)
# minStack.push(1)
# minStack.push(0)
# minStack.getMin()
# minStack.pop()
# minStack.getMin()

# minStack = MinStack()
# minStack.push(2)
# minStack.push(0)
# minStack.push(3)
# minStack.push(0)
# minStack.getMin()
# minStack.pop()
# minStack.getMin()
# minStack.pop()
# minStack.getMin()
# minStack.pop()
# minStack.getMin()
