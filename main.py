import spacy
from spacy import displacy
from IPython.core.display import display, HTML

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

svg = displacy.render(doc, style='dep', minify='true')

with open('spacy-NLP/sentence_connections.svg', 'w', encoding='utf-8') as connections:
    connections.write(svg)

for token in doc:
    print(token.text, token.pos_, token.dep_)
