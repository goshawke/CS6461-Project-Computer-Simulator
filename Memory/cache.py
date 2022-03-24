
from Memory.memory import *

class CacheLine:
    def __init__(self, tag = '', value = ''):
        self.tag = tag
        self.value = value

class Cache:
    def __init__(self, size = 16):
        self.size = size
        self.cache_content = []
        self.mem = Memory()
        self.msg = ''

    def reset(self):
        self.cache_content = []
        self.mem = Memory()
        self.msg = ''

    def find(self, add : int):
        """This function checks if tag is in the chache"""
        for line in self.cache_content:
            if line.tag == add:
                return True
        return False

    def __push(self, line : CacheLine):
        """This function push new cache line into Cache
        it obeys FIFO
        """
        if len(self.cache_content) == self.size:
            self.cache_content.pop(0)
        self.cache_content.append(line)

    def get(self, add : int):
        """This function looks for tag in cache.
        Return value from cache if tag exists,
        push new line into cache and retrun from memory if it doesn't
        """
        for line in self.cache_content:
            if line.tag == add:
                self.msg = 'Cache[tag='+str(add)+'] :\t\t\t'+str(int(line.value))+'\n'
                return line.value
        value = self.mem.get_from_memory(add)
        self.msg = 'MEM[' + str(add) + '] :\t\t\t' + str(int(value)) + '\n\n'
        new_line = CacheLine(add, value)
        self.__push(new_line)
        self.msg += 'Not in Cache, push into Cache\n\n'
        return value

    def set(self, add : int, value : str):
        """This function looks for tag in cache.
        set both memory and cache if tag exists,
        set memory and push the line into cache if it doesn't
        """
        for line in self.cache_content:
            if line.tag == add:
                line.value = value
                self.msg = 'Update Cache[tag=' + str(add) + ']\n'
                self.mem.set_to_memory(add, value)
                self.msg += 'MEM['+str(add)+'] :\t\t\t'+str(int(value))+'\n\n'
                return
        new_line = CacheLine(add, value)
        self.__push(new_line)
        self.msg = 'Not in Cache, push into Cache\n'
        self.mem.set_to_memory(add, value)
        self.msg += 'MEM['+str(add)+'] :\t\t\t'+str(int(value))+'\n\n'

    def print_out(self):
        word = '\n-------------CACHE---------------\n'
        for line in self.cache_content:
            word += str(line.tag) + ':\t' + str(int(line.value)) + '\n'
        return word
