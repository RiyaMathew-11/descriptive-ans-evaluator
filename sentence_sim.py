# Jaccard's similarity with preprocessing
import re
from nltk.corpus import stopwords


def preprocess(doc):
    # Remove all non-alphanumeric characters
    doc = re.sub(r'[^a-zA-Z0-9]', ' ', doc)
    # Convert to lowercase
    doc = doc.lower()
    # Remove all stop words
    doc = doc.split()
    doc = [word for word in doc if word not in stopwords.words('english')]
    # Join all words back together
    doc = ' '.join(doc)
    # Return preprocessed doc
    return doc


def Jaccard_Similarity(doc1, doc2):

    # List the unique words in a document
    words_doc1 = set(doc1.split())
    words_doc2 = set(doc2.split())

    # Find the intersection of words list of doc1 & doc2
    intersection = words_doc1.intersection(words_doc2)

    # Find the union of words list of doc1 & doc2
    union = words_doc1.union(words_doc2)

    # Calculate Jaccard similarity score
    return float(len(intersection)) / len(union)


def answer_score(index):
    if index >= 0.70:
        return 2
    
    elif 0.70 < index <= 0.5:
        return 1.5
    
    elif 0.5 < index <= 0.3:
        return 1
    
    elif 0.3 < index <= 0.1:
        return 0.5
    
    else:
        return 0

    
    