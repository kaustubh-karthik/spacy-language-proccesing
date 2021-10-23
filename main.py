import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

displacy.render(doc, style='dep')

for token in doc:
    print(token.text, token.pos_, token.dep_)
    