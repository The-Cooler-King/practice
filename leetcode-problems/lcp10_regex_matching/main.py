'''
alright so i think we need to need to use two pointers: one pointer to progress through our regex and one to progress through the string
lets check and see if i have that right
when progressing through the regex pattern we need to check on the next character. if the next character is not a * then we are doing
one to one matching.

i have two questions:
1. what if I put two * in a row? e.g. "a**"
The first asterisk is telling me to look for all the a's in a row, but what is the second asterisk saying?
Ahh it seems that this is answered in the constraints:
    "It is guaranteed for each appearance of the character *, there will be a previous valid character to match."

2. in the event of a ".*" pattern, is the value of the wild "." set by the first character? I'm guessing so.
"aaaaaaaaa" would match that pattern for sure, but would "abbbbbb" not also match the pattern?
I am going to guess that the first letter sets the value of the wild, otherwise '.*' would match any string

okay so we start at the beginning of our regex:
check to see if the next character is a "*" (i think we can use next(char) for this. it is convenient that I just encountered it in someone's code)
if not then
    if char is .
        match to any character and progress both pointers
    if char is a letter
        see if letter matches the letter in s and if so progress both pointers. otherwise return false
if the next char is a * then
    if char is .
        set wild as char in s and progress s pointer until another char is encountered
    if char is letter
        progress s pointer until another char is encountered (THIS CAN BE CLEARLY WRITTEN BY COMBINING THE TWO ABOVE CONDITIONALS)

if we get to the end of the pattern and the string, we have a successful match

in which case I think we need a while loop that runs as long as we are within bounds of regex and s
and then we also need a check at the end to make sure both pointers are at the ends

this runs in O(n). we are only able to go through one character at a time and have to check all of them to be sure the pattern matches the string
therefore, this is optimized
also we are not creating any additional memory structures so we are optimized from a space complexity perspective as well
'''


# class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #
    #     regex_pointer = 0
    #     string_pointer = 0
    #
    #     while regex_pointer < len(p) and string_pointer < len(s)
    #         next_regex_index = regex_pointer + 1
    #         if next_regex_index < len(p) and p[next_regex_index] == '*': # repeating char
    #             repeating_char = p[regex_pointer]
    #             if repeating_char == '.':
    #                 repeating_char = s[string_pointer]
    #
    #             while string_pointer < len(s) and s[string_pointer] == repeating_char:
    #                 string_pointer += 1
    #
    #         else:
    #             matching_char = p[regex_pointer]
    #             if matching_char == '.' or matching_char == s[string_pointer]:
    #                 string_pointer += 1
    #             else:
    #                 return False
    #
    #     if regex_pointer == len(p) - 1 and string_pointer == len(s) - 1:
    #         return True
    #
    #     return False

def isMatch(s: str, p: str) -> bool:

    regex_pointer = 0
    string_pointer = 0

    while regex_pointer < len(p) and string_pointer < len(s):
        next_regex_index = regex_pointer + 1
        if next_regex_index < len(p) and p[next_regex_index] == '*':  # repeating char
            repeating_char = p[regex_pointer]
            if repeating_char == '.':
                repeating_char = s[string_pointer]

            while string_pointer < len(s) and s[string_pointer] == repeating_char:
                string_pointer += 1

        else:
            matching_char = p[regex_pointer]
            if matching_char == '.' or matching_char == s[string_pointer]:
                string_pointer += 1
            else:
                return False

    if regex_pointer == len(p) - 1 and string_pointer == len(s) - 1:
        return True

    return False


print(isMatch("aaa", "a*"))
