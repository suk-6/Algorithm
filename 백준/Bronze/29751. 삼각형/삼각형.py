import sys

w, h = list(map(int, sys.stdin.readline().split()))

print(round(w * h / 2, 1))