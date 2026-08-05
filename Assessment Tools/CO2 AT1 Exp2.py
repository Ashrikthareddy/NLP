words = ["unhappy", "happiness", "happily"]

print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<12}".format(
    "Word", "Prefix", "Root", "Suffix", "Transformation", "Normalized"
))

for word in words:
    prefix = "-"
    suffix = "-"
    root = ""
    transformation = "Derivational"

    if word.startswith("un"):
        prefix = "un"
        root = "happy"

    elif word.endswith("ness"):
        suffix = "ness"
        root = "happy"

    elif word.endswith("ly"):
        suffix = "ly"
        root = "happy"

    else:
        root = word

    print("{:<12}{:<10}{:<10}{:<10}{:<15}{:<12}".format(
        word,
        prefix,
        root,
        suffix,
        transformation,
        "happy"
    ))