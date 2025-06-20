def problem_function(top_of_divisor_range):
    smallest_product_or_highest_two_factors = top_of_divisor_range * (top_of_divisor_range - 1)
    product = smallest_product_or_highest_two_factors

    while True:

        for divisor in range(top_of_divisor_range, top_of_divisor_range // 2 - 1, -1):

            if product % divisor != 0:
                break
            else:
                if divisor == top_of_divisor_range // 2:
                    return product

        product += smallest_product_or_highest_two_factors


for number in range(2, 25, 1):
    print(f"Smallest product for {number}: {problem_function(number)}")