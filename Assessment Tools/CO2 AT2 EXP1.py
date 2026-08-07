morphology = {
    "analyzing": {
        "root": "analyze",
        "suffix": "-ing",
        "type": "Inflectional",
        "normalized": "analyze"
    },
    "analysis": {
        "root": "analyze",
        "suffix": "-sis",
        "type": "Derivational",
        "normalized": "analyze"
    },
    "analytical": {
        "root": "analyze",
        "suffix": "-ical",
        "type": "Derivational",
        "normalized": "analyze"
    }
}

words = ["analyzing", "analysis", "analytical"]

print("        RULE-BASED MORPHOLOGICAL PROCESSING SYSTEM")

print("{:<15} {:<15} {:<15} {:<18} {:<15}".format(
    "Original Word",
    "Root",
    "Affix",
    "Transformation",
    "Normalized"
))

print("-" * 90)

for word in words:
    if word in morphology:
        data = morphology[word]
        print("{:<15} {:<15} {:<15} {:<18} {:<15}".format(
            word,
            data["root"],
            data["suffix"],
            data["type"],
            data["normalized"]
        ))
    else:
        print("{:<15} {:<15} {:<15} {:<18} {:<15}".format(
            word,
            "Unknown",
            "-",
            "-",
            "-"
        ))


print("\nNormalized Index Representation:")
normalized = {}

for word in words:
    norm = morphology[word]["normalized"]
    normalized.setdefault(norm, []).append(word)

for root, variants in normalized.items():
    print(f"{root} --> {variants}")