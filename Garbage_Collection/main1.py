# 예시 1: 참조 카운팅
# 클래스 정의
class MyClass:
    def __init__(self, name):
        self.name = name

# 객체 생성과 참조
obj1 = MyClass("Object 1")
obj2 = obj1  # obj2가 obj1을 참조

# 참조 카운트 확인
import sys
print(sys.getrefcount(obj1))  # 3 (obj1, obj2, getrefcount 함수의 임시 참조)

# 참조 해제
del obj1
print(sys.getrefcount(obj2))  # 2 (obj2, getrefcount 함수의 임시 참조)

# 가비지 컬렉션 실행
import gc
gc.collect()

# 출력: 1 (getrefcount 함수의 임시 참조만 남음)
print(sys.getrefcount(obj2))
#########################################################################
# 예시 2: 순환 참조 검사
# 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 객체 생성과 순환 참조
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1  # 순환 참조

