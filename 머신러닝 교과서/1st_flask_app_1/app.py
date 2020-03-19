from flask import Flask, render_template

app = Flask(__name__)  ##새로운 플라스크 인스턴스 초기화 => 현재 디렉토리 위치에서 html 템플릿 폴더 찾기
@app.route('/')  ##특정 URL이 index 함수를 실행하도록 지정
def index(): 
    return render_template('first_app.html') ##templates 폴더 아래에 있는  first_app.html 파일을 화면에 출력

if __name__ == '__main__':  ##스크립트가 파이썬 인터프리터에 의해 직접 실행될때만 실행되게 하는 코드
    app.run()