from typing import List
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

def extract_text(input_file: str) -> str:
    """
    PDF 파일에서 텍스트를 추출, 추출한 텍스트를 반환.
    """
    extracted_text = ''
    for page_layout in extract_pages(input_file):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                extracted_text += element.get_text()
    return extracted_text

def extract_text_pages(input_file: str) -> List[str]:
    """
    PDF 파일로부터 각 페이지마다 추출한 텍스트를 리스트로 반환.
    """
    extracted_text_pages = []
    for page_layout in extract_pages(input_file):
        page_text = ''
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                page_text += element.get_text()
        if page_text:
            extracted_text_pages.append(page_text)

    return extracted_text_pages



