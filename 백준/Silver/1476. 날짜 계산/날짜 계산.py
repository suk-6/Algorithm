E, S, M = map(int, input().split())
N = 1

while 1:
    if ((N-E) % 15 == 0) and ((N-S) % 28 == 0) and ((N-M) % 19 == 0):
        break 
    N += 1

print(N)