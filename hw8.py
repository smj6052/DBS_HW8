import pymysql

# MySQL Connection 연결
conn=pymysql.connect(host='192.168.56.3', port=4567, user='mjseo',
                    password='****', db='madang', charset='utf8')

# Connection으로부터 Cursor 생성
curs=conn.cursor()

while True:
    # 사용자에게 입력받기
    ans=int(input("[추가:1, 삭제:2, 검색:3, 종료 : 0] 입력 : "))
    if(ans==1):     # 추가할 책의 정보를 입력 -> 추가
        insert_id=int(input("Enter the bookid : "))
        insert_bookname=input("Enter the bookname : ")
        insert_publisher=input("Enter the publisher : ")
        insert_price=int(input("Enter the price : "))
        insert=(insert_id,insert_bookname,insert_publisher,insert_price)
        # SQL문 실행
        addBook="insert into Book (bookid, bookname, publisher, price) values(%s,%s,%s,%s)"
        curs.execute(addBook,insert)
        conn.commit()
    elif(ans==2):   # 삭제할 책의 이름을 입력 -> 삭제
        remove=input("Enter the bookname : ")
        # SQL문 실행
        delBook="delete from Book where bookname=%s"  
        curs.execute(delBook,remove)
        conn.commit()   
    elif(ans==3):   # 검색할 책의 이름을 입력(일부 단어도 가능) -> 검색 
        retrieve=input("Enter the bookname : ")
        # SQL문 실행
        getBook="select * from Book where bookname like %s order by bookname"
        curs.execute(getBook,"%{}%".format(retrieve))   # .format 함수를 이용하여 해당 단어를 포함한 것을 검색
        # 데이터 Fetch
        rows=curs.fetchall()
        print(rows)     # 전체 rows
    elif(ans==0):   # 종료
        break
    else:
        print('잘못입력하셨습니다.')

# Connection 닫기
conn.close()


