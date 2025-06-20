
def problem_function():
    palindrome = 0

    for x in range(9, 0, -1):
        for y in range(9, -1, -1):
            for z in range(9, -1, -1):
                palindrome = (100001 * x) + (10010 * y) + (1100 * z)
                print(f"Palindrome found: {palindrome}")
                for a in range (999, 99, -1):
                    if palindrome % a == 0:
                        for b in range(999, 99, -1):
                            if b == palindrome // a:
                                print(f"product of {a} * {b}")
                                return

problem_function()