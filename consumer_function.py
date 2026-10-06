import generic_functions

result1 = generic_functions.add(10, 5)
result2 = generic_functions.div(10, 5)

print("Addition:", result1)
print("Division:", result2)

from generic_functions import add, div

result1 = add(10, 5)
result2 = div(10, 5)

print("Addition:", result1)
print("Division:", result2)

import generic_functions as gf

result1 = gf.add(20, 10)
result2 = gf.div(20, 10)

print("Addition:", result1)
print("Division:", result2)

from generic_functions import add as addition
from generic_functions import div as division

result1 = addition(20, 10)
result2 = division(20, 10)

print("Addition:", result1)
print("Division:", result2)