import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'he' | 'she' | 'they'
VP -> 'runs' | 'eats' | 'run' | 'eat'
""")

parser = nltk.ChartParser(grammar)

sentence = input("Enter a sentence: ").lower().split()

try:
    trees = list(parser.parse(sentence))
    if trees:
        print("Sentence is grammatically correct.")
    else:
        print("Sentence is not grammatically correct.")
except ValueError:
    print("Sentence is not grammatically correct.")