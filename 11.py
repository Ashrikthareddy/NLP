import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

parser = nltk.TopDownChartParser(grammar)

sentence = input("Enter a sentence: ").lower().split()

for tree in parser.parse(sentence):
    print(tree)