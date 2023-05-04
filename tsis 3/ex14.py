import math
import random
from functions_1 import grams_to_ounces,f_to_c,solve,filter_prime
from functions_1 import permute,reverse_sentence ,sol,has_33,vol,unique_list
from functions_1 import is_palindrom,histogram,ex14,has_007

grams_to_ounces(100)
f_to_c(100)
solve(35,94)
n = [1,2,3,4,5,6,7,8,9,10,11]
n1 = filter_prime(n)
print(*n1)
string = "KBTU"
permute(list(string),0,len(string))
words = "TSIS3 PP2"
print(''.join(sol(list(words),len(words))))
print(has_33([3,3]))
print(has_33([1,2,3]))
print(has_007([0,0,7]))
print(has_007([0,0,0]))
print(vol(3))
print(unique_list([1,1,1,0]))
print(is_palindrom("qwerty"))
print(is_palindrom("qweewq"))
histogram([1,3,5,])
ex14()
