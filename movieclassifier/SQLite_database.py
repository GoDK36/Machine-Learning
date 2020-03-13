import sqlite3

conn = sqlite3.connect('reviews.sqlite')  ##sqlite database에 연결하기
c = conn.cursor()  ##커서 생성을 하여 다양한 sql 문법으로 데이터베이스 레코드 조작
c.execute('DROP TABLE IF EXISTS review_db')  ##데이터베이스 테이블 review_db 생성
c.execute('CREATE TABLE review_db'\
            ' (review TEXT, sentiment INTEGER, date TEXT)')

example1 = 'I love this movie'
c.execute("INSERT INTO review_db"\
            " (review, sentiment, date) VALUES"\
            " (?, ?, DATETIME('now'))", (example1, 1))  ##3개의 칼럼(review, sentiment, date) 생성 / 긍정
example2 = 'I disliked this movie'
c.execute("INSERT INTO review_db"\
            " (review, sentiment, date) VALUES"\
            " (?, ?, DATETIME('now'))", (example2, 0))  ##부정 / DATETIME('now')는 레코드 컬럼에 날짜와 시간을 추가

conn.commit()
conn.close()


######데이터 베이스 확인하기######

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()
c.execute("SELECT * FROM review_db WHERE date"\
            " BETWEEN '2017-01-01 00:00:00' AND DATETIME('now')")  ##2017년부터 오늘까지 테이블에 추가된 모든 row 추출하기
results = c.fetchall()

conn.close()
print(results)