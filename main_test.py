from Project_Euler import *
from large_inputs import *

# https://projecteuler.net/problem=1   233168
print(f'The sum of all the numbers up to 1000 divisible by 3 and 5 is {sum_div(1000, 3, 5):d}.')

# https://projecteuler.net/problem=2   4613732
print(f'The sum of the even-valued Fibonacci numbers smaller than 4 million is {fib_even_sum(4 * 10 ** 6):d}.')

# https://projecteuler.net/problem=3   6857
print(f'The largest prime factor of 600851475143 is {prime_factors(600851475143)[-1]:d}.')

# https://projecteuler.net/problem=4   906609
print(f'The largest palindromic number made from the product of two 3-digit numbers is {max_pal_num(100, 999):d}.')

# https://projecteuler.net/problem=5   232792560
print(f'The smallest positive number that is evenly divisible by all of the numbers up to 20 is {div_mul(20):d}.')

# https://projecteuler.net/problem=6   25164150
print(f'The square of the sums minus the sum of squares up to 100 is {sum_sum(100)}.')

# https://projecteuler.net/problem=7   104743
print(f'The 10001st prime is {primes(10002)[-1]}.')

# https://projecteuler.net/problem=8   23514624000
print(f'The greatest product of 13 adjacent digits from this large number is {max(seq_prod(p8, 13).values()):d}.')

# https://projecteuler.net/problem=9   31875000
print(f'The product of a Pythagorean triplet, which add up to 1000, is {a * b * c}.')

# https://projecteuler.net/problem=10   142913828922   It takes about 10 seconds
print(f'The sum of all primes below 2 million is {primes_sum(2 * 10 ** 6)}.')

# https://projecteuler.net/problem=11   70600674
print(f'The greatest product of 4 adjacent numbers in this grid is {products(listing(p11), 4)}.')

# https://projecteuler.net/problem=12   76576500
print(f'The first triangle number to have over five hundred divisors is {max_primes(500, lambda x: sum(range(x+1)))}.')

# https://projecteuler.net/problem=13   5537376230
print(f'The first ten digits of the sum of these numbers are {first_digits(sum(int(i) for i in p13), 10)}.')
