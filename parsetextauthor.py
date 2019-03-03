# author extraction using spacy 
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

doc = nlp(sentence)
print("Author :")
for X in doc.ents :
    if X.label_=='PERSON' :
        print(X.text)
