# https://projecteuler.net/problem=1


def sum_div_3_5(x):
    """This function takes all the numbers up to x
    that are divisible by 3 and 5 and it adds them up"""

    my_sum = 0

    for i in range(1, x, 1):
        if i % 3 == 0 or i % 5 == 0:
            my_sum += i

    return my_sum


# https://projecteuler.net/problem=2


def fib_even_sum(x):
    """This function takes all the even-valued Fibonacci numbers up to x-ith
    number of the sequence and adds the up. It has a limit of 4 million"""

    a = [1]
    even = []

    for i in range(0, x, 1):
        result = a[i] + a[i - 1]
        a.append(result)
        if result >= 4000000:
            break
        if result % 2 == 0:
            even.append(result)

    k = sum(even)

    return k


# https://projecteuler.net/problem=3


def prime_factors(x):
    """This function takes a number and returns a list of its prime factors"""

    p_factors = []
    y = round(x ** 0.5 + 1)  # need to check only up to square root of x, not up to x

    for i in range(2, y+1, 1):
        while x % i == 0:
            p_factors.append(i)
            x = x / i

    if x != 1:  # if there is factor relatively big to others, it will be bigger than the square root of x
        for j in range(y, int(x+1), 1):  # therefore, we make sure it is added to the list of factors
            while x % j == 0:
                p_factors.append(j)
                x = x / j

    return p_factors


# https://projecteuler.net/problem=4


def max_pal_num(x, y):
    """This function takes a range of values (x, y) in which it finds
    the largest palindromic number of all the products in that range"""

    pal_num = []

    for i in range(x, y, 1):
        for j in range(x, y, 1):
            if str(i * j) != str(i * j)[::-1]:
                continue
            else:
                pal_num.append(i * j)

    return max(pal_num)


# https://projecteuler.net/problem=5


def div_mul(x):
    """This function takes finds the smallest positive number that
    is evenly divisible by all of the numbers from 1 to x"""

    product = 1
    for i in range(2, x, 1):
        if product % i != 0:
            product *= prime_factors(i)[-1]  # using the function of prime factors from problem 3

    return product
