import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

with open(r'C:\Users\Kaustubh Karthik\Downloads\freecodecamp_spacy-main\freecodecamp_spacy-main\data\wiki_us.txt', 'r') as file:
    text = file.read()

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

displacy.serve(doc, style='ent', minify=True)
