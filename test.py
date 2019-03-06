
from fp import *


        
        
def myinc( x ):
    return x + 1 
    
def myadd( x , y ):
    return x + y 

def mymul( x , y ):
    return x * y

    




test_fp = fp( list(range(20)))

print( test_fp.map( partial(myadd,10  ) ) \
              .filter( lambda x: x % 2 == 0 ) \
              .reduce( lambda x, y: x + y) \
       )

print('Sample 1')

test_fp.map(partial(mymul,2 )) \
       .map(partial(myadd,3 )) \
       .filter( lambda x: x % 3 == 0 ) \
       .show()

assert fp([1, 2, 3]).reduce( lambda x, y: x + y) == 6
assert fp([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).filter( lambda x: x % 2 == 0 ).reduce( lambda x, y: x + y) == 30




