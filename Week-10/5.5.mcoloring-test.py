import importlib.util
from typing import List, Dict

module_name = "map_coloring"

# Each test case defines: number of nodes (n), number of colors (m), adjacency matrix (W), expected count, and description
test_cases: List[Dict] = [
    {
        "n": 0, "m": 3, "W": [], "expected": 0,
        "desc": "empty graph"
    },
    {
        "n": 1, "m": 1, "W": [[0]], "expected": 1,
        "desc": "single node, one color"
    },
    {
        "n": 2, "m": 1, "W": [[0, 1], [1, 0]], "expected": 0,
        "desc": "two connected nodes, one color"
    },
    {
        "n": 2, "m": 2, "W": [[0, 1], [1, 0]], "expected": 2,
        "desc": "two connected nodes, two colors"
    },
    {
        "n": 3, "m": 3, "W": [[0,1,1],[1,0,1],[1,1,0]], "expected": 6,
        "desc": "triangle, 3 colors"
    },
    {
        "n": 3, "m": 2, "W": [[0,1,1],[1,0,1],[1,1,0]], "expected": 0,
        "desc": "triangle, 2 colors (impossible)"
    },
    {
        "n": 4, "m": 3, "W": [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]], "expected": 18,
        "desc": "square (cycle of 4), 3 colors"
    },
    {
        "n": 5, "m": 3, "W": [[0,1,1,0,0],[1,0,1,1,0],[1,1,0,1,1],[0,1,1,0,1],[0,0,1,1,0]], "expected": 6,
        "desc": "complex graph of 5 nodes, 3 colors"
    },
    {
        "n": 4, "m": 4, "W": [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], "expected": 24,
        "desc": "fully connected 4 nodes (K4), 4 colors"
    },
    {
        "n": 4, "m": 3, "W": [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], "expected": 0,
        "desc": "fully connected 4 nodes (K4), 3 colors (impossible)"
    }
]

def pad_adjacency_matrix(W: List[List[int]], n: int) -> List[List[int]]:
    """Pads the adjacency matrix to be 1-indexed for the tested algorithm"""
    padded = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            padded[i + 1][j + 1] = W[i][j]
    return padded

def run_test_cases(file_path = "5.5.mcoloring.py"):
    # Load module
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    coloring_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(coloring_module)

    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n = case["n"]
        m = case["m"]
        W = case["W"]
        expected = case["expected"]
        desc = case["desc"]

        # Initialize global variables
        coloring_module.n = n
        coloring_module.count = 0
        coloring_module.W = pad_adjacency_matrix(W, n)
        coloring_module.vcolor = [0] * (n + 1)

        print(f"\033[1mExample {i}: {desc}\033[0m")
        if n > 0:
            coloring_module.mcoloring(0, m)
        result = coloring_module.count
        print(f"Valid colorings: {result}")

        if result == expected:
            print("출력: ✅ Passed")
            passed += 1
        else:
            print(f"출력: ❌ Failed (Expected: {expected}, Got: {result})")
        print("-" * 30 + "\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == '__main__':
    run_test_cases()