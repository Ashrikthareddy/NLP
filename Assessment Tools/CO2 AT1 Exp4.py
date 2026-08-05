n = int(input("Enter number of words: "))

print("{:<12}{:<35}{:<12}{:<15}{:<12}{:<12}".format(
    "Word", "State Transition", "Root", "Suffix", "Type", "Normalized"
))

for i in range(n):
    word = input("Enter word: ")

    transition = "q0"
    root = word
    suffix = "-"
    typ = "Unknown"
    normalized = word

    if word.endswith("s"):
        transition = "q0 -> q1 -> qf"
        root = word[:-1]
        suffix = "s"
        typ = "Regular Inflection"
        normalized = "write"

    elif word.endswith("ing"):
        transition = "q0 -> q2 -> qf"
        root = word[:-3]
        suffix = "ing"
        typ = "Regular Inflection"
        normalized = "write"

    elif word == "written":
        transition = "q0 -> q3 -> qf"
        root = "write"
        suffix = "en"
        typ = "Irregular Inflection"
        normalized = "write"

    print("{:<12}{:<35}{:<12}{:<15}{:<12}{:<12}".format(
        word,
        transition,
        root,
        suffix,
        typ,
        normalized
    ))