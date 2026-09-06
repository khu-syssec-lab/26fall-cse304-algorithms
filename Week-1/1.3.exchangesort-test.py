import sys
import importlib.util

# 동적으로 import
module_name = "exchangesort"



# 테스트 케이스 정의
test_cases = [
    {"S": [10, 7, 11, 5, 13, 8], "expected": [5, 7, 8, 10, 11, 13], "desc": "일반적인 배열"},
    {"S": [], "expected": [], "desc": "빈 배열"},
    {"S": [100], "expected": [100], "desc": "배열 크기 1"},
    {"S": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5], "desc": "역순 정렬된 배열"},
    {"S": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5], "desc": "이미 정렬된 배열"},
    {"S": [3, 1, 2, 3, 2, 1], "expected": [1, 1, 2, 2, 3, 3], "desc": "중복값 포함"},
    {"S": [0, -1, -5, 3, 2, -2], "expected": [-5, -2, -1, 0, 2, 3], "desc": "음수 포함"},
    {"S": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "desc": "역순 정렬된 긴 배열"},
    {"S": [5] * 100, "expected": [5] * 100, "desc": "같은 숫자가 100개 있는 경우"},
    {"S": list(range(100, 0, -1)), "expected": list(range(1, 101)), "desc": "100부터 1까지 내림차순"},
]

def run_test_cases(file_path = "1.3.exchangesort.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    exchangesort_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(exchangesort_module)

    exchangesort = exchangesort_module.exchangesort
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        S, expected, desc = case["S"], case["expected"], case["desc"]
        print(f"\033[1m Example {i}: {desc}\033[0m")  
        print(f"입력 배열: {S}")
        exchangesort(len(S), S)
        
        # 결과 검증
        if S == expected:
            print(f"정렬된 배열: {S} ✅ Passed")
            passed += 1
        else:
            print(f"정렬된 배열: {S} ❌ Failed (Expected: {expected}, Got: {S})")

        print(f"{'-'*20}\n")

    # 최종 테스트 결과 요약
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()