"""Module for all the functions needed."""
import time
import math
import datetime


def timer(function):
    """This decorator is used to check how long it takes a function to run."""

    def wrapper(*args, **kwargs):
        time_start = time.time()
        outcome = function(*args, **kwargs)
        total_time = time.time() - time_start
        print(f'Total time needed: {total_time:f}')
        return outcome

    return wrapper


# https://projecteuler.net/problem=1


def sum_div(numbers: range, *args: int) -> int:
    """This function takes all the numbers up to provided
    that are divisible by *args and it adds them up."""

    return sum(num for num in numbers if any(num % i == 0 for i in args))


# https://projecteuler.net/problem=2


def fibonacci_numbers(limit: bool) -> list:
    """This function produces all Fibonacci numbers
    up to the limit specified for the last term."""

    i, fibs = 0, [1, 1]  # to start the Fibonacci series

    while limit(fibs[i + 1]):
        i += 1
        fibs.append(fibs[i] + fibs[i - 1])

    return fibs


# https://projecteuler.net/problem=3


def prime_factors(number: int) -> list:
    """This function lists all the prime factors of the number.
    If it is prime it returns only itself."""

    p_factors = []

    for i in range(2, round(number ** 0.5 + 1)):
        while number % i == 0:
            p_factors.append(i)
            number = number / i
        if number == 1:
            break

    if number != 1:  # in case it is prime
        p_factors.append(number)

    return p_factors


# https://projecteuler.net/problem=4


def max_pal_num(min_n: int, max_n: int) -> int:
    """This function takes a range of values (min_n, max_n) in which it finds
    the largest palindromic number of all the products in that range."""

    return max(i * j for j in range(min_n, max_n) for i in range(min_n, max_n)
               if str(i * j) == str(i * j)[::-1])


# https://projecteuler.net/problem=5


def div_mul(number: int) -> int:
    """This function finds the smallest positive number that
    is evenly divisible by all of the numbers up to certain number."""

    product = 1

    for num in range(2, number):
        if product % num != 0:
            product *= prime_factors(num)[-1]  # function from problem 3

    return product


# https://projecteuler.net/problem=6


def sum_sum(numbers: int) -> int:
    """This function calculates the difference between the sum of the squares
    of the first natural specified numbers and the square of the sum."""

    return sum(i for i in range(numbers + 1)) **2 - sum(i**2
            for i in range(numbers + 1))


# https://projecteuler.net/problem=7


def prime_check(number: int) -> int:
    """This function returns True if the number is prime & False otherwise."""

    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, round(number ** 0.5 + 1)):
        if number % i == 0:
            return False

    return True


def primes(max_prime: int) -> list:
    """This function lists the first primes up to a certain number."""

    p_list = [2]  # the first prime is 2
    i = 2

    while len(p_list) < max_prime:
        i += 1
        if prime_check(i):
            p_list.append(i)

    return p_list


# https://projecteuler.net/problem=8


def seq_prod(large_number: str, adj: int):
    """This function takes all the adjacent digits specified of
    a number and returns a dictionary with its products."""

    large_number = int(large_number.replace("\n", ""))
    adj_digits = []  # all the adjacent numbers
    adj_products = []  # and their products

    if len(str(large_number)) <= adj:  # pointless in that case
        return {'None': 0}

    for digit in range(len(str(large_number)) - adj + 1):
        adj_digits.append(str(large_number)[digit: digit + adj])

    for adjacent in adj_digits:
        adj_products.append(math.prod(int(i) for i in str(adjacent)))
    adjacents_product = dict(zip(adj_digits, adj_products))

    return adjacents_product


# https://projecteuler.net/problem=9


# This problem requires some maths beforehand. Constraints:
# (1) 0 < a < b < c ,  (2) a + b + c = 1000 ,  (3) a^2 + b^2 = c^2
# (2) & (3) => a^2 + b^2 = 10^6 + a^2 + b^2 - 2000*a -2000*b + 2*a*b
# <=> 0 = 5*10^5 - 1000(a + b) + ab <=> 0 = 5*10^5 + a(b - 1000) - 1000*b
# <=> 0 = a(b - 1000) - 1000(b - 500) <=> 5*10^5 = (b - 1000)(a - 1000) (4)
# (1) & (4) => 0 < a < b < 500 <=> -1000 < a - 1000 < b - 1000 < -500
# At this point is quite fast and easy to do an exhaustive search.

for fives in range(505, 1000, 5):
    for teners in range(1000, 500, -10):
        if fives * teners == 5 * 10 ** 5:
            a = 1000 - fives
            b = 1000 - teners
            c = 1000 - a - b


# https://projecteuler.net/problem=10


def primes_sum(number: int) -> int:
    """This function adds all the primes below a certain number."""

    nums = list(range(2,  number + 1))
    for num in nums[:round(number ** 0.5 + 1)]:
        if prime_check(num):  # function from problem 7
            nums = [i for i in nums if i == num or i % num != 0]
        else:
            continue

    return sum(nums)


# https://projecteuler.net/problem=11


def listing(matrix: str) -> list:
    """This function takes a matrix in string type and returns it as a list of
    lists. It can be used also for triangles formats (problems 18 and 67)."""

    big_list = matrix.split('\n')

    for line in big_list:
        row = line.split(' ')
        row = [int(number) for number in row]
        yield row


def products(rows: list, adj: int) -> int:
    """This funcion takes a matrix and returns the greatest product
    of specified adjacent numbers in any direction."""

    alln = []

    for i in range(len(rows)):
        for j in range(0, len(rows[0])-adj+1):
            alln.append(math.prod(rows[i][j + k] for k in range(adj)))
            alln.append(math.prod(rows[j + k][i] for k in range(adj)))

            if i <= (len(rows) - adj):  # diagonals
                alln.append(math.prod(rows[i + k][j + k] for k in range(adj)))
                alln.append(math.prod(rows[i + k][j + adj - k - 1]
                    for k in range(adj))) # right top to left bottom (weirdly)

    return max(alln)


# https://projecteuler.net/problem=12


def divisors(number: int) -> int:
    """This function returns the list of all the factors of a number."""

    divs = [i for i in range(1, int(round(number ** 0.5 + 1, 0)))
            if number % i == 0]
    divs = divs + [int(number / d) for d in divs[::-1] if number % d == 0]

    return sorted(set(divs)) # for perfect squares, remove duplicate root

def max_primes(divs: int, func: callable) -> int:
    """This function takes as inputs a number and a function/sequence and
    returns the first number of the sequence with that many divisors."""

    i = 1
    while True:
        i += 1
        divs_list = divisors(func(i))
        if len(divs_list) > divs:
            break

    return func(i)


# https://projecteuler.net/problem=13


def first_digits(num: int, dig: int) -> int:
    """This function returns the first specified digits of a number."""

    return math.floor(num / (10 ** math.floor((math.log10(num)) + 1 - dig)))


# https://projecteuler.net/problem=14


def collatz_seq(limit: int) -> dict:
    """This function produces all Collatz sequences for all numbers up to
    a certain limit. Each sequence is stored as a list in a dictionary."""

    collatzs = {}

    for number in range(2, limit):
        collatzs[number] = [number]
        num = number
        while collatzs[number][-1] > 1:
            if collatzs[number][-1] in collatzs and len(collatzs[number]) > 1:
                collatzs[number] = collatzs[number] + collatzs[num]
                break # to avoid recalculating a known subsequence
            num = int(num / 2) if num % 2 == 0 else 3 * num + 1
            collatzs[number].append(num)
        collatzs[number].pop(0)

    return collatzs


def greatest_length(inputs: dict) -> int:
    """This function finds which number produces the longest sequence."""

    outputs = {key: len(value) for key, value in inputs.items()}

    return max(outputs, key=outputs.get)


# https://projecteuler.net/problem=15


# The straight forward solution to this problem is 40 choose 20 derived by
# counting binomial coefficients. However, I figured it out using the Pascal's
# triangle so I'm coding this method instead. We have 2-dimensional grid, with
# side of length 20. Therefore we want the largest coefficient of 2*20 Pascal's
# triangle which counts all the paths to reach from the top left corner of the
# square (top of triangle) to the bottom right one (bottom-middle of triangle).


def pascal_triangle(power: int):
    """This function returns a list of the coefficients
    for a specific power using the Pascal's triangle"""

    coef = [1] # (a + b) ** 0

    for _ in range(power):
        left, right = [0] + coef, coef + [0]
        coef = [x + y for x, y in zip(left, right)]

    return coef


# https://projecteuler.net/problem=16


def count_length(number):
    """This function calculates the sum of the digits of a number."""

    return sum(int(n) for n in str(number))


# https://projecteuler.net/problem=17


def letters(number):
    """This function prints how a number is written"""

    ones = ['', 'One', 'Two', 'Three', 'Four',
        'Five', 'Six', 'Seven', 'Eight','Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
        'Fifteen', 'Sixteen', 'Seventeen','Eighteen','Nineteen']
    tens = ['', teens, 'Twenty', 'Thirty', 'Forty',
        'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    thousands = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

    grouped = []
    while True:
        remain, number = divmod(number, 1000)
        grouped.append(number)
        number = remain
        if len(str(remain)) <= 3:
            if remain != 0:
                grouped.append(remain)
            break

    word = ''
    for nth, number in enumerate(grouped[::-1]):
        third, number = divmod(number, 100)
        if third > 0:
            word += ones[third] + 'Hundred'
        second, number = divmod(number, 10)
        if (second != 0 or number != 0) and third > 0:
            word += 'and'
        if second != 1:
            word += tens[second] + ones[number]
        else:
            word += tens[second][number]
        word += thousands[len(grouped) - nth - 1]

    return word


# https://projecteuler.net/problem=18


def max_paths(routes: list) -> list:
    """This funcion takes a matrix and returns
    the maximum total from top to bottom"""

    for i, row in enumerate(routes[:0:-1]):
        for j, _ in enumerate(row[:-1]):
            routes[-i-2][j] = max(row[j] + routes[-i-2][j],
                                  row[j+1] + routes[-i-2][j])

    return routes[0]


# https://projecteuler.net/problem=19


def count_days(start_date: tuple, end_date: tuple) -> int:
    """This function counts how many Sundays fall on the first of the month
    for a given period of time. The input start and end dates should be in
    the format accepted by datetime (yyyy, mm, dd)."""

    start, end = datetime.date(*start_date), datetime.date(*end_date)
    dtime = datetime.timedelta(days = 1)

    days = 0
    while start <= end:
        if start.day == 1 and start.weekday() == 6 :
            days += 1
        start += dtime

    return days


# https://projecteuler.net/problem=20


# Use function from problem 16 and the built-in factorial one.


# https://projecteuler.net/problem=21


def amicable_numbers(number: int) -> dict:
    """This functions finds all amicable numbers up to a number.
    They are presented in a dictionary format as a form of proof"""

    divs_sum = {n : sum(divisors(n)[:-1]) for n in range(1, number) if
                    len(divisors(n)) > 2} # get rid of n itself and all primes

    amicables = {key: value for key, value in divs_sum.items() if key in
                divs_sum.values() and value in divs_sum and divs_sum[value] ==
                key and key != value} # to exlude all perfect numbers

    return amicables


# https://projecteuler.net/problem=22


def sort_n_count(names: list) -> dict:
    """This function sorts names in alphabetical order and it calculates their
    scores (alphabetical position times the sum of alphabetical values)"""

    names = sorted(names)
    scores = {n: (names.index(n) + 1) * sum(ord(l.lower()) - 96
                for l in n) for n in names}

    return scores


# https://projecteuler.net/problem=23


def non_abundant_sums(limit: int) -> dict:
    """This function calculates the sum of all numbers up
    to a limit that are not a sum of 2 abundant numbers."""

    abundants = set(n for n in range(1, limit) if sum(divisors(n)[:-1]) > n)

    return sum(num for num in range(1, limit) if not any(num - abuns
                in abundants for abuns in abundants))


# https://projecteuler.net/problem=25


# We can just use the function from problem 2.


if __name__ == "__main__":

    import large_inputs
    print(
          sum_div(range(1000), 3, 5), #1
          sum_div(fibonacci_numbers(lambda x: x < 4 * 10 ** 6), 2), #2
          prime_factors(600851475143)[-1], #3
          max_pal_num(100, 999), #4
          div_mul(20), #5
          sum_sum(10000), #6
          primes(10001)[-1], #7
          max(seq_prod(large_inputs.P8, 13).values()), #8
          a * b * c, #9
          primes_sum(2 * 10 ** 6), #10
          products(list(listing(large_inputs.P11)), 4), #11
          max_primes(500, lambda x: sum(range(x+1))), #12
          first_digits(sum(int(i) for i in large_inputs.P13), 10), #13
          greatest_length(collatz_seq(10 ** 6)), #14
          max(pascal_triangle(40)), #15
          count_length(2**1000), #16
          sum(len(letters(i)) for i in range(1, 1001)), #17
          max_paths(list(listing(large_inputs.P18)))[0], #18
          count_days((1901, 1, 1), (2000, 12, 31)), #19
          count_length(math.factorial(100)), #20
          sum(amicable_numbers(10000)), #21
          sum(sort_n_count(large_inputs.P22).values()), #22
          non_abundant_sums(28123), #23
          len(fibonacci_numbers(lambda x: len(str(x)) < 1000)), #25
          max_paths(list(listing(large_inputs.P67)))[0], #67
        )
