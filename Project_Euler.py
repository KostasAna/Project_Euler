# create a timer decorator
import time


def timer(function):
    """This decorator is used if I need to check how long it takes a function to run"""

    def wrapper(*args, **kwargs):
        time_start = time.time()
        outcome = function(*args, **kwargs)
        total_time = time.time() - time_start
        print(f'Total time needed: {total_time:f}')
        return outcome

    return wrapper

# https://projecteuler.net/problem=1


def sum_div(x: int, *args) -> int:
    """This function takes all the numbers up to x
    that are divisible by *args and it adds them up"""

    my_sum = 0

    for num in range(x):
        if any(num % i == 0 for i in args):
            my_sum += num

    return my_sum


# https://projecteuler.net/problem=2


def fib_even_sum(x: int) -> int:
    """This function takes all the even valued Fibonacci numbers
     smaller than x and adds them up"""

    i = 0
    a = [1, 1]  # to start the Fibonacci series
    even = []

    while True:
        i += 1
        result = a[i] + a[i - 1]
        a.append(result)
        if result >= x:
            break
        if result % 2 == 0:
            even.append(result)

    k = sum(even)

    return k


# https://projecteuler.net/problem=3


def prime_factors(x: int) -> list:
    """This function lists all the prime factors of the number x.
    If it is prime it returns only itself"""

    p_factors = []

    for i in range(2, round((x + 1) / 2)):
        while x % i == 0:
            p_factors.append(i)
            x = x / i
        if x == 1:
            break

    if x != 1:  # in case it is prime
        p_factors.append(x)

    return p_factors


# https://projecteuler.net/problem=4


def max_pal_num(x: int, y: int) -> int:
    """This function takes a range of values (x, y) in which it finds
    the largest palindromic number of all the products in that range"""

    pal_num = []

    for i in range(x, y):
        for j in range(x, y):
            if str(i * j) != str(i * j)[::-1]:
                continue
            else:
                pal_num.append(i * j)

    return max(pal_num)


# https://projecteuler.net/problem=5


def div_mul(x: int) -> int:
    """This function finds the smallest positive number that
    is evenly divisible by all of the numbers up to x"""

    product = 1

    for num in range(2, x):
        if product % num != 0:
            product *= prime_factors(num)[-1]  # using the function of prime factors from problem 3

    return product


# https://projecteuler.net/problem=6


def sum_sum(x: int) -> int:
    """This function calculates the difference between the sum of the squares
    of the first x natural numbers and the square of the sum"""

    ss = 0
    s = 0

    for num in range(x + 1):
        s += num
        ss += num ** 2

    my_sum = s ** 2 - ss

    return my_sum


# https://projecteuler.net/problem=7


def primes(x: int) -> list:
    """This function lists the first x primes"""

    p_list = [2]  # the first prime is 2
    i = 2

    while True:
        i += 1
        if prime_factors(i)[0] == i:  # using the function of prime factors from problem 3
            p_list.append(i)
            if len(p_list) == x:
                break

    return p_list


# https://projecteuler.net/problem=8


def prod(x: int or str) -> int:  # This function is needed within the next one
    """This function multiplies all digits of a number """

    product = 1

    for i in str(x):
        product *= int(i)

    return product


def seq_prod(x, y):
    """This function takes all the y adjacent digits of x and
    returns a dictionary with its products"""

    y_digits = []  # all the adjacent numbers
    products = []  # and their products

    if len(str(x)) <= y:  # no point in that case so just return empty
        return {'None': 0}

    else:
        for digit in range(len(str(x)) - y + 1):
            y_digits.append(str(x)[digit: digit + y])

        for adjacent in y_digits:
            products.append(prod(adjacent))  # using the function created above

        d = dict(zip(y_digits, products))

    return d
