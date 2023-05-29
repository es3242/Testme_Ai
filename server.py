from flask import Flask, jsonify, request
from Blank_Fill.tfIdf import make_test
from Multiple_Choice.multiple_choice import make_mutiple_choice_Test

app = Flask(__name__)

@app.route('/Blank_Fill', methods=['POST']) #/Blank_Fill에 'POST'로 접근하면 다음 get_answer을 실행함
def get_blank_fill_answer():
    try:
        # 클라이언트로부터 전송된 JSON 데이터 수신
        data = request.get_json()
        Text_based_PDF = data['Text_based_PDF']
        Pages = len(Text_based_PDF)

        #데이터 처리~~
        Test,Solutions = make_test(Text_based_PDF)


        # 처리된 응답 생성
        response = {'Questions Amount' : Pages,
                    'Test': Test,
                    'Solutions' : Solutions}
        return jsonify(response)

    except Exception as ex:
        # 예외 처리
        print(ex)
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/MultipleChoice', methods=['POST']) #/Blank_Fill에 'POST'로 접근하면 다음 get_answer을 실행함
def get_multiple_choice_answer():
    try:
        # 클라이언트로부터 전송된 JSON 데이터 수신
        data = request.get_json()
        Pages = data['Pages']
        Text_based_PDF = data['Text_based_PDF']
        Questions_Amount = data['Questions_Amount']

        #데이터 처리~~
        Test = make_mutiple_choice_Test(Text_based_PDF,Questions_Amount)
        #테스트 파싱 작업 필요. 테스트용으로 Test전체를 보내게 함

        # 처리된 응답 생성
        response = {'Test': Test}
        return jsonify(response)

    except Exception as ex:
        # 예외 처리
        print(ex)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)