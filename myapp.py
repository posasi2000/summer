
class MyApp:
    name=''; city='';   count = 3600 #전역변수=class변수

    def __init__(self, kind):
        print('MyApp클래스 __init__() 생성자')
        print(kind , '관련 공모전')

    def saveMenu(self):
        name=input('이름입력>>> ')
        city=input('주소입력>>> ')
        print(name, city)

    def printCount(self):
        #count = 123 #지역변수 
        #print('지역count =', count) #123출력
        print('전역count =', self.count) #3600


    @staticmethod
    def isSquare( w, h):
        area = w * h
        #print('전역count =', self.count) #3600
        return area


#문제1 isSquare()함수호출 
#val = MyApp.isSquare(7, 7) 비권장

my = MyApp('빅데이터') #객체화
val = my.isSquare(8, 8)
print('사각형넓이 =', val)