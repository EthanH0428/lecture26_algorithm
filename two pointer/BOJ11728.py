import sys

input = sys.stdin.readline

n = map(int, input().split())
m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p1, p2 = 0, 0
result = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        result.append(a[p1])
        p1 += 1
    else:
        result.append(b[p2])
        p2 += 1


result.extend(a[p1:])
result.extend(b[p2:])

print(*(result))