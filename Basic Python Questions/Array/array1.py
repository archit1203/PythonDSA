import ctypes

class myList:
    def __init__(self):
        self.size=1
        self.n=0
        #create a c type array with size=self.size
        self.A=self.__makeArray(self.size)
    
    #LENGTH OF LIST
    def __len__(self):
        return self.n

    #CREATE LIST
    def __makeArray(self,capacity):
        #creates a ctype static refrential array with size capacity
        return (capacity*ctypes.py_object)()
    
    #APPEND LIST

    

L=myList()
#print(L,type(L))
#print(len(L))

L2=[10,20,30]
L2.append("Hi")
print(L2)
    