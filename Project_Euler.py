# create a timer decorator
import time


def timer(function):
    """This decorator is used to check how long it takes a function to run"""

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

    for i in range(2, round((x + 2) / 2)):
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
            product *= prime_factors(num)[-1]  # function from problem 3

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


def prime_check(x: int) -> int:
    """This function returns True if the number x is prime & False otherwise"""

    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, round(x ** 0.5 + 1)):
        if x % i == 0:
            return False

    return True


def primes(x: int) -> list:
    """This function lists the first x primes"""

    p_list = [2]  # the first prime is 2
    i = 2

    while len(p_list) < x:
        i += 1
        if prime_check(i):
            p_list.append(i)

    return p_list


# https://projecteuler.net/problem=8


def prod(x: int or str) -> int:  # This function is needed within the next one
    """This function multiplies all digits of a number"""

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
            products.append(prod(adjacent))  # function created above

        d = dict(zip(y_digits, products))

    return d


# https://projecteuler.net/problem=9


"""This problem requires some maths beforehand. Constraints:
(1) 0 < a < b < c ,  (2) a + b + c = 1000 ,  (3) a^2 + b^2 = c^2
(2) & (3) => a^2 + b^2 = 10^6 + a^2 + b^2 - 2000*a -2000*b + 2*a*b
<=> 0 = 5*10^5 - 1000(a + b) + ab <=> 0 = 5*10^5 + a(b - 1000) - 1000*b
<=> 0 = a(b - 1000) - 1000(b - 500) <=> 5*10^5 = (b - 1000)(a - 1000) (4)
(1) & (4) => 0 < a < b < 500 <=> -1000 < a - 1000 < b - 1000 < -500
At this point is quite fast and easy to do an exhaustive search."""

for i in range(505, 1000, 5):
    for j in range(1000, 500, -10):
        if i * j == 5 * 10 ** 5:
            a = 1000 - j
            b = 1000 - i
            c = 1000 - a - b


# https://projecteuler.net/problem=10


def primes_sum(x: int) -> int:
    """This function adds all the primes below x"""

    p_sum = 2  # the first prime is 2
    i = 2

    while i < x:
        i += 1
        if prime_check(i):  # function from problem 7
            p_sum += i
        else:
            continue

    return p_sum


# https://projecteuler.net/problem=11

def listing(x: str) -> list:
    """This function takes a matrix in string type and
    returns it as a list of lists"""

    big_list = x.split('\n')
    matrix = []

    for line in big_list:
        row = line.split(' ')
        row = [int(number) for number in row]
        matrix.append(row)

    return matrix


def products(m: list, n: int) -> int:
    """This funcion takes a matrix and returns the greatest product
    of n adjacent numbers in any direction"""

    x = len(m)  # how many rows the matrix has
    y = len(m[0])  # how many columns the matrix has

    alln = []

    for i in range(x):
        for j in range(0, y-n+1):
            alln.append(m[i][j]*m[i][j+1]*m[i][j+2]*m[i][j+3])
            alln.append(m[j][i]*m[j+1][i]*m[j+2][i]*m[j+3][i])

            if i <= (x-n):  # diagonals
                alln.append(m[i][j]*m[i+1][j+1]*m[i+2][j+2]*m[i+3][j+3])
                alln.append(m[i][j+3]*m[i+1][j+2]*m[i+2][j+1]*m[i+3][j])

    return max(alln)


# https://projecteuler.net/problem=12

def divisors(n: int) -> int:
    """This function returns the list of all the factors of a number"""

    divs = [i for i in range(1, int(round(n ** 0.5 + 1, 0))) if n % i == 0]
    divs = divs + [int(n / d) for d in divs[::-1] if n % d == 0]

    return divs


def max_primes(d: int, f: callable) -> int:
    """This function takes as inputs a number d and a function/sequence
    and returns the first number of the sequence with d divisors"""

    i = 1
    while True:
        i += 1
        divs = divisors(f(i))
        if len(divs) > d:
            break

    return f(i)


# https://projecteuler.net/problem=13

def first_digits(num: int, d: int) -> int:
    """This function returns the first d digits of a number"""

    from math import log10
    power = int((log10(num)))
    digits = int(num / (10 ** (power + 1 - d)))

    return digits
