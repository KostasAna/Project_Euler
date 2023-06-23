from Project_Euler import *
from large_inputs import *

# https://projecteuler.net/problem=1   233168
print(f'The sum of all the numbers up to 1000 divisible by 3 and 5 is {sum_div(range(1000), 3, 5)}.')

# https://projecteuler.net/problem=2   4613732
print(f'The sum of the even-valued Fibonacci numbers smaller than 4 million is {sum_div(fibonacci_numbers(lambda x: x < 4 * 10 ** 6), 2)}.')

# https://projecteuler.net/problem=3   6857
print(f'The largest prime factor of 600851475143 is {prime_factors(600851475143)[-1]}.')

# https://projecteuler.net/problem=4   906609
print(f'The largest palindromic number made from the product of two 3-digit numbers is {max_pal_num(100, 999)}.')

# https://projecteuler.net/problem=5   232792560
print(f'The smallest positive number that is evenly divisible by all of the numbers up to 20 is {div_mul(20)}.')

# https://projecteuler.net/problem=6   25164150
print(f'The square of the sums minus the sum of squares up to 100 is {sum_sum(100)}.')

# https://projecteuler.net/problem=7   104743
print(f'The 10001st prime is {primes(10001)[-1]}.')

# https://projecteuler.net/problem=8   23514624000
print(f'The greatest product of 13 adjacent digits from this large number is {max(seq_prod(p8, 13).values())}.')

# https://projecteuler.net/problem=9   31875000
print(f'The product of a Pythagorean triplet, which add up to 1000, is {a * b * c}.')

# https://projecteuler.net/problem=10   142913828922
print(f'The sum of all primes below 2 million is {primes_sum(2 * 10 ** 6)}.')

# https://projecteuler.net/problem=11   70600674
print(f'The greatest product of 4 adjacent numbers in this grid is {products(list(listing(p11)), 4)}.')

# https://projecteuler.net/problem=12   76576500
print(f'The first triangle number to have over five hundred divisors is {max_primes(500, lambda x: sum(range(x+1)))}.')

# https://projecteuler.net/problem=13   5537376230
print(f'The first ten digits of the sum of these numbers are {first_digits(sum(int(i) for i in p13), 10)}.')

# https://projecteuler.net/problem=14   837799
print(f'The number, under 1 million, that produces the longest Collatz sequence is {max_len(collatz, 10 ** 6)}.')

# https://projecteuler.net/problem=15   137846528820
print(f'From top left to right bottom, there are exactly {max(pascal_triangle(40))} routes.')

# https://projecteuler.net/problem=16   1366
print(f'The sum of the digits of the number 2^1000 is {count_length(2**1000)}.')

# https://projecteuler.net/problem=17   21124
print(f'There are {sum(len(letters(i)) for i in range(1, 1001))} letters used to write all the numbers from 1 to 1000.')

# https://projecteuler.net/problem=18   1074
print(f'The maximum total from top to bottom of this triangle is {max_paths(list(listing(p18)))[0]}.')

# https://projecteuler.net/problem=20   648
print(f'The sum of the digits in the number 100! is {count_length(factorial(100))}.')

# https://projecteuler.net/problem=21   31626
print(f'The sum of all the amicable numbers under 10000 is {sum(amicable_numbers(10000))}.')

# https://projecteuler.net/problem=25   4782
print(f'the index of the first term in the Fibonacci sequence to contain 1000 digits is {len(fibonacci_numbers(lambda x: len(str(x)) < 1000))}.')

# https://projecteuler.net/problem=67   7273
print(f'The maximum total from top to bottom of this triangle is {max_paths(list(listing(p67)))[0]}.')