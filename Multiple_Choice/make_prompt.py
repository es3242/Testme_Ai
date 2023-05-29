def make_prompt(page,keyword):
    prompt = f"{page}'\n\n'+위의 지문에서 '{keyword}' 라는 키워드를 활용해서\
    4지 선다 객관식 문제를 만들어 줘.\
    답변은 다음과 같은 json형식으로 해줘.\n\n \
    {{'question' : {{문제}}, 'd1' : {{1번 선택지}},\
    'd2' : {{2번 선택지}}, 'd3' : {{3번 선택지}},\
    'd4' : {{4번 선택지}}, 'solution' : {{정답 선택지 번호 1~4}} }}"

    return prompt