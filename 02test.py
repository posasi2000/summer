def  myData(*param):
    total = 0
    for k in param:
        total = total + k
    return total


a = myData(1,2,3,4,5)
print('총합계 =', a)
b = myData(15, 4)
print('총합계 =', b)
c = myData(1,2,3)
print('총합계 =', c)


#d = myData(1,2,'c','d',5)
#print('총합계 =', d)



'''
파이썬은 함수중복이 허용되지 않습니다
같은이름 허용하지 않습니다 
#함수 def  myData():
#함수 def  myData(23):
#함수 def  myData('kim', 23):
#함수 def  myData('kim', 23, True):
def  myData(kor,eng,math,com,sci):
    total = kor+eng+math+com+sci
    return total

def  myData(x,y):
    total = x+y
    return total

def  myData(kor,eng,flag,disp,sci):
    total = kor+eng+sci
    return total

a = myData(1,2,3,4,5)
print('총합계 =', a)
b = myData(15, 4)
print('총합계 =', b)
c = myData(1,2,'c','d',5)
print('총합계 =', c)
'''