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


def isMatch_deprecated(s: str, p: str) -> bool:
    """
    Determines whether the input string `s` matches the simplified regex pattern `p`.

    Supported pattern features:
    - '.' matches any single character
    - '*' matches zero or more of the preceding character
    """

    pattern_index = 0
    string_index = 0

    while pattern_index < len(p) and string_index < len(s):
        next_pattern_index = pattern_index + 1
        current_pattern_char = p[pattern_index]

        # Case 1: The next pattern char is "*", meaning repetition
        if next_pattern_index < len(p) and p[next_pattern_index] == '*':
            # Special case: ".*" is treated as a full wildcard match
            if current_pattern_char == '.':
                return True

            # Skip over the "<char>*" in the pattern
            pattern_index += 2

            # Consume as many matching characters as possible
            while string_index < len(s) and s[string_index] == current_pattern_char:
                string_index += 1

        # Case 2: Single-character match
        else:
            pattern_index += 1

            if current_pattern_char == '.' or current_pattern_char == s[string_index]:
                string_index += 1
            else:
                return False

    # Successfully match only if both pattern and string are fully consumed
    if pattern_index == len(p) and string_index == len(s):
        return True

    return False


# print(f'Does "aaa" match pattern "a*": {isMatch("aaa", "a*")}')
# print(f'Does "aa" match pattern "a": {isMatch("aa", "a")}')
# print(f'Does "aa" match pattern "a*": {isMatch("aa", "a*")}')
# print(f'Does "ab" match pattern ".*": {isMatch("ab", ".*")}')
# print(f'Does "vincenttttt" match pattern "vin.e.t*": {isMatch("vincenttttt", "vin.e.t*")}')

'''
I have apparently missed something that is implicit in the problem statement, but not explicit.

".*" is a match of any length of string, but if characters come after that e.g., ".*xyz" we need to match these characters as well
No ideas are really jumping out to me and the possibility of a pattern such as "abc.*mno.*tuv.*z" throws me for even more of a loop
there must be something simple that I am missing.
my first instinct is to search for the next pattern character after .*

pattern = "abc.*hij" string = "abcdefghij" 
we pass "defg" and then we hit h and start matching again

okay well now consider:
pattern = "abc.*hij" string = "abcdefghihihihihij"
now we get to the first "hi" and this is not a match so we need to move on to the next one
since there might be overlap:
pattern = "abc.*hhhij" string = "abcdefghhhhhhhhhhij"
we need to only regard the starting point of the possible match and when the match is invalid, we have to move to the next index from the starting point.
perhaps there is a chance for optimization here

okay well now consider:
pattern = "abc.*hhh" string = "abcdefghhhhhhhhhh"
in our current solution, and with how we are thinking about fixing our solution this would wrongly be labeled false. The first "hhh"
substring would match and there would be a whole bunch of h's left in the string unmatched.

well thats easy to solve right? flip the end of the pattern around and match starting with the last character! duh
no, I'm not so sure we can do that. at least not so simply.
pattern = "abc.*mno.*tuv.*z"
this pattern confounds that plan, at least initially. after "abc" we encounter our first .* and if we go to the end of the string, we may 
match to an "mno" that happens too late. this will be hard to illustrate with this example. let me choose a new one
pattern = "a.*d.*f.*e" string = "abcdfde"
"a.*" --> "abcdf"
"d.*" --> "d"
"f" --> "e" NO MATCH

What we want
"a.*" --> "abc"
"d.*" --> "d"
"f.*" --> "fd"
"e" --> "e" MATCH

i guess we need recursion...
we keep going deeper every time we encounter an *
or rather is it every time we encounter a match?
yah maybe something like return isMatch(p[1:], s[1:]) something like that

base case is:
if s == "" and p = "":
    return True
    
and then we need to handle both of the possibilities repetition and single-character matching
if p[1] == "*"
    repetition
else:
    if current_char = string_char:
        return isMatch(p[1:], s[1:])
    return False

so the repetition part needs to try all possibilities. if any of them hit the base case, it is a match
'''


def isMatch(s: str, p: str) -> bool:
    """
    Determine whether the entire input string `s` matches the pattern `p`.

    This function implements a recursive matcher for a restricted regular
    expression language with the following operators:

        - Literal characters match themselves
        - '.' matches any single character
        - '*' matches zero or more occurrences of the immediately preceding
          element (either a literal or '.')

    The match is anchored: the pattern must consume the entire input string
    for the result to be True. Partial matches are not considered valid.

    Approach
    --------
    The algorithm proceeds by recursively comparing the remaining suffixes
    of the string and pattern. At each step, the matcher examines the first
    character of the pattern and applies one of two strategies:

    1. Repetition ('*'):
       If the next pattern character is '*', the matcher explores all valid
       ways to interpret the repetition:
         - The repetition matches zero characters, and the matcher advances
           past the '<char>*' construct in the pattern.
         - The repetition matches one or more characters, consuming characters
           from the input string as long as they match the repeated element.

       If any interpretation leads to a successful match of the remaining
       string and pattern, the function returns True.

    2. Single-character match:
       If no repetition operator is present, the current pattern character
       must match exactly one character from the input string (either via
       literal equality or '.'). The matcher then recurses on the remaining
       suffixes.

    Base Cases
    ----------
    - If the pattern is empty, the match succeeds only if the string is also
      empty.
    - If the pattern requires a character but the string is exhausted, the
      match fails.

    Complexity
    ----------
    This implementation prioritizes clarity and correctness over performance.
    In the presence of multiple '*' operators, the recursion may explore
    overlapping subproblems, leading to exponential worst-case time complexity.
    Memoization can be applied as a future optimization to reduce this to
    O(len(s) * len(p)).

    Parameters
    ----------
    s : str
        The input string to be matched.
    p : str
        The pattern string containing literals, '.', and '*'.

    Returns
    -------
    bool
        True if the pattern matches the entire string; False otherwise.
    """
    # Base case
    if p == "":
        return s == ""

    current_char = p[0]

    # Case 1: Repetition
    if len(p) > 1 and p[1] == "*":

        for index in range(len(s)):
            # Zero occurrence case
            if isMatch(s, p[2:]):
                return True

            if s[index] == current_char or current_char == ".":
                if isMatch(s[index + 1:], p[2:]):
                    return True
                else:
                    continue
            else:
                return False

        # Zero occurrence case for empty string
        if len(s) == 0 and len(p) <= 2:
            return True
        return False

    # Case 2: Single-character matching
    else:
        if len(s) == 0:
            return False

        if current_char == "." or current_char == s[0]:
            return isMatch(s[1:], p[1:])
        return False

#isMatch("mississippi", "mis*is*p*.")
#print(isMatch("ssippi", "p*."))
print(isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*c"))
'''
s =
"aaaaaaaaaaaaab"
p =
"a*a*a*a*a*a*a*a*a*c"
'''