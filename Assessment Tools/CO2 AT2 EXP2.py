morphology = {
    "disagree": {
        "prefix": "dis-",
        "root": "agree",
        "suffix": "-",
        "type": "Derivational",
        "meaning": "Expresses the opposite meaning of agree.",
        "normalized": "agree"
    },
    "agreement": {
        "prefix": "-",
        "root": "agree",
        "suffix": "-ment",
        "type": "Derivational",
        "meaning": "Forms a noun indicating the result or state of agreeing.",
        "normalized": "agree"
    },
    "agreeable": {
        "prefix": "-",
        "root": "agree",
        "suffix": "-able",
        "type": "Derivational",
        "meaning": "Forms an adjective meaning pleasant or willing to agree.",
        "normalized": "agree"
    }
}

words = ["disagree", "agreement", "agreeable"]

print("{:<15} {:<10} {:<12} {:<10} {:<15} {:<45} {:<12}".format(
    "Original",
    "Prefix",
    "Root",
    "Suffix",
    "Category",
    "Semantic Interpretation",
    "Normalized"
))

for word in words:
    data = morphology[word]
    print("{:<15} {:<10} {:<12} {:<10} {:<15} {:<45} {:<12}".format(
        word,
        data["prefix"],
        data["root"],
        data["suffix"],
        data["type"],
        data["meaning"],
        data["normalized"]
    ))

print("\nNormalized Base Representation:")

normalized = {}

for word in words:
    base = morphology[word]["normalized"]
    normalized.setdefault(base, []).append(word)

for base, variants in normalized.items():
    print(f"{base} --> {variants}")