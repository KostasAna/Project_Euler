from Project_Euler import *

# https://projecteuler.net/problem=1
print(f'The sum of all the numbers up to 1000 divisible by 3 and 5 is {sum_div_3_5(1000):d}.')

# https://projecteuler.net/problem=2
print(f'The sum of the even-valued Fibonacci numbers smaller than 4 million is {fib_even_sum(35):d}.')
# could choose other number instead of 35 as long as the loop reaches 4 million

# https://projecteuler.net/problem=3
print(f'The largest prime factor of 600851475143 is {prime_factors(600851475143)[-1]:d}.')

# https://projecteuler.net/problem=4
print(f'The largest palindromic number made from the product of two 3-digit numbers is {max_pal_num(100, 999):d}.')

# https://projecteuler.net/problem=5
print(f'The smallest positive number that is evenly divisible by all of the numbers up to 20 is {div_mul(20):d}.')
