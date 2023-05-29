import os
from tokenize import String
from Blank_Fill.pdftotext_pdfminer import extract_text_pages
from typing import List
from konlpy.tag import Okt

Okt = Okt()

def makeBlanks(Text_based_PDF: List[int], dict_list: List[int]) -> List[str]:
    """
    입력한 PDF 파일에서 명사를 빈칸으로 변경하여 반환.

    Args:
        pdf_path (str): 빈칸으로 변경할 PDF 파일 경로
        dict_list (List[int]): 빈칸으로 변경할 문장의 인덱스 번호와 빈칸 갯수를 담은 리스트

    Returns:
        List[str]: 빈칸으로 변경한 문장을 담은 리스트
    """
    try:    
        writeLine = Text_based_PDF.copy()

        for i in range(len(dict_list)):
            line = writeLine[i] # 한줄 씩 읽어 옴
            if not line: break # 파일 끝 까지 반복

            if dict_list[i] == 0: 
                continue #명사 없을 경우 pass

            line = line.replace(dict_list[i], '( )')
            writeLine[i] = line

        return writeLine
    except:
            print('error')