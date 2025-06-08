print("=== vars() 함수 완전 분석 ===")

# 1. vars()가 내장 함수인지 확인
print(f"1. vars 함수 정보:")
print(f"   타입: {type(vars)}")
print(f"   모듈: {vars.__module__}")
print(f"   설명: {vars.__doc__}")

# 2. 내장 함수 목록에서 확인
import builtins

builtin_functions = dir(builtins)
print(f"\n2. 내장 함수인가? {'vars' in builtin_functions}")

# 3. vars() 함수의 다양한 사용법
print(f"\n3. vars() 함수 사용법들:")

# 3-1. 인수 없이 호출 (현재 로컬 변수들)
name = "홍길동"
age = 25
local_vars = vars()
print(f"   로컬 변수들: {[k for k in local_vars.keys() if not k.startswith('_')]}")


# 3-2. 객체의 속성 딕셔너리 반환
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("김철수", 30)
print(f"   person 객체: {vars(person)}")

# 3-3. 모듈의 속성들
import os

os_vars = vars(os)
print(f"   os 모듈 속성 개수: {len(os_vars)}")
print(f"   os 모듈 일부 속성: {list(os_vars.keys())[:5]}")

# 4. vars()와 __dict__의 관계
print(f"\n4. vars()와 __dict__ 비교:")
print(f"   vars(person): {vars(person)}")
print(f"   person.__dict__: {person.__dict__}")
print(f"   같은 객체? {vars(person) is person.__dict__}")

# 5. ArgumentParser Namespace와 vars()
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", default="값")
args = parser.parse_args([])

print(f"\n5. Namespace와 vars():")
print(f"   args: {args}")
print(f"   vars(args): {vars(args)}")
print(f"   args.__dict__: {args.__dict__}")
print(f"   모두 같은 객체? {vars(args) is args.__dict__}")
