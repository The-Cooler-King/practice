import heapq


def runningMedianchatgpt(a):
    lowers = []  # Max-heap (invert numbers to use Python's min-heap as max-heap)
    highers = []  # Min-heap
    medians = []

    for number in a:
        # Step 1: Add to one of the heaps
        if not lowers or number < -lowers[0]:
            heapq.heappush(lowers, -number)
        else:
            heapq.heappush(highers, number)

        # Step 2: Rebalance the heaps (make sure the size difference is at most 1)
        if len(lowers) > len(highers) + 1:
            heapq.heappush(highers, -heapq.heappop(lowers))
        elif len(highers) > len(lowers) + 1:
            heapq.heappush(lowers, -heapq.heappop(highers))

        # Step 3: Get the median
        if len(lowers) == len(highers):
            median = (-lowers[0] + highers[0]) / 2.0
        elif len(lowers) > len(highers):
            median = -lowers[0] * 1.0
        else:
            median = highers[0] * 1.0

        medians.append(float(f"{median:.1f}"))

    return medians


def runningMedian(a):
    # Write your code here
    # we need a min heap and a max heap
    # the max heap will be the lower group of integers e.g. [-5, -3, -4, -1]
    # the min heap will be the high group of integers e.g. [7, 20, 21, 22]

    low_numbers = []
    high_numbers = []
    medians = []

    for index, number in enumerate(a):
        number = float(number)
        if index == 0:
            low_numbers.append(-number)
            high_numbers.append(number)
            median = number
            heapq.heapify(low_numbers)
            heapq.heapify(high_numbers)

        elif (
                index + 1) % 2 == 0:  # this number makes list length even which means the median is the average of
            # the two roots
            if number < median:  # this number is less than the median which is currently shared by both heaps at the
                # root
                # pop the root from the lower numbers and push the new number to the lower list
                heapq.heappop(low_numbers)
                heapq.heappush(low_numbers, -number)
            else:  # this number is gtoe to the median
                # pop the root from the higher numbers and push the new number to the lower list
                heapq.heappop(high_numbers)
                heapq.heappush(high_numbers, number)
            # calculate median as the average of the root of both heaps
            median = (-low_numbers[0] + high_numbers[0]) / 2

        else:  # this number makes list length odd which means root is shared by both lists and is the median
            if number >= -low_numbers[0]:
                if number <= high_numbers[0]:  # if number is in between both roots, inclusively, this is the new
                    # median and will become
                    # the root of both
                    heapq.heappush(low_numbers, -number)
                    heapq.heappush(high_numbers, number)
                    median = number
                else:  # the number goes on the high side
                    heapq.heappush(low_numbers, -high_numbers[0])
                    heapq.heappush(high_numbers, number)
                    median = high_numbers[0]
            else:  # the number goes on the low side
                heapq.heappush(high_numbers, -low_numbers[0])
                heapq.heappush(low_numbers, -number)
                median = high_numbers[0]

    return medians

import random

input_list = []
for index in range(10000):
    input_list.append(random.randint(1,10000))

chatgpt_medians = runningMedianchatgpt(input_list)
my_medians = runningMedian(input_list)

for index, median in enumerate(my_medians):
    if median != chatgpt_medians[index]:
        print(f"At index: {index} there was a discrepancy")
        print(f"My median: {median}")
        print(f"Chat GPT's median: {chatgpt_medians[index]}")

