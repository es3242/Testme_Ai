from konlpy.tag import Okt
from Multiple_Choice.pdftotext_pdfminer import extract_text_pages

okt = Okt()

def extract_nouns_list(Text_based_PDF):
    nouns_list = []
    for idx, page in enumerate(Text_based_PDF, start=0):
        nouns = okt.nouns(page)
        if not nouns:
            nouns_list.append({'page': idx, 'nouns': [], 'nouns_exist': False})
            continue
        nouns_list.append({'page': idx, 'nouns': nouns, 'nouns_exist': True})
    return nouns_list

def extract_verbs_list(file_path):
    arr = extract_text_pages(file_path)
    verbs_list = []
    for page in arr:
        temp = []
        tagging = okt.pos(page)
        if not tagging:
            temp.append(' ')
            continue
        for i, j in tagging:
            if j == 'Verb':
                temp.append(i)
        verbs_list.append(' '.join(str(verb) for verb in temp))
    print(verbs_list)
    return verbs_list

def extract_adjectives_list(file_path):
    arr = extract_text_pages(file_path)
    adjs_list = []
    for lines in arr:
        temp = []
        tagging = okt.pos(lines)
        if not tagging:
            temp.append(' ')
            continue
        for i, j in tagging:
            if j == 'Adjective':
                temp.append(i)
        adjs_list.append(' '.join(str(adj) for adj in temp))
    print(adjs_list)
    return adjs_list