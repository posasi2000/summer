 %c -> 문자열 하나로 입력 필요시 사용
 %s -> 문자열 표현할때 사용
 %d -> 정수
 %f -> 실수   %.2f  %(데이터)


   자료형(type)
    - 데이터의 형태
    - 파이썬 자료형
        1) 숫자형
            정수형 : int (소숫점 X)   나이, 버스번호 
            실수형 : float (소숫점 O)  평균, 원주율, 환율
        2) 문자형 : str
            - 싱따옴표 혹은 쌍따옴표로 감싼 데이터
            - string (문자열)
        3) 논리형 : bool
            - 참 혹은 거짓  성별,flag깃발
            - True / False (대소문자 조심할 것!)
            - boolean


a = 3.14
# 각 데이터의 자료형 알려줘! : type(값 혹은 식)
print(type(a))  # <class 'float'>

    < 제어문자 (Escape Sequence) >
    : (출력 커서를) 제어하는 문자.

    \n : new line (줄바꿈 = enter)  제일많이 사용
    \t : tab
    \b : back space

print('AAAA\nBBBB')
print('A\tB\tC')
print('AAAA\bBBBB\bCCCC')
print('C:\\Users\\hong\\naconda\\test')


    제어문
        1. 조건문 (conditional statement): if문
        2. 반복문 (loop statement) : while문, for문
        3. 분기문 (braching statement) : break, continue, return, pass

    break
        - 자신이 속한 반복문을 완전히 종료한다.

    continue
        - 자신이 속한 반복문의 남아있던 종속문장을 1회만 건너뛴다.

        #단순if
        if 조건식:
            수행할문장1
        else:
            수행할문장2


        # 다중 if문임
        if 조건식1:
            실행할문장1
        elif 조건식2:
            실행할문장2
        else:
            실행할문장3



  리스트 :
        - 1개 이상의 원소로 이루어진 서랍장 역할을 하는 메모리
        - []
        - 목적 : 대량의 데이터를 일괄 처리(반복 처리)
            예) 학생 100명의 이름을 저장
                1. 변수 100개를 사용 --> 손 아픔
                2. 변수 1개 + for문 --> 덮어씀
                3. 100칸 리스트 생성 + for문
        - 관련 용어
            1) 원소 (element; 요소)
                : 리스트에 담겨있는 알맹이 데이터들
            2) 인덱스 (index)
                : 각 칸의 `번호`. 정수형. 0번부터 시작한다.

            [-4]  [-3]  [-2]  [-1] <-- 음의 인덱스 (-0은 없다)
            [0]   [1]   [2]   [3]  <-- 인덱스
            100   200   300   400  <-- 원소

        - 주의사항
            1. 처음 생성된 리스트의 크기는 변경 불가
            2. 원소는 인덱스를 통해 접근한다.
                리스트명[인덱스]


5월17일 화요일학습 
# 반복문 - for/while, 
  보조제어문 - break/continue/pass/return
# 예외처리 - try ~ except Exception as ex:
# 함수구현기술하면 반드시 호출해야함
  def bank(): 함수구현
    
5월17일 화요일오후
 ㄴ연산 관계,대입연산
 ㄴ리스트 [] 나열
 ㄴ함수


1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25
26  27  28  29  30


5월18일 수요일 수업
ㄴ리스트, 튜플, set, dict딕트=딕션
ㄴ난수사용 random, 로또