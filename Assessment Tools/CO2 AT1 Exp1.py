words = ["connected", "connecting", "connection"]

suffixes = {
    "ed": "Inflectional",
    "ing": "Inflectional",
    "ion": "Derivational"
}

print("{:<15}{:<15}{:<15}{:<18}{:<15}".format("Word", "Root", "Suffix", "Type", "Normalized"))

for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        normalized = "connect"
    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        normalized = "connect"
    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        normalized = "connect"
    else:
        root = word
        suffix = "-"
        normalized = word

    print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
        word,
        root,
        suffix,
        suffixes.get(suffix, "-"),
        normalized
    ))