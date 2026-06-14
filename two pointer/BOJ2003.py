n, m = map(int, input().split())
num_list = list(map(int, input().split()))
answer = 0
start = 0
end = 0
sum = num_list[0] if n > 0 else 0
while True:

    if sum == m: 
        answer += 1
    if sum <= m:
        end += 1
        if end == n:  
            break
        sum += num_list[end]
    
    else:
        sum -= num_list[start]
        start += 1

print(answer)