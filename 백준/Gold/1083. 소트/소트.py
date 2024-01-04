N = int(input())
A = list(map(int, input().split()))
S = int(input())
idx = 0

for i in range(N):
    maxN = max(A[i : min(i + S + 1, N)])
    idx = A.index(maxN)

    for j in range(idx, i, -1):
        A[j], A[j - 1] = A[j - 1], A[j]

    S -= idx - i

    if S <= 0:
        break

print(" ".join(str(i) for i in A))