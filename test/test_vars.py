import argparse
from argparse import Namespace

print("=== vars() 함수 동작 이해하기 ===")

# 1. Namespace 객체 생성
parser = argparse.ArgumentParser()
parser.add_argument("--name", default="홍길동")
parser.add_argument("--age", type=int, default=25)
args = parser.parse_args([])

print(f"1. 원본 args (Namespace): {args}")
print(f"   타입: {type(args)}")
print(f"   속성 접근: args.name = {args.name}")

# 2. vars()로 딕셔너리 변환
args_dict = vars(args)
print(f"\n2. vars(args) 결과: {args_dict}")
print(f"   타입: {type(args_dict)}")
print(f"   키 접근: args_dict['name'] = {args_dict['name']}")

# 3. 중요한 점: 같은 메모리 공유!
print(f"\n3. 메모리 공유 확인:")
print(f"   변환 전 id: {id(args.__dict__)}")
print(f"   변환 후 id: {id(args_dict)}")
print(f"   같은 객체? {args.__dict__ is args_dict}")

# 4. 한쪽을 수정하면 다른 쪽도 변경됨
args_dict["name"] = "김철수"
print(f"\n4. args_dict 수정 후:")
print(f"   args.name: {args.name}")
print(f"   args_dict['name']: {args_dict['name']}")
