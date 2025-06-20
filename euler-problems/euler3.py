def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# big_effin_number = 600,851,475,143
big_effin_number = 600851475143


# for index in range(2, int(big_effin_number/2) + 1):
#     print(f"Index: {index}")
#     if big_effin_number % index  == 0:
#         print(f"Factor found at {big_effin_number/index}")
#         print("Checking primeness...")
#         if is_prime(big_effin_number/index):
#             print(f"The largest prime factor of {big_effin_number} is {big_effin_number/index}")
#             break

# Chat GPT answer
def largest_prime_factor(n):
    # Step 1: Remove all factors of 2
    while n % 2 == 0:
        n //= 2
    # Now n is odd. Start checking odd divisors from 3 onward.
    i = 3
    max_factor = 1
    while i * i <= n:
        while n % i == 0:
            max_factor = i
            n //= i
        i += 2
    # If n is still > 2, it's a prime factor itself
    if n > 2:
        max_factor = n
    return int(max_factor)

print(largest_prime_factor(big_effin_number))