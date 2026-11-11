from typing import List

n: int
W: int
w: List[int]
include: List[int]

def promising(i: int, weight: int, total: int) -> bool:
    global n, W, w, include
    # Complete the code here

def sumofsubsets(i: int, weight: int, total: int) -> None:
    global n, W, w, include
    if promising(i, weight, total):
        if weight == W:
            print("found:", include[1:])
        else:
            # Complete the code here
