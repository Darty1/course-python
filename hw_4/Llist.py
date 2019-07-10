
from typing import Any, Union, Optional, Iterable

class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self, begin, end, length):
        self.begin = Node(None)
        self.end = None
        self.length = 0
    def __iter__(self):
        current = self.begin.next
        if current:
            yield current.value
            current = current.next

    def __getitem__(self, key):
        length = 0
        current = None
        if self.begin != None:
            current = self.begin
            while key!=length or current.next != None:
                current = current.next
                length +=1
            if key==length:current=current.value
        return current

    def __setitem__(self, key, value):
        if self.begin != None:
            current = self.begin
            val = self.value
        while current !=

    def __len__(self):
        self.length = 1
        if self.first != None:
            current = self.begin
            while current.next != None:
                current = current.next
                self.length += 1
            return self.length

    def index(item: Any):

    def insert(self, index, item):
        if self.begin == None:
            self.begin = Node(item, self.begin)
            self.end = self.begin.next
            return
        if index == 0:
            self.begin = Node(item, self.begin)
            return
        if index > self.__len__(self):
            print('ValueError')
        elif index < 0:
            index = self.__len__ + index
        current = self.begin
        count = 0
        while current != None:
            if count == index - 1:
                current.next = Node(item, current.next)
                if current.next.next == None:
                    self.end = current.next
                break
            current = current.next

    def append(self, item):
        if self.begin == None:
            self.begin = Node(item, None)
            self.end = self.begin
        elif self.end == self.begin:
            self.end = Node(item, None)
            self.begin.next = self.end
        else:
            current = Node(item, None)
            self.end.next = current
            self.end = current

    def pop(self, index: int = -1):
        if (self.begin == None):
            return
        old = current = self.begin
        count = 0
        if index == 0:
            self.begin = self.begin.next
            return
        while current != None:
            if count == index:
                if current.next == self.end:
                    self.end = current
                    break
                else:
                    old.next = current.next
                break
            old = current
            current = current.next
            count += 1

    def remove(item: Any):

class Iterator(object):

     def __iter__(self):
         return self

     def __next__(self):