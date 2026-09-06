import sys
import importlib.util

# 동적으로 import
module_name = "arrsum"


# 테스트 케이스 정의
test_cases = [
    {"S": [10, 7, 11, 5, 13, 8], "expected": 54, "desc": "일반적인 배열"},
    {"S": [], "expected": 0, "desc": "빈 배열"},
    {"S": [100], "expected": 100, "desc": "배열 크기 1"},
    {"S": [-1, -2, -3, -4], "expected": -10, "desc": "음수 포함"},
    {"S": [1, -1, 2, -2, 3, -3], "expected": 0, "desc": "양수와 음수가 합쳐진 경우"},
    {"S": [1000000, 2000000, 3000000], "expected": 6000000, "desc": "큰 수 포함"},
    {"S": list(range(100)), "expected": sum(range(100)), "desc": "0부터 99까지 합"},
    {"S": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "expected": 55, "desc": "1부터 10까지 합"},
    {"S": [5] * 100, "expected": 500, "desc": "같은 숫자가 100개 있는 경우"},
    {"S": [-1000, 500, 200, -300, 400, -500, 600, -700, 800, -900], "expected": -900, "desc": "양수와 음수가 섞인 경우"},
]

def run_test_cases(file_path = "1.2.arrsum.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    arrsum_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(arrsum_module)

    arrsum = arrsum_module.arrsum
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        S, expected, desc = case["S"], case["expected"], case["desc"]
        print(f"\033[1m Example {i}: {desc}\033[0m")  
        print(f"S = {S}")
        result = arrsum(len(S), S)
        
        # 결과 검증
        if result == expected:
            print(f"출력: {result} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {result} ❌ Failed (Expected: {expected}, Got: {result})")

        print(f"{'-'*20}\n")

    # 최종 테스트 결과 요약
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()