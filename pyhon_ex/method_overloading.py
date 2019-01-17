

class Overloading:
    def sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None:
           return  a+b+c
        elif a!=None and b!=None:
            return  a+b
        else:
            return  a

result = Overloading()



print(result.sum())
