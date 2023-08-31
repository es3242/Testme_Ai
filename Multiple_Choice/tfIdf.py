from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import pandas as pd
import numpy as np
from Multiple_Choice.nounExtractor import extract_nouns_list
from Multiple_Choice.pdftotext_pdfminer import extract_text_pages 


import pandas as pd


def tf_idf(Text_based_PDF):
    documents = extract_nouns_list(Text_based_PDF)
    corpus = [' '.join(doc['nouns']) for doc in documents]
    pages = [doc['page'] for doc in documents]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    feature_names = vectorizer.get_feature_names_out()
    tfidf_array = tfidf_matrix.toarray()

    # TF-IDF 점수를 가진 DataFrame 생성
    tfidf = pd.DataFrame(tfidf_array, columns=feature_names)
    tfidf['page'] = pages

    # TF-IDF 점수를 기준으로 열(단어)을 내림차순 정렬
    sorted_cols = tfidf.iloc[:, :-1].mean().sort_values(ascending=False).index
    tfidf = tfidf[sorted_cols.tolist() + ['page']]

    return tfidf


def get_highest_tfidf_pages(tfidf_df):
    highest_tfidf_pages = []

    for column in tfidf_df.columns[:-1]:
        max_page_index = tfidf_df[column].idxmax()
        word = column
        page = tfidf_df.loc[max_page_index, 'page']

        highest_tfidf_pages.append({'word': word, 'page_index': page})

    return highest_tfidf_pages
