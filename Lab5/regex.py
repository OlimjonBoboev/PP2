import re

# 1. Match 'a' followed by zero or more 'b's
def match_a_b(s):
    return bool(re.fullmatch(r'a*b*', s))

print(match_a_b("ab"))  # True
print(match_a_b("a"))   # True
print(match_a_b("abb")) # True
print(match_a_b("b"))   # False

# 2. Match 'a' followed by two to three 'b's
def match_a_bbb(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

print(match_a_bbb("abb"))   # True
print(match_a_bbb("abbb"))  # True
print(match_a_bbb("a"))     # False

# 3. Find sequences of lowercase letters joined with an underscore
def find_lower_underscore(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

print(find_lower_underscore("hello_world test_string"))  # ['hello_world', 'test_string']

# 4. Find sequences of one uppercase letter followed by lowercase letters
def find_upper_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

print(find_upper_lower("Hello World Test"))  # ['Hello', 'World', 'Test']

# 5. Match 'a' followed by anything, ending in 'b'
def match_a_any_b(s):
    return bool(re.fullmatch(r'a.*b', s))

print(match_a_any_b("acb"))  # True
print(match_a_any_b("ab"))   # True
print(match_a_any_b("a123b")) # True
print(match_a_any_b("abc"))  # False

# 6. Replace spaces, commas, or dots with a colon
def replace_chars(s):
    return re.sub(r'[ ,.]', ':', s)

print(replace_chars("Hello, World. How are you"))  # "Hello:World:How:are:you"

# 7. Convert snake case to camel case
def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))

print(snake_to_camel("hello_world_test"))  # "HelloWorldTest"

# 8. Split a string at uppercase letters
def split_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

print(split_uppercase("HelloWorldTest"))  # ['Hello', 'World', 'Test']

# 9. Insert spaces between words starting with capital letters
def insert_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

print(insert_spaces("HelloWorldTest"))  # "Hello World Test"

# 10. Convert camel case to snake case
def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

print(camel_to_snake("HelloWorldTest"))  # "hello_world_test"
