def guess_number():
    print("Think of a number between 1 and 9999.")
    input("Press Enter when you're ready...")

    low = 1
    high = 9999
    guesses = 0

    while low <= high:
        guess = (low + high) // 2
        guesses += 1

        print(f"My guess #{guesses}: {guess}")
        feedback = input("Is your number (h)igher, (l)ower, or (c)orrect? ").strip().lower()

        if feedback == 'c':
            print(f"I guessed it in {guesses} tries!")
            return
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print("Please enter 'h' for higher, 'l' for lower, or 'c' for correct.")

    print("Hmm, something went wrong — are you sure you followed the rules?")

# Run the script
#guess_number()

list_test = [1,4,2,3]

for index, number in enumerate(list_test):
    print(index)

print(list_test[:1])
