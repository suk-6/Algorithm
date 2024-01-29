T = int(input())

for _ in range(T):
    input()
    N = int(input())
    count = sum([int(input()) for _ in range(N)])
    
    if count % N == 0:
        print("YES")
    else:
        print("NO")