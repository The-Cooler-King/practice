print("1")
print("2")


def fibonacci_sequence(term_minus_one, term_minus_two, even_sum):
    new_term = term_minus_one + term_minus_two
    if new_term <= 4000000:
        print(new_term)
        if new_term % 2 == 0:
            print("EVEN!!!!")
            print(f"even_sum before: {even_sum}")
            even_sum += new_term
            print(f"even_sum after: {even_sum}")

        fibonacci_sequence(new_term, term_minus_one, even_sum)
    return even_sum


fibonacci_sequence(2, 1, 2)
