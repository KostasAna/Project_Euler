"""Print answers."""
import math
import project_euler
import large_inputs


# https://projecteuler.net/problem=1   233168
print(f'The sum of all the numbers up to 1000 divisible by 3 and 5 is {project_euler.sum_div(range(1000), 3, 5)}.')

# https://projecteuler.net/problem=2   4613732
print(f'The sum of the even-valued Fibonacci numbers smaller than 4 million is {project_euler.sum_div(project_euler.fibonacci_numbers(lambda x: x < 4 * 10 ** 6), 2)}.')

# https://projecteuler.net/problem=3   6857
print(f'The largest prime factor of 600851475143 is {project_euler.prime_factors(600851475143)[-1]}.')

# https://projecteuler.net/problem=4   906609
print(f'The largest palindromic number made from the product of two 3-digit numbers is {project_euler.max_pal_num(100, 999)}.')

# https://projecteuler.net/problem=5   232792560
print(f'The smallest positive number that is evenly divisible by all of the numbers up to 20 is {project_euler.div_mul(20)}.')

# https://projecteuler.net/problem=6   25164150
print(f'The square of the sums minus the sum of squares up to 100 is {project_euler.sum_sum(100)}.')

# https://projecteuler.net/problem=7   104743
print(f'The 10001st prime is {project_euler.primes(10001)[-1]}.')

# https://projecteuler.net/problem=8   23514624000
print(f'The greatest product of 13 adjacent digits from this large number is {max(project_euler.seq_prod(large_inputs.P8, 13).values())}.')

# https://projecteuler.net/problem=9   31875000
print(f'The product of a Pythagorean triplet, which add up to 1000, is {project_euler.a * project_euler.b * project_euler.c}.')

# https://projecteuler.net/problem=10   142913828922
print(f'The sum of all primes below 2 million is {project_euler.primes_sum(2 * 10 ** 6)}.')

# https://projecteuler.net/problem=11   70600674
print(f'The greatest product of 4 adjacent numbers in this grid is {project_euler.products(list(project_euler.listing(large_inputs.P11)), 4)}.')

# https://projecteuler.net/problem=12   76576500
print(f'The first triangle number to have over five hundred divisors is {project_euler.max_primes(500, lambda x: sum(range(x+1)))}.')

# https://projecteuler.net/problem=13   5537376230
print(f'The first ten digits of the sum of these numbers are {project_euler.first_digits(sum(int(i) for i in large_inputs.P13), 10)}.')

# https://projecteuler.net/problem=14   837799
print(f'The number, under 1 million, that produces the longest Collatz sequence is {project_euler.greatest_length(project_euler.collatz_seq(10 ** 6))}.')

# https://projecteuler.net/problem=15   137846528820
print(f'From top left to right bottom, there are exactly {max(project_euler.pascal_triangle(40))} routes.')

# https://projecteuler.net/problem=16   1366
print(f'The sum of the digits of the number 2^1000 is {project_euler.count_length(2**1000)}.')

# https://projecteuler.net/problem=17   21124
print(f'There are {sum(len(project_euler.letters(i)) for i in range(1, 1001))} letters used to write all the numbers from 1 to 1000.')

# https://projecteuler.net/problem=18   1074
print(f'The maximum total from top to bottom of this triangle is {project_euler.max_paths(list(project_euler.listing(large_inputs.P18)))[0]}.')

# https://projecteuler.net/problem=19   171
print(f'There are {project_euler.count_days((1901, 1, 1), (2000, 12, 31))} Sundays that fall on the first of the month during the twentieth century.')

# https://projecteuler.net/problem=20   648
print(f'The sum of the digits in the number 100! is {project_euler.count_length(math.factorial(100))}.')

# https://projecteuler.net/problem=21   31626
print(f'The sum of all the amicable numbers under 10000 is {sum(project_euler.amicable_numbers(10000))}.')

# https://projecteuler.net/problem=22   871198282
print(f'The total score of all names in the names text file is {sum(project_euler.sort_n_count(large_inputs.P22).values())}.')

# https://projecteuler.net/problem=23   4179871
print(f'The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {project_euler.non_abundant_sums(28123)}.')

# https://projecteuler.net/problem=24   2783915460
print(f'The millionth lexicographic permutation of the digits 0 to 9 is {project_euler.nth_permutation(list(range(10)), 10 ** 6)}.')

# https://projecteuler.net/problem=25   4782
print(f'The index of the first term in the Fibonacci sequence to contain 1000 digits is {len(project_euler.fibonacci_numbers(lambda x: len(str(x)) < 1000))}.')

# https://projecteuler.net/problem=26   983
print(f'The number under 1000 which contains the longest recurring cycle in its decimal unit fraction part is {max(i for i in range(1000) if project_euler.reptend_check(i))}.')

# https://projecteuler.net/problem=27   -59231
print(f'The product of the coefficients for the quadratic expression that produces the maximum number of primes for consecutive values is {math.prod(project_euler.quadratic_prime_sequence(1000))}.')

# https://projecteuler.net/problem=67   7273
print(f'The maximum total from top to bottom of this triangle is {project_euler.max_paths(list(project_euler.listing(large_inputs.P67)))[0]}.')
