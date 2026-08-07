morphology = {
    "activate": {
        "prefix": "-",
        "root": "active",
        "suffix": "-ate",
        "sequence": "active → activate",
        "meaning": "Converts adjective to verb (to make active).",
        "normalized": "active"
    },
    "activation": {
        "prefix": "-",
        "root": "active",
        "suffix": "-ation",
        "sequence": "active → activate → activation",
        "meaning": "Converts verb to noun (process of activating).",
        "normalized": "active"
    },
    "reactivation": {
        "prefix": "re-",
        "root": "active",
        "suffix": "-ation",
        "sequence": "active → activate → activation → reactivation",
        "meaning": "Adds repetition meaning (activate again).",
        "normalized": "active"
    }
}

words = ["activate", "activation", "reactivation"]

print("{:<15} {:<10} {:<12} {:<10} {:<40} {:<15} {:<35}".format(
    "Original",
    "Prefix",
    "Root",
    "Suffix",
    "Derivational Sequence",
    "Normalized",
    "Parsed Representation"
))

for word in words:
    data = morphology[word]
    parsed = f"{data['prefix']} + {data['root']} + {data['suffix']}"
    print("{:<15} {:<10} {:<12} {:<10} {:<40} {:<15} {:<35}".format(
        word,
        data["prefix"],
        data["root"],
        data["suffix"],
        data["sequence"],
        data["normalized"],
        parsed
    ))

print("\nNormalized Base Representation:")

normalized = {}

for word in words:
    base = morphology[word]["normalized"]
    normalized.setdefault(base, []).append(word)

for base, variants in normalized.items():
    print(f"{base} --> {variants}")