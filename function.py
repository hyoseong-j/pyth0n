# 함수: 특정한 입력을 받아서 처리를 한 이후에, 특정한 출력을 하는 모듈
# 함수를 이용하면 특정한 소스코드의 반복을 줄일 수 있다는 특징

# def = define 정의한다



# 파이썬의 함수는 반환 값이 여러 개일 수 있음
def add():
    a = 5
    b = (1, 2, 3)
    return a,b
a, b = add()
print(a)

print(b)
print(add())

# 가변 인자: 함수의 매개변수가 가변적일 수 있을 떄 사용
# 전역 변수 : 소스코드 전체 어디에서든지 사용 가능한 변수
# 지역 변수: 특정한 함수(블록) 안에서만 사용할 수 있는 변수
'''
def add():
    global a
    a = a + 5 # 지역 변수

a = 2 # 전역 변수
add()
print(a)  #2


def function(*data):
    print(data)

function(1, 2 ,3)
'''


