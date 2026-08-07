import nltk
from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*s$', 'NNS'),
    (r'^[0-9]+$', 'CD'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

text = input("Enter a sentence: ")

words = text.split()

tags = tagger.tag(words)

print("\nWord\tPOS Tag")
for word, tag in tags:
    print(word, "\t", tag)