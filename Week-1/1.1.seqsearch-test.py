import sys
import importlib.util

# 동적으로 import
module_name = "seqsearch"


# 테스트 케이스 정의 
test_cases = [
    {"S": [10, 7, 11, 5, 13, 8], "x": 10, "expected": 0, "desc": "Best Case (첫 번째 원소)"},
    {"S": [10, 7, 11, 5, 13, 8], "x": 6, "expected": -1, "desc": "Worst Case (배열에 없음)"},
    {"S": [10, 7, 11, 5, 13, 8], "x": 5, "expected": 3, "desc": "중간 위치 찾기"},
    {"S": [], "x": 5, "expected": -1, "desc": "Edge Case (빈 배열)"},
    {"S": [3], "x": 3, "expected": 0, "desc": "Edge Case (배열 크기 1, 존재하는 값)"},
    {"S": [3], "x": 5, "expected": -1, "desc": "Edge Case (배열 크기 1, 없는 값)"},
    {"S": [4, 2, 9, 7, 5], "x": 5, "expected": 4, "desc": "Edge Case (마지막 원소 찾기)"},
    {"S": [1, 2, 2, 2, 3, 4, 5], "x": 2, "expected": 1, "desc": "Duplicate Case (여러 개 존재)"},
    {"S": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "x": 7, "expected": 6, "desc": "중간 원소 찾기"},
    {"S": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "x": 11, "expected": -1, "desc": "배열에 없는 값 찾기"}
]

def run_test_cases(file_path = "1.1.seqsearch.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    seqsearch_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(seqsearch_module)

    seqsearch = seqsearch_module.seqsearch
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        S, x, expected, desc = case["S"], case["x"], case["expected"], case["desc"]
        print(f"\033[1m Example {i}: {desc}\033[0m")  
        print(f"S = {S}")
        print(f"x = {x}")
        location = seqsearch(len(S), S, x)
        
        # 결과 검증
        if location == expected:
            print(f"출력: {location} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {location} ❌ Failed (Expected: {expected}, Got: {location})")

        print(f"{'-'*20}\n")

    # 최종 테스트 결과 요약
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()