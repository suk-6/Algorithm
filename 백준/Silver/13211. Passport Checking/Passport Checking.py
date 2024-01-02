stolen = {input(): 1 for _ in range(int(input()))}
print(sum([stolen.get(input(), 0) for _ in range(int(input()))]))