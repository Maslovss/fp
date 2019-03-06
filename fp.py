


from functools import partial
from functools import reduce

class fp:
    def __init__(self , l ):
        self.mylist = l
        
    def map(self , f):
        return fp( list(map(f , self.mylist)))
        
    def filter( self , f):
        return fp( list(filter(f , self.mylist)))
        
    def reduce(self , f ):
        return reduce( f , self.mylist)
        
    def show(self):
        for i in self.mylist:
            print(i)
      
            
