# 모듈 가져오기
import ctypes
import gc

# 참조 카운팅
def count_references(id):
    return ctypes.c_long.from_address(id).value

# 가비지 컬렉션에서 객체 보기
def object_in_garbage(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "개체 가비지 컬렉션에 존재"
    return "객체 가비지 컬렉션에 존재 X"

# 순환 참조 생성
class A:
    def __init__(self):
        self.var_a = B(self)
        print("A: {0}, var_a: {1}".format(id(self), id(self.var_a)))

class B:
    def __init__(self, obj):
        self.var_b = obj
        print("B: {0}, var_b: {1}".format(id(self), id(self.var_b)))

# 가비지 수집 비활성화
gc.disable()

# 결과
print()
print("------------------------------")
print("주소:")
var = A()

# Storing id of object A and var_a
# 객체 A와 var_a의 id 저장
obj_a_id = id(var)
obj_b_id = id(var.var_a)


print()
print("------------------------------")
print('A:',obj_a_id)
print('B:', obj_b_id)

print()
print("------------------------------")
print("객체 A와 객체 B에 대한 참조 횟수 표시:")
ref_count_a = count_references(obj_a_id)
ref_count_b = count_references(obj_b_id)
print("A 참조 횟수: ", ref_count_a)
print("B 참조 횟수: ", ref_count_b)

# 수집 var
var = None

print()
print("------------------------------")
print("var 수집 후 A와 B 참조 횟수 표시")
ref_count_a = count_references(obj_a_id)
ref_count_b = count_references(obj_b_id)
print("A 참조 횟수: ", ref_count_a)
print("B 참조 횟수: ", ref_count_b)

# 객체 존재 확인
print()
print("가비지 수집 전")
print("------------------------------")
print(object_in_garbage(obj_a_id))
print(object_in_garbage(obj_b_id))

# 수동으로 가비지 수거
gc.collect()

# 수집 후 객체 확인
print()
print("------------------------------")
print("가비지 수집 후")
print(object_in_garbage(obj_a_id))
print(object_in_garbage(obj_b_id))

print()
print("------------------------------")
print("수집후 객체 A와 B에 대한 참조 횟수 표시")
ref_count_a = count_references(obj_a_id)
ref_count_b = count_references(obj_b_id)
print("A 참조 횟수: ", ref_count_a)
print("B 참조 횟수: ", ref_count_b)

# 가비지 컬렉터 활상화
gc.enable()