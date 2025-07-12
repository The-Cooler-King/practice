'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,0001st prime number?
'''
import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from is_prime import is_prime


def generate_n_primes(n):
    '''
    This function generates the first n prime numbers
    '''

    primes_found = 0
    current_number = 2

    while n > primes_found:
        if is_prime(current_number):
            primes_found += 1
            print(current_number)

        current_number += 1


# print(f"1: {is_prime(1)}")
# print(f"2: {is_prime(2)}")
# print(f"3: {is_prime(3)}")
# print(f"4: {is_prime(4)}")
# print(f"5: {is_prime(5)}")

generate_n_primes(10001)
