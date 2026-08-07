morphology = {
    "create": {
        "suffix": "-",
        "category": "Base Form",
        "root": "create",
        "normalized": "create"
    },
    "creates": {
        "suffix": "-s",
        "category": "Third-Person Singular",
        "root": "create",
        "normalized": "create"
    },
    "creating": {
        "suffix": "-ing",
        "category": "Present Participle",
        "root": "create",
        "normalized": "create"
    }
}

words = ["create", "creates", "creating"]

print("{:<15} {:<10} {:<25} {:<12} {:<15} {:<20}".format(
    "Original",
    "Suffix",
    "Grammatical Category",
    "Root",
    "Normalized",
    "Final Output"
))

for word in words:
    data = morphology[word]
    print("{:<15} {:<10} {:<25} {:<12} {:<15} {:<20}".format(
        word,
        data["suffix"],
        data["category"],
        data["root"],
        data["normalized"],
        data["normalized"]
    ))

print("\nNormalized Base Representation:")

normalized = {}

for word in words:
    base = morphology[word]["normalized"]
    normalized.setdefault(base, []).append(word)

for base, variants in normalized.items():
    print(f"{base} --> {variants}")