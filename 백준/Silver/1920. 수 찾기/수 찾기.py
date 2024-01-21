import sys

sys.stdin.readline()
A = sorted(list(map(int, sys.stdin.readline().split())))
sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))

for i in M:
    s, e = 0, len(A) - 1
    isExist = False
    
    while s <= e:
        mid = (s + e) // 2
        if i == A[mid]:
            isExist = True
            print(1)
            break
        elif i > A[mid]:
            s = mid + 1
        else:
            e = mid - 1
        
    if not isExist:
        print(0)