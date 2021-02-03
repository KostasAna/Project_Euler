# https://projecteuler.net/problem=1


def sum_div_3_5(x):
    """This function takes all the numbers up to x
    that are divisible by 3 and 5 and it adds them up"""

    my_sum = 0

    for i in range(1, x, 1):
        if i % 3 == 0 or i % 5 == 0:
            my_sum += i

    print(f'The sum of all the numbers up to {x:d} divisible by 3 and 5 is {my_sum:d}')
    return my_sum


# https://projecteuler.net/problem=2


def fib_even_sum(x):
    """This function takes all the even_valued Fibonacci numbers up to x-ith
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
    print(f'The sum of the even-valued Fibonacci numbers smaller than 4 million is {k:d}')
    return k


# https://projecteuler.net/problem=3


def largest_factor(x):
    """This function takes a number and returns its largest prime factor"""

    p_factors = []
    y = round(x ** 0.5 + 1)  # need to check only up to square root of x, not up to x
    z = x  # just to store the initial value of x for the print statement

    for i in range(2, y, 1):
        while x % i == 0:
            p_factors.append(i)
            x = x / i

    print(f'The largest prime factor of {z:d} is {int(p_factors[-1]):d}')
    return p_factors[-1]


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

    print(f'The largest palindromic number made from a product\n'
          f' of numbers between {x:d} and {y:d} is {max(pal_num):d}')
    return max(pal_num)
