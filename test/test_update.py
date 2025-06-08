import argparse
from argparse import Namespace

print("=== 설정 병합과 확장 과정 ===")

# 1. 기본 설정
parser = argparse.ArgumentParser()
parser.add_argument("--name", default="홍길동")
parser.add_argument("--age", type=int, default=25)
args = parser.parse_args([])

print(f"1. 초기 args: {args}")

# 2. Namespace → 딕셔너리 변환
args_dict = vars(args)
print(f"2. 딕셔너리 변환: {args_dict}")

# 3. 추가 설정 정의
extra_config = {"job": "개발자", "age": 30}  # age는 덮어쓰기됨
print(f"3. 추가 설정: {extra_config}")

# 4. 병합 전후 비교
print(f"\n4. 병합 과정:")
print(f"   병합 전: {args_dict}")
args_dict.update(extra_config)  # 핵심!
print(f"   병합 후: {args_dict}")

# 5. 변경사항 확인
print(f"\n5. 변경사항:")
print(f"   name: 그대로 '{args_dict['name']}'")
print(f"   age: 25 → {args_dict['age']} (덮어쓰기)")
print(f"   job: 새로 추가 '{args_dict['job']}'")

# 6. 원본 Namespace도 변경됨 (메모리 공유)
print(f"\n6. 원본 Namespace 변경 확인:")
print(f"   args.age: {args.age} (자동 업데이트)")
print(f"   args.job: {getattr(args, 'job', '속성 없음')}")  # 새 속성은 직접 접근 안됨

# 7. 다시 Namespace로 변환하는 이유
final_args = Namespace(**args_dict)
print(f"\n7. 최종 Namespace 재생성:")
print(f"   final_args: {final_args}")
print(f"   final_args.job: {final_args.job}")  # 이제 속성으로 접근 가능
