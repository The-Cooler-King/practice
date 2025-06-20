three_counter = 0
five_counter = 0
sum_of_multiples = 0

for index in range(1, 1000):
    three_counter += 1
    five_counter += 1

    if three_counter == 3:
        sum_of_multiples += index
        three_counter = 0
        if five_counter == 5:
            five_counter = 0
    elif five_counter == 5:
        sum_of_multiples += index
        five_counter = 0

print(sum_of_multiples)