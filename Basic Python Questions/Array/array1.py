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
    def append(self,item):
        if self.n==self.size:
            #resize
            self.__resize(self.size*2)

        #append
        self.A[self.n]=item
        self.n+=1
    
    def __resize(self,new_cap):
        #new array with new capacity
        B = self.__makeArray(new_cap)
        self.size=new_cap

        #copy A to B
        for i in range(self.n):
            B[i]=self.A[i]
        
        #reasssign A
        self.A=B
        



    

L=myList()
#print(L,type(L))
#print(len(L))

L2=[10,20,30]
L2.append("Hi")
print(L2)
    