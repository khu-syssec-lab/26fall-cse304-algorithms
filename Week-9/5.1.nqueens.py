from typing import List

def promising(i: int, n: int, col: List[int]) -> bool:
    is_promising = True
    # Complete the code here

    return is_promising

def nqueens(i: int, n: int, col: List[int]) -> None:
    if promising(i, n, col):
        if i == n:
            print("found=", col[1:])
        else:
            # Complete the code here
