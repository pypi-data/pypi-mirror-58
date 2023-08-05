class A:
    no_objects = 0
    def __init__(self,myname):        
        print('Contructor Initiated')
        self.myname = myname
        A.no_objects += 1
    def test(self):
        print(self.myname)

class B(A):
    def __init__(self,bname):
        self.bname = bname
    def test(self):
        print(self.bname)