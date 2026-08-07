words = input("Enter words separated by space: ").split()

tags = []

for word in words:
    if word.endswith("ing"):
        tags.append((word, "VBG"))
    elif word.endswith("ed"):
        tags.append((word, "VBD"))
    elif word[0].isupper():
        tags.append((word, "NNP"))
    elif word.endswith("ly"):
        tags.append((word, "RB"))
    else:
        tags.append((word, "NN"))

print("\nWord\tPOS Tag")
for word, tag in tags:
    print(word, "\t", tag)