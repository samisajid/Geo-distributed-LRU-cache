from collections import deque
import sys
import time

class LRUcache(object):
    def __init__(self,cachesize,timeout=10,valuemap={},timemap={},clist=deque()):
        self.cachesize=cachesize
        self.timeout=timeout
        self.valuemap=valuemap
        self.timemap=timemap
        self.clist=clist
    def append(self,x,y):
        if x not in self.timemap:
            while (sys.getsizeof(self.valuemap)+sys.getsizeof(y))>self.cachesize:
                if self.clist==deque() and (sys.getsizeof(self.clist)+sys.getsizeof(x))>self.cachesize:
                    print("The data is bigger than the cache size, compress or divide the data")
                    return
                else:
                    last=self.clist.pop()                    
                    del self.timemap[last]
                    del self.valuemap[last]
                
        else:
            self.clist.remove(x)
        self.valuemap[x]=y
        self.clist.appendleft(x)
        self.timemap[x]=time.time()
        self.expire()
    def get(self,x):
        if x in self.timemap:
            print("cache hit")
            return self.valuemap[x]
        else:
            print("Cache miss")
            print("The program will not deal with this issue for now, we send you 'None'")
            return
    def expire(self):
        try:
            while time.time()>(self.timemap[self.clist[-1]]+self.timeout):
                out=self.clist.pop()
                del self.timemap[out]
                del self.valuemap[out]
        except IndexError:
            pass
            
