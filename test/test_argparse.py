import argparse
import sys

print("=== ArgumentParser 명령행 인자 파싱 테스트 ===")
print(f"sys.argv: {sys.argv}")

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="기본이름")
parser.add_argument("--age", type=int, default=25)

print("\n1. 일반적인 방법 (명령행 인자 사용)")
try:
    args1 = parser.parse_args()  # 명령행 인자 자동 읽기
    print(f"결과: name={args1.name}, age={args1.age}")
except SystemExit as e:
    print(f"에러 발생: {e}")

print("\n2. Isaac Lab 방법 (빈 리스트)")
args2 = parser.parse_args([])  # 명령행 인자 무시
print(f"결과: name={args2.name}, age={args2.age}")

print("\n3. 수동으로 인자 제공")
args3 = parser.parse_args(["--name", "홍길동", "--age", "30"])
print(f"결과: name={args3.name}, age={args3.age}")
