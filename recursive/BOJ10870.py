import sys

def fibonnachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnachi(n - 1) +
fibonnachi(n - 2)

n = int(sys.stdin.readline())
print(fibonnachi(n))