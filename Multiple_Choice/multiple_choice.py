import Multiple_Choice.openAI_settings as setting
import openai
import Multiple_Choice.make_prompt as make_prompt
import Multiple_Choice.tfIdf as tfidf


# ChatGPT API 호출 함수
def generate_response(prompt,model):
    # API 호출
    response = openai.Completion.create(
        model=model,  # 사용할 GPT 엔진 선택
        prompt=prompt,
        max_tokens=1024,  # 출력 텍스트의 최대 길이
        n=1,  # 생성할 텍스트 개수
        stop=None,  # 출력 텍스트 중지 조건
        temperature=0,  # 생성할 텍스트의 창의성과 일관성을 조절하는 옵션
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    # API 응답 반환
    return response

def make_mutiple_choice_Test(Text_based_PDF,Questions_Amount):
    if len(Text_based_PDF) < Questions_Amount:
        print('문제 수는 페이지 수 보다 적거나 같아야 합니다.')
    
    else:
        # OpenAI API Key 설정
        openai.organization = setting.organization
        openai.api_key = setting.api_key
        keyword_page_dict = tfidf.get_highest_tfidf_pages(tfidf.tf_idf(Text_based_PDF))[:Questions_Amount]
        Test = []
        for i in range(Questions_Amount):
            print("확인1")
            #문제 갯수 만큼 랜덤 추출로 수정-> 중요 문서로 수정
            prompt = make_prompt.make_prompt(Text_based_PDF[keyword_page_dict[i]['page_index']],keyword_page_dict[i]['word'])
            print("확인2")
            response = generate_response(prompt,setting.GPT_model)
            Test.append(response.choices[0].text.strip())
    return Test