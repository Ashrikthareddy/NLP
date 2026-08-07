import random
from collections import defaultdict

text = input("Enter a sentence: ")

words = text.split()

bigrams = defaultdict(list)

for i in range(len(words) - 1):
    bigrams[words[i]].append(words[i + 1])

start = random.choice(words[:-1])
result = [start]

for i in range(9):
    if start in bigrams:
        next_word = random.choice(bigrams[start])
        result.append(next_word)
        start = next_word
    else:
        break

print("\nGenerated Text:")
print(" ".join(result))