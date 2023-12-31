def hanoi(N, start, end):
    if N == 1:
        print(start, end)
        return
    
    remain = 6 - (start + end)
    hanoi(N - 1, start, remain)
    print(start, end)
    hanoi(N - 1, remain, end)
    
N = int(input())
print(2 ** N - 1) # K
hanoi(N, 1, 3)