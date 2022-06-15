class Info:
    total = 9800
    def __init__(self):
        print('Info클래스 __init__() 생성자')
        print('Info클래스  생성자 전역변수', self.total)
        print()

    def update(self, number):
        print('Info클래스 수정처리')
        print('수정숫자 =' , number)
        print('수정 전역변수 =' , self.total)
        print()

    def search(self):
        print('Info클래스 조회 C') 
        print('Info클래스 조회 D') 
        print('조회 전역변수 =' , self.total)

# Info.__init__(7)  #비권장문법 에러및실행중 에러없음
# Info.update(1234) #비권장 문법에러및실행중 에러없음
# Info.search() #비권장 문법에러및실행중 에러없음

my = Info()
my.update(12)
my.search()

