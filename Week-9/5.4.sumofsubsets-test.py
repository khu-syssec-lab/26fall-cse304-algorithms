import sys
import importlib.util
from io import StringIO
import ast

# 모듈 이름과 테스트 케이스 정의
module_name = "sumofsubsets_algo"

# 각 예제에 대한 w, W, 그리고 기대하는 include 패턴 리스트
test_cases = [
    {   # 1) 단일 원소 [5], 목표합 5
        "w": [0, 5],
        "W": 5,
        "expected": [[1]],
        "desc": "단일 원소 [5], 목표합 5"
    },
    {   # 2) 단일 원소 [5], 목표합 3
        "w": [0, 5],
        "W": 3,
        "expected": [],
        "desc": "단일 원소 [5], 목표합 3"
    },
    {   # 3) [1,2,3], 목표합 5
        "w": [0, 1, 2, 3],
        "W": 5,
        "expected": [[0,1,1]],  # 2+3
        "desc": "[1,2,3], 목표합 5"
    },
    {   # 4) [2,3,5,6], 목표합 8
        "w": [0, 2, 3, 5, 6],
        "W": 8,
        "expected": [[0,1,1,0],[1,0,0,1]],
        "desc": "[2,3,5,6], 목표합 8"
    },
    {   # 5) 다섯 개 1, 목표합 3
        "w": [0, 1, 1, 1, 1, 1],
        "W": 3,
        "expected": [
            [1,1,1,0,0],[1,1,0,1,0],[1,1,0,0,1],[1,0,1,1,0],[1,0,1,0,1],
            [1,0,0,1,1],[0,1,1,1,0],[0,1,1,0,1],[0,1,0,1,1],[0,0,1,1,1]
        ],
        "desc": "다섯 개 1, 목표합 3"
    },
    {   # 6) [2,4,6,8,10], 목표합 10
        "w": [0,2,4,6,8,10],
        "W": 10,
        "expected": [[0,0,0,0,1],[1,0,0,1,0],[0,1,1,0,0]],
        "desc": "[2,4,6,8,10], 목표합 10"
    },
        {   # 7) [0,2,3,4,5,12,34] 목표합 9
        "w": [0,2,3,4,5,12,34],
        "W": 9,
        "expected": [[1,1,1,0,0,0], [0,0,1,1,0,0]],  
        "desc": "[0,2,3,4,5,12,34], 목표합 9"
    },
    {   # 8) [1,2,3,5,7], 목표합 10
        "w": [0,1,2,3,5,7],
        "W": 10,
        "expected": [[1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 1]],
        "desc": "[1,2,3,5,7], 목표합 10"
    },
    {   # 9) [1,2,3,4,5], 목표합 5
        "w": [0,1,2,3,4,5],
        "W": 5,
        "expected": [[0,0,0,0,1],[1,0,0,1,0],[0,1,1,0,0]],
        "desc": "[1,2,3,4,5], 목표합 5"
    },
    {   # 10) [1,2,3,4,5], 목표합 12
        "w": [0,1,2,3,4,5],
        "W": 12,
        "expected": [[0,0,1,1,1],[1,1,0,1,1]],
        "desc": "[1,2,3,4,5], 목표합 12"
    }
]

def run_test_cases(file_path='5.4.sumofsubsets.py'):
    # 모듈 로드
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    subset_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(subset_module)
    sumofsubsets = subset_module.sumofsubsets

    passed = 0
    total  = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        w = case['w']
        W = case['W']
        expected = case['expected']
        desc = case['desc']
        n = len(w) - 1

        # 글로벌 변수 세팅
        subset_module.n       = n
        subset_module.W       = W
        subset_module.w       = w
        subset_module.include = [0] * (n + 1)

        print(f"\033[1mExample {i}: {desc}\033[0m")
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        total_weight = sum(w[1:])
        sumofsubsets(0, 0, total_weight)
        output = sys.stdout.getvalue().strip().splitlines()
        sys.stdout = old_stdout

        # found: 이후 include 리스트 파싱
        actual = []
        for line in output:
            if line.startswith('found:'):
                pat = line.split(':',1)[1].strip()
                actual.append(ast.literal_eval(pat))

        actual_set   = set(tuple(x) for x in actual)
        expected_set = set(tuple(x) for x in expected)

        if actual_set == expected_set:
            print(f"✅ Passed: {len(actual)} solutions matched expected")
            passed += 1
        else:
            print(f"❌ Failed: expected {len(expected)} solutions, got {len(actual)}")
            print(f" Expected: {expected}")
            print(f" Got: {actual}")
        print('-'*20 + '\n')

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == '__main__':
    run_test_cases()
