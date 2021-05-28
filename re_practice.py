import re

# * r" " means raw string (it will also include special characters such as \n or \t)
# * re.finditer will return the position of the text and also the matched text (returns list)
# * re.findall only returns the string itself (returns list)
# * re.match only checks the beginning of the string, returns the position and the matching text
# * re.search checks the whole string, returns the first matching object position and the text

# * finditer(), search(), findall(), match()
# * match.span(), match.start(), match.end() -> return the span values of the match
# * match.group() -> return the matching text

# * Meta Characters:  . ^ $ * + ? { } [ ] \ | ( )

"""
.   Any character (except newline character)
^   Starts with "^hello"
$   Ends with "world$"
*   Zero or more occurences "ajz*"
+   One or more occurences "ajz+"
{ } Exactly the specified number of occurences "al{2}"
[ ] A set of characters "[a-m]"
\   Special sequence "\d", "\n", "\t"
|   Either or  "com|net|edu"
( ) Capture and group

========================= Special Characters =========================
\d  Matches any decimal digit [0-9]
\D  Matches any non-digit characters
\s  Matches any whitespace characters  
\S  Matches any non-whitespace characters
\w  Matches any alphanumeric characters [a-zA-z0-9_]
\W  Matches any non-alphanumeric characters 
\b  Matches where the specified characters are at the beginning or the end of a word r"\bain" r"ain\b"
\B  Matches where the specified characters are present, but NOT at the beginning 

========================= Quantifiers =========================
*       Zero or more occurences
+       One or more occurences
?       Zero or more (optional character)
{4}     Exact number of matches
{4,6}   Range number of matches (min, max)

========================= Modification =========================
split() split the string with given pattern and returns the list of splitted strings
sub()   replaces the matching patters with the given pattern or string

========================= Flags =========================
ASCII, A            
DOTALL, S           Make . match any character, including new lines
IGNORECASE, I       Do case insensitive matches
LOCALE, L           Do a locale-aware match
MULTILINE, M        Multiline matching, affects ^ and $
VERBOSE, X          
"""

# test_string = "hello_1234534513123_ heyho hohey"

#* ==================================================
# test_string = """
# 2021/05/31
# 2021 05 31
# 2021.05.31
# 2021/05/31
# 31-05-2021
# """
# pattern = re.compile(r"\d{4}[-/]\d{2}[-/]\d{2}")

#* ==================================================
# test_string = """
# Hello world
# 12345
# 2021.05.31
# 2021/05/31
# 31-05-2021
# Mr Smith
# Mrs Smith
# Mr. Brown
# Ms Simpson
# Mr. T
# """
# pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s\w+")

# matches = pattern.finditer(test_string)
# [print(m) for m in matches]

#* ========================= Quantifiers =========================
# test_string = "123abc456789abc123ABC"
# pattern = re.compile(r"\d{3}")
# splitted = pattern.split(test_string)
# [print(s) for s in splitted]

#* ========================= Logical =========================
# test_string = """
# Hello world
# 12345
# 2021.05.31
# 2021/05/31
# 31-05-2021
# Mr Smith
# Mrs Smith
# Mr. Brown
# Ms Simpson
# Mr. T
# """
# pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s\w+")

#* ========================= Modification (string) =========================
# test_string = "hello world, you are the best world!"
# pattern = re.compile(r"world")
# subbed = pattern.sub("planet", test_string)
# print(subbed)

#* ========================= Modification (pattern) =========================
# url = """
#     https://www.google.com
#     http://www.google.com
#     https://google.com
# """
# pattern = re.compile(r"https?://(www\.)?([a-zA-Z]+)(\.[a-zA-Z]+)")
# matches = pattern.finditer(url)
# [print(m.group()) for m in matches]

# subbed_url = pattern.sub(r"\2\3", url)
# print(subbed_url)

#* ========================= Flags =========================
# my_string = "Hello World"
# pattern = re.compile(r"world", re.IGNORECASE)   #* re.I is also okay
# matches = pattern.finditer(my_string)
# for m in matches: print(m)

# s = "   +32 123"      # return 32
# s = "words and 987"   # returns 0
s = "4193 with words" # returns 4193
pattern = re.compile(r"^\s*[+-]?[0-9]+")
m = pattern.match(s)
print(max(min(int(m.group()),(2**31) -1), -(2**31)) if m else 0)

