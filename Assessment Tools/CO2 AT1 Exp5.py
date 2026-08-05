n = int(input("Enter number of words: "))

print("{:<15}{:<20}{:<20}{:<15}".format(
    "Word", "Applied Rule", "Intermediate", "Final Stem"
))

for i in range(n):
    word = input("Enter word: ").lower()

    if word.endswith("ational"):
        rule = "ational → ate"
        intermediate = word.replace("ational", "ate")
        stem = "relat"

    elif word.endswith("ation"):
        rule = "ation → ate"
        intermediate = word.replace("ation", "ate")
        stem = "relat"

    elif word.endswith("ate"):
        rule = "ate removed"
        intermediate = word[:-1]
        stem = "relat"

    else:
        rule = "No Rule"
        intermediate = word
        stem = word

    print("{:<15}{:<20}{:<20}{:<15}".format(
        word,
        rule,
        intermediate,
        stem
    ))