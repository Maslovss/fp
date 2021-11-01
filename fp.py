from functools import reduce

class fp:
    def __init__(self , l ):
        self.mylist = l
        
    def __iter__(self):
         return iter(self.mylist)
        
    def map(self , f):
        return fp( list(map(f , self.mylist)))
        
    def filter( self , f):
        return fp( list(filter(f , self.mylist)))
        
    def reduce(self , f ):
        return reduce( f , self.mylist)
    
    def distinct(self):
        self.mylist = list(set(self.mylist))
        return fp( self.mylist)

    def sort(self, key=None, reverse=False):
        return fp( sorted( self.mylist , key = key , reverse = reverse))

    def show(self):
        for i in self.mylist:
            print(i)
            
