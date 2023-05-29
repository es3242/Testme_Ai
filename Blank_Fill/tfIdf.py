from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from Blank_Fill.nounExtractor import extract_nouns_list
from Blank_Fill.blankMaker import makeBlanks 

def tf_idf(Text_based_PDF):
    documents = extract_nouns_list(Text_based_PDF)
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(documents)

    tf = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    df = tf.astype(bool).sum(axis=0)
    D = len(tf)

    # Inverse Document Frequency - IDF 계산
    idf = np.log((D + 1) / (df + 1)) + 1
    # TF-IDF
    tfidf = (tf * idf) / np.linalg.norm((tf * idf), axis=1, keepdims=True)

    return tfidf

def make_test(Text_based_PDF):
    #답(중요 키워드) 
    solutions = list(tf_idf(Text_based_PDF).idxmax(axis=1).fillna(0))

    #빈칸 생성
    Test = makeBlanks(Text_based_PDF, solutions)

    return Test,solutions