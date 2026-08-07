morphology = {
    "govern": {
        "root": "govern",
        "suffix": "-",
        "level": "Level 0 (Base Word)",
        "normalized": "govern"
    },
    "government": {
        "root": "govern",
        "suffix": "-ment",
        "level": "Level 1 (Derived Noun)",
        "normalized": "govern"
    },
    "governance": {
        "root": "govern",
        "suffix": "-ance",
        "level": "Level 1 (Derived Noun)",
        "normalized": "govern"
    }
}

words = ["govern", "government", "governance"]

print("{:<15} {:<12} {:<10} {:<25} {:<15} {:<15}".format(
    "Original",
    "Root",
    "Suffix",
    "Derivational Level",
    "Normalized",
    "Final Output"
))

for word in words:
    data = morphology[word]
    print("{:<15} {:<12} {:<10} {:<25} {:<15} {:<15}".format(
        word,
        data["root"],
        data["suffix"],
        data["level"],
        data["normalized"],
        data["normalized"]
    ))

print("\nNormalized Lexical Representation:")

normalized = {}

for word in words:
    base = morphology[word]["normalized"]
    normalized.setdefault(base, []).append(word)

for base, variants in normalized.items():
    print(f"{base} --> {variants}")