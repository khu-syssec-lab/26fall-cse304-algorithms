import importlib.util

module_name = "knapsack_branchbound"

# Test cases: each with n, W, w[], p[], expected max profit, and description
test_cases = [
    {"n": 0, "W": 50.0, "w": [], "p": [], "expected": 0.0, "desc": "no items"},
    {"n": 3, "W": 0.0, "w": [10, 20, 30], "p": [60, 100, 120], "expected": 0.0, "desc": "zero capacity"},
    {"n": 1, "W": 50.0, "w": [50], "p": [100], "expected": 100.0, "desc": "single exact fit"},
    {"n": 1, "W": 50.0, "w": [60], "p": [120], "expected": 0.0, "desc": "single item too heavy"},
    {"n": 3, "W": 50.0, "w": [10, 20, 30], "p": [60, 100, 120], "expected": 220.0, "desc": "classic example from textbooks"},
    {"n": 4, "W": 10.0, "w": [5, 4, 6, 3], "p": [10, 40, 30, 50], "expected": 90.0, "desc": "optimal is item 2 + 4"},
    {"n": 2, "W": 5.0, "w": [6, 7], "p": [50, 60], "expected": 0.0, "desc": "all items too heavy"},
    {"n": 5, "W": 15.0, "w": [12, 2, 1, 1, 4], "p": [4, 2, 2, 1, 10], "expected": 15.0, "desc": "combination of multiple small items"},
    {"n": 3, "W": 60.0, "w": [10, 20, 30], "p": [60, 100, 120], "expected": 280.0, "desc": "total weight equals capacity"},
    {"n": 3, "W": 100.0, "w": [10, 20, 30], "p": [60, 100, 120], "expected": 280.0, "desc": "capacity exceeds total weight"}
]

def run_test_cases(file_path="5.7.knapsack.0-1.bt.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    ks_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ks_module)

    knapsack = ks_module.knapsack
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        print(f"\033[1mExample {i}: {case['desc']}\033[0m")

        ks_module.n = case["n"]
        ks_module.W = case["W"]
        ks_module.w = [0] + case["w"]  # 1-based
        ks_module.p = [0] + case["p"]
        ks_module.maxprofit = 0.0
        ks_module.include = [0] * (ks_module.n + 1)
        ks_module.bestset = [0] * (ks_module.n + 1)

        knapsack(0, 0.0, 0.0)

        result = ks_module.maxprofit
        expected = case["expected"]
        print(f"Max profit: {result}")

        if abs(result - expected) < 1e-6:
            print("출력: ✅ Passed")
            passed += 1
        else:
            print(f"출력: ❌ Failed (Expected: {expected}, Got: {result})")

        print("-" * 30 + "\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == '__main__':
    run_test_cases()