import ctypes

class myList:
    def __init__(self):
        self.size=1
        self.n=0
        #create a c type array with size=self.size
        self.A=self.__makeArray(self.size)
    
    def __len__(self):
        return self.n

    def __makeArray(self,capacity):
        #creates a ctype static refrential array with size capacity
        return (capacity*ctypes.py_object)()
    

L=myList()
print(L,type(L))
print(len(L))
    