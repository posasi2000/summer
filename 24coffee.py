'''
 coffee
문) 다음과 같이 아메리카노 3잔만 제공하는 커피 자판기 프로그램을 구현
     (커피 한 잔은 2500원이라고 가정한다.)
     조건1> 2500원 미만, 금액이 부족합니다. 반복 수행
     조건2> 2500원 이상, 맛있게 드세요. 잔돈 표시, 커피 잔 빼기
     조건3> 2500원 이면, 맛있게 드세오. 커피 잔 빼기
     조건4> 커피 3잔을 모두 판매하면 프로그램 종료
'''

print('- ' * 30)   
print('아메리카노 커피 자판기 동작')
print('가격은 2,500원')
print('커피는 3잔만 판매 가능')
print('- ' * 30)   

cnt = 3
while True :
    price = int(input("자판기 투입 금액>>> "))

    if price < 2500 :
        print("금액이 부족합니다.")
    elif price == 2500 :
        print("맛있게 드세요.")
        cnt  = cnt - 1
    elif price > 2500 :
        print("맛있게 드세요.")
        cnt -= 1
        price = price - 2500
        print("잔액은 %d입니다"%(price))
        #print("잔액은 {}입니다".format(price))
        #print(f"잔액은 {price}입니다")

    # 종료조건
    if cnt == 0 :
        print("커피가 소진되었습니다. 오늘 장사 끝!")
        break



    
    