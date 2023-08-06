import textract
import re
from urlextract import URLExtract
import networkx as nx
import matplotlib as plt
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
nltk.download('maxent_ne_chunker')
nltk.download('stopwords')
nltk.download('universal_tagset')
nltk.download('stopwords')
nltk.download('words')
from topicrankpy import topicrank as tr
import spacy
import en_core_web_sm as en
import spacy
ner_model= en.load()
from spacy import displacy  



def top_phrases_extraction(path,no_of_phrases):

    text = textract.process(path)
    string= str(text,encoding='utf-8')
    # initialize keyphrase extraction model, here TopicRank
    extractor =  tr.TopicRank()
    # load the content of the document, here document is expected to be in raw
    # format (i.e. a simple text file) and preprocessing is carried out using spacy
    extractor.load_document(input=string,language='en')
    # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
    # and adjectives (i.e. `(Noun|Adj)*`)
    extractor.candidate_selection()
    # candidate weighting, in the case of TopicRank: using a random walk algorithm
    extractor.candidate_weighting()
    # N-best selection, keyphrases contains the 10 highest scored candidates as
    # (keyphrase, score) tuples
    keyphrases = extractor.get_n_best(no_of_phrases)
    return keyphrases


def extract_phone_numbers(path):
    phone_numbers=[]
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    
    #r = re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?')
    phone_numbers.append(re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]',string))
    
    return phone_numbers


def extract_email_addresses(path):
    emails =[]
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    
    emails.append(re.findall(r'\S+@\S+',string))
    return emails


def extract_names(path):

    text = textract.process(path)
    string= str(text,encoding='utf-8')
    
    ORG=[] 
    PRODUCT=[] 
    PERSON=[] 
    NORP=[] 
    FAC=[] 
    GPE=[] 
    LOC=[] 
    EVENT=[] 
    WORK_OF_ART=[] 
    LAW=[] 
    DATE=[] 
    TIME=[] 
    PERCENT=[] 
    MONEY=[] 

    for ent in ner_model(string).ents:
        if ent.label_ == 'ORG':
            if ent.text.strip().lower() not in ORG:
                ORG.append(ent.text.strip().lower())
        if ent.label_ == 'PERSON':
            if ent.text.strip().lower() not in PERSON:
                PERSON.append(ent.text.strip().lower())
        if ent.label_ == 'PRODUCT':
            if ent.text.strip().lower() not in PRODUCT:
                PRODUCT.append(ent.text.strip().lower())
        if ent.label_ == 'DATE':
            if ent.text.strip().lower() not in DATE:
                DATE.append(ent.text.strip().lower())
        if ent.label_ == 'TIME':
            if ent.text.strip().lower() not in TIME:
                TIME.append(ent.text.strip().lower())
        if ent.label_ == 'MONEY':
            if ent.text.strip().lower() not in MONEY:
                MONEY.append(ent.text.strip().lower())
        if ent.label_ == 'PERCENT':
            if ent.text.strip().lower() not in PERCENT:
                PERCENT.append(ent.text.strip().lower())
        if ent.label_ == 'LAW':
            if ent.text.strip().lower() not in LAW:
                LAW.append(ent.text.strip().lower())
        if ent.label_ == 'EVENT':
            if ent.text.strip().lower() not in EVENT:
                EVENT.append(ent.text.strip().lower())
        if ent.label_ == 'GPE':
            if ent.text.strip().lower() not in GPE:
                GPE.append(ent.text.strip().lower())
        if ent.label_ == 'WORK_OF_ART':
            if ent.text.strip().lower() not in WORK_OF_ART:
                WORK_OF_ART.append(ent.text.strip().lower())
        if ent.label_ == 'FAC':
            if ent.text.strip().lower() not in FAC:
                FAC.append(ent.text.strip().lower())
        if ent.label_ == 'NORP':
            if ent.text.strip().lower() not in NORP:
                NORP.append(ent.text.strip().lower())
        if ent.label_ == 'LOC':
            if ent.text.strip().lower() not in LOC:
                LOC.append(ent.text.strip().lower())


    ner_data = {
        'ORGANIZATIONS:': ORG,
        'PERSONS': PERSON,
        'LOC-Non-gpe locations' : LOC,
        'NORP-Nationalities' : NORP,
        'FAC -Buildings' : FAC,
        'WORK_OF_ART' : WORK_OF_ART,
        'GPE' : GPE,
        'DATE' : DATE,
        'EVENT' : EVENT,
        'LAW' : LAW,
        'PERCENT': PERCENT,
        'MONEY' : MONEY,
        'PRODUCT' : PRODUCT
        }
    
    return ner_data
    

def show_ner_output(path):
    from pathlib import Path
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    nlp=ner_model
    doc = nlp(string) 
    html = displacy.render(doc, style="ent")
    output_path = Path("./ner_output.html")
    output_path.open('w', encoding="utf-8").write(html)
    
def extract_urls(path):
    
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    extractor = URLExtract()
    urls = extractor.find_urls(string)
    return urls 
    
def extract_text(path):
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    return string

def extract_all(path,no_of_phrases):
    top_phrases = top_phrases_extraction(path,no_of_phrases)
    phone_numbers = extract_phone_numbers(path)
    email_address = extract_email_addresses(path)
    urls = extract_urls(path)
    ner_output = extract_names(path)
    text_data = extract_text(path)
    data = {
        
        'Top_Phrases_With_Ranking' : top_phrases,
        'Phone_Numbers' : phone_numbers,
        'Email_address' : email_address,
        'URLS': urls,
        'Named Entity Reconition' : ner_output,
        'text' : text_data
    }
    
    #print(data)
    
    return data
    #show_ner_output(path)

#data = extract_all('/home/ayush/Documents/testpdfs/trentdoc.pdf',15)    
#print(data)

#show_ner_output('/home/ayush/Documents/Resume-Tech.pdf')

#############################################################################################3



