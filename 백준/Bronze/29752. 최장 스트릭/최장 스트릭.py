import sys
N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

maxs = 0

for i in range(N):
    tmp = 0
    if s[i] >= 1:
        tmp += 1
        for j in range(N - i - 1):
            if s[i + j + 1] >= 1:
                tmp += 1
            else:
                break
        if tmp > maxs:
            maxs = tmp
            
print(maxs)