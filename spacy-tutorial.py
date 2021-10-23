import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open("data/wiki_us.txt", 'r') as file:
    text = file.read()

doc = nlp(text)


