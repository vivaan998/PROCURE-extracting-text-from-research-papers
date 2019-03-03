import pytesseract as py
from PIL import Image
import pdf2image

#extracting pdf file into image

pdf2image.convert_from_path(r'C:\\Users\\Hp\\Desktop\\python\\extract.pdf' , output_folder=r'C:\\Users\\Hp\\Desktop\\python')
text=[None]*(len(pages))


for i in range(1):
    text[i]=py.image_to_string(pages[i])
    print(text[0])

#importing nltk for text summarizing

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

text1 = text[0]
for txt in nltk.sent_tokenize(text1):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(txt))):
        if hasattr(chunk, 'label'):
            #print(type(chunk))
            print("Author :")
            if (chunk.label()=='PERSON'):
                print(chunk.label(), ' '.join(c[0] for c in chunk))
                

                
#importing spacy for Author name extraction 

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()


doc = nlp(text1)
print("AUTHOR :")
for x in doc.ents :
    if x.label_=='PERSON' :
        print(x.text)
   


i_abstract=text[0].find('Abstract')
if(i_abstract==-1):
    i_abstract=word.find('ABSTRACT')
    if(i_abstract==-1):
        print("<<<<<<<<-----Abstract not found in paper----->>>>>>>")
# print(i_abstract)
        
        
abstract=['']*10000     
    
    
        
if(i_abstract!=-1):
    i_intro=text[0].find('Introduction')
    if(i_intro==-1):
        i_intro=text[0].find('INTRODUCTION')
            
i_intro=i_intro-3           
i=0
if(i_intro!=-1):
    for j in range(i_abstract+9,i_intro,1):
        abstract[i]=text[0][j]
        i=i+1


        
abstract=''.join(abstract)
print("ABSTRACT  :" , abstract)


#method to diffrentiate and extract abstract from given pdf

