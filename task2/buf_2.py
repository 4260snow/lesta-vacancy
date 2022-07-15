""" Буфер FIFO на array """
from array import *


class BuffArr:
    def __init__(self, typecode='i', size=10):
        self._type = typecode
        self._size = size
        self.buff = array(self._type, [0 for _ in xrange(self._size)])
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
        tmp = self.buff[self.readPtr]
        self.buff[self.readPtr] = 0
        self.readPtr = (self.readPtr + 1) % self._size
        return tmp

    def get(self):
        return self.buff[self.readPtr]


"""
buff = BuffArr('i', 5);
buff.push_back(1)
print buff.buff

for i in xrange(7):
    buff.push_back(i)
    print buff.buff, buff.readPtr, buff.writePtr

print

for i in xrange(3):
    buff.pop_front()
    print buff.buff, buff.readPtr, buff.writePtr

print

for i in xrange(7):
    buff.push_back(i)
    print buff.buff, buff.readPtr, buff.writePtr

print

for i in xrange(3):
    buff.pop_front()
    print buff.buff, buff.readPtr, buff.writePtr

print buff.get()
"""