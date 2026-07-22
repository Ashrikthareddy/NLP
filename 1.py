import re

text = input("Enter a sentence: ")
pattern = input("Enter the word/pattern to search: ")

search_result = re.search(pattern, text)
match_result = re.match(pattern, text)

if search_result:
    print("\nSearch Result:")
    print("Pattern found at position:", search_result.start())
else:
    print("\nSearch Result:")
    print("Pattern not found.")

if match_result:
    print("\nMatch Result:")
    print("Pattern matched at the beginning of the text.")
else:
    print("\nMatch Result:")
    print("Pattern does not match at the beginning.")