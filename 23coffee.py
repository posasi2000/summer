#if,for,while,break,contine,형변환,출력포맷 {} %

money, sel = 0,0
money = int(input('금액입력>>> '))  #500입력 

while True:
    print('::::::::::::::::::커피자판기::::::::::::::::::::::::')
    print('1.커피(150)\t2.코코아(300)\t3.반환\t  9.종료')
    sel = int(input('메뉴번호 >>>'))
    if sel==9:
        print('초미니자판기프로그램을 종료합니다')
        break
    elif ((sel == 1 and money < 150) or ( sel == 2 and money< 300)):
        print("요금이 부족합니다")
        break
    elif sel==1:
        print('커피주문 성공입니다')
        money = money - 150
        print('잔액', money ,  '원 남았습니다')
    elif sel==2:
        print('코코아주문 성공입니다')
        money = money - 300
        print('잔액', money ,  '원 남았습니다')
    elif sel==3:
        print('잔액은', money ,'원입니다')
        break
    else:
        print('잘못된메뉴선택으로 자판기서비스 일시정지')
        break

print()

'''
 500원입력후 2번 코코아주문하면 안내메세지 코코아주문성공 잔액표시
 2번 코코아주문 누르면 잔액이 부족합니다
 1번 커피 누르면 커피주문성공  잔액표시 
 반복문while  if제어문 and/or조건, 형변환 
'''