import unittest
import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from is_prime import is_prime


class TestIsPrime(unittest.TestCase):

    def test_negative_numbers_and_zero(self):
        # Arrange
        inputs = [-10, -1, 0]

        # Act & Assert
        for n in inputs:
            self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_small_non_primes(self):
        # Arrange
        inputs = [1, 4, 6, 8, 9, 10]

        # Act & Assert
        for n in inputs:
            self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_small_primes(self):
        # Arrange
        primes = [2, 3, 5, 7]

        # Act & Assert
        for n in primes:
            self.assertTrue(is_prime(n), f"{n} should be prime")

    def test_larger_primes(self):
        # Arrange
        primes = [29, 31, 97, 101, 997]

        # Act & Assert
        for n in primes:
            self.assertTrue(is_prime(n), f"{n} should be prime")

    def test_larger_non_primes(self):
        # Arrange
        non_primes = [100, 102, 111, 121, 1001]

        # Act & Assert
        for n in non_primes:
            self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_large_prime_and_non_prime(self):
        # Arrange
        large_prime = 104729  # 10000th prime
        large_non_prime = 104730  # one more than that

        # Act
        result_prime = is_prime(large_prime)
        result_non_prime = is_prime(large_non_prime)

        # Assert
        self.assertTrue(result_prime, f"{large_prime} should be prime")
        self.assertFalse(result_non_prime, f"{large_non_prime} should not be prime")


if __name__ == "__main__":
    unittest.main()
