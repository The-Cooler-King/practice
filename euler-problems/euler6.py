'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def sum_of_n_squares(n):
    sum = 0

    for number in range(1, n + 1):
        sum += number ** 2

    return sum


def sum_of_n_squared(n):
    sum = 0

    for number in range(1, n + 1):
        sum += number

    return sum ** 2


def get_difference(n):
    squares_sum = sum_of_n_squares(n)
    print(f"The sum of the squares of the first {n} natural numbers is, {squares_sum}")
    sum_squared = sum_of_n_squared(n)
    print(f"The square of the sum of the first {n} natural numbers is, {sum_squared}")

    print(f"The difference is, {sum_squared - squares_sum}")

get_difference(100)
