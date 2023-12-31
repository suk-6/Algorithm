from math import factorial as f

for i in range(int(input())):
    n, m = map(int, input().split(" "))
    bridge = f(m) // (f(n) * f(m - n))
    print(bridge)