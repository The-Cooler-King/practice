def is_prime(n: int) -> bool:
    """
    Determines whether a given integer is a prime number.

    This function uses the 6k ± 1 optimization to reduce the number of
    divisibility checks required. Here's how it works:

    - Numbers less than or equal to 1 are not prime by definition.
    - 2 and 3 are the first two primes, handled as special cases.
    - Any number divisible by 2 or 3 is not prime.
    - All primes greater than 3 can be written in the form 6k ± 1.
      So we check divisibility starting from 5 and 7, then 11 and 13, and so on
      (i.e., i and i + 2), incrementing i by 6 each time.

    This reduces the number of checks from O(n) to approximately O(√n / 3),
    making it efficient for relatively large numbers.

    Parameters:
        n (int): The integer to test for primality.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False  # 0 and 1 are not prime
    if n <= 3:
        return True   # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # eliminate multiples of 2 and 3

    candidate_factor = 5
    while candidate_factor * candidate_factor <= n:
        # Check for divisibility by 6k - 1 and 6k + 1
        if n % candidate_factor == 0 or n % (candidate_factor + 2) == 0:
            return False
        candidate_factor += 6

    return True
