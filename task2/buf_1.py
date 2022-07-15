""" Буфер FIFO на list() """


class BuffList:
    def __init__(self, size=5):
        self._size = size
        self.buff = [None for _ in xrange(self._size)]
        self.readPtr = None
        self.writePtr = 0

    def push_back(self, val):
        self.buff[self.writePtr] = val
        if self.readPtr is None:
            self.readPtr = self.writePtr
        elif self.writePtr == self.readPtr:
            self.readPtr = (self.readPtr + 1) % self._size
        self.writePtr = (self.writePtr + 1) % self._size

    def pop_front(self):
        if self.readPtr is None:
            return None
        tmp = self.buff[self.readPtr]
        if not tmp is None:
            self.buff[self.readPtr] = None
            self.readPtr = (self.readPtr + 1) % self._size
        return tmp

    def get(self):
        return self.buff[self.readPtr]


"""
size = 12
buff = BuffList(size)
print buff.buff

for i in xrange(7):
    buff.push_back(i)
    print buff.buff, buff.readPtr, buff.writePtr

for i in xrange(3):
    buff.pop_front()
    print buff.buff, buff.readPtr, buff.writePtr

for i in xrange(7):
    buff.push_back(i)
    print buff.buff, buff.readPtr, buff.writePtr

for i in xrange(3):
    buff.pop_front()
    print buff.buff, buff.readPtr, buff.writePtr
"""
