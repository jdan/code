class StackOverflowException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class StackUnderflowException(Exception):
    def __init__(self):
        pass
    def __str__(self):
        pass

class Stack:
    def __init__(self, n):
        self.capacity = n
        self.s = [0] * n
        self.size = 0

    def push(self, val):
        try:
            if self.isFull():
                raise StackOverflowException(self.size)
            self.s[self.size] = val
            self.size += 1
        except StackOverflowException as soe:
            print 'Stack overflow at index', soe.value

    def pop(self):
        try:
            if self.isEmpty():
                raise StackUnderflowException
            self.size -= 1
            return self.s[self.size]
        except StackUnderflowException as sue:
            print 'Stack underflow.'
            return ''

    def top(self):
        return self.s[self.size - 1]

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0
