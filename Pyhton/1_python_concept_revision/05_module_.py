"""
.py is module -> can be built in or user defined

How to Import Modules : 

1st Method : Imports all the fxn/variables in the Module
 - import module_name

2nd Method : For importing just few fxns /Variables
 - from module_name import fxn1, fxn2 fxn3

"""


import math
num = 16
square_root = math.sqrt(num)
print(f"Square Root of {num} is {square_root}\n\n\n\n\n\n\n")


from random import randint
# threw a die
random_val = randint(1,6)
print(random_val)

# import as Alias
from datetime import date as dt
print(f"Today Date is :{dt(2008,9,1)}")