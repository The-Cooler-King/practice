# def factorial(number):
#     if number < 1:
#         return 1
#
#     return number * factorial(number - 1)
#
#
# for index in range(101):
#     print(f"{index}: {factorial(index)}")


# def array_sum(array):
#     if len(array) == 0:
#         return 0
#
#     return array[0] + array_sum(array[1:])
#
#
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(array_sum(array))

# def reverse_string(word):
#     if word == "":
#         return ""
#
#     return reverse_string(word[1:]) + word[0]
#
# print(reverse_string("Vincent Hamalainen"))


sample = {"key1": "value1", "key2": "value2", "key3": "value3"}
for index, key in enumerate(sample):
    print(index, key)