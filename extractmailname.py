import pdfplumber
import re
from collections import OrderedDict
pdf = pdfplumber.open("C:\\Users\\Hp\\Desktop\\python\\res2.pdf")
p0 = pdf.pages[0]
im = p0.to_image()
im
im.reset().draw_rects(p0.chars)
text = p0.extract_text()
text1=text.lstrip()
text1=text1.lower()
emails= re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text1)
email=re.sub(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",'',text1)
print (email)
with open("C:\\Users\\Hp\\Desktop\\python\\Output1.txt", "w" , encoding="utf-8") as text_file:
    text_file.write("%s" %email)
test_file = open('C:\\Users\\Hp\\Desktop\\python\\Output1.txt', 'r' , encoding="utf-8")
test_lines = test_file.readlines()
test_file.close()
# Print second line
print(test_lines[1])
print(test_lines[2:8])
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en_core_web_sm')

doc = nlp(email)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

