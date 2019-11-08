from collections import deque
import sys
import time

class LRUcache(object):
    def __init__(self,cachesize,timeout=100,timemap={},clist=deque()):
        self.cachesize=cachesize
        self.timeout=timeout
        self.timemap=timemap
        self.clist=clist
    def append(self,x):
        if x not in self.timemap:
            while (sys.getsizeof(self.clist)+sys.getsizeof(x))>self.cachesize:
                if self.clist==deque() and (sys.getsizeof(self.clist)+sys.getsizeof(x))>self.cachesize:
                    print("The data is bigger than the cache size, compress or divide the data")
                    return
                else:
                    last=self.clist.pop()
                    del self.timemap[last]
                
        else:
            self.clist.remove(x)
        self.clist.appendleft(x)
        self.timemap[x]=time.time()
        self.expire()
    def expire(self):
        try:
            while time.time()>(self.timemap[self.clist[-1]]+self.timeout):
                out=self.clist.pop()
                del self.timemap[out]
        except IndexError:
            pass
            
