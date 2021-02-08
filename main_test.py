from Project_Euler import *

# https://projecteuler.net/problem=1   233168
print(f'The sum of all the numbers up to 1000 divisible by 3 and 5 is {sum_div_3_5(1000):d}.')

# https://projecteuler.net/problem=2   4613732
print(f'The sum of the even-valued Fibonacci numbers smaller than 4 million is {fib_even_sum(4*10**6):d}.')

# https://projecteuler.net/problem=3   6857
print(f'The largest prime factor of 600851475143 is {prime_factors(600851475143)[-1]:d}.')

# https://projecteuler.net/problem=4   906609
print(f'The largest palindromic number made from the product of two 3-digit numbers is {max_pal_num(100, 999):d}.')

# https://projecteuler.net/problem=5   232792560
print(f'The smallest positive number that is evenly divisible by all of the numbers up to 20 is {div_mul(20):d}.')

# https://projecteuler.net/problem=6   25164150
print(f'The square of the sums minus the sum of squares up to 100 is {sum_sum(100)}.')

# https://projecteuler.net/problem=7   104743
print(f'The 10001st prime is {primes(10001)[-1]}.')  # Slow
