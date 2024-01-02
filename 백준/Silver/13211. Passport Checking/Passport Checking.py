s = {input(): 1 for _ in range(int(input()))}
print(sum([s.get(input(), 0) for _ in range(int(input()))]))