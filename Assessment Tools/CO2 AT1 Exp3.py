n = int(input("Enter number of words: "))

print("{:<12}{:<10}{:<12}{:<15}{:<15}".format(
    "Word", "Stem", "Removed", "Type", "Normalized"
))

for i in range(n):
    word = input("Enter word: ")

    stem = word
    removed = "-"
    transformation = "Unknown"
    normalized = word

    if word.endswith("ing"):
        stem = word[:-3]
        removed = "ing"
        transformation = "Inflectional"
        normalized = stem

    elif word.endswith("ed"):
        stem = word[:-2]
        removed = "ed"
        transformation = "Inflectional"
        normalized = stem

    elif word.endswith("er"):
        stem = word[:-2]
        removed = "er"
        transformation = "Derivational"
        normalized = stem

    print("{:<12}{:<10}{:<12}{:<15}{:<15}".format(
        word,
        stem,
        removed,
        transformation,
        normalized
    ))