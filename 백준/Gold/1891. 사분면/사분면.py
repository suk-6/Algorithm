def getCoordinate(idx, x1, x2, y1, y2):
    global number
    if idx == len(number):
        return x1, y1

    target = int(number[idx])

    halfx = (x1 + x2) // 2
    halfy = (y1 + y2) // 2

    if target == 1:
        return getCoordinate(idx + 1, x1, halfx, halfy, y2)
    elif target == 2:
        return getCoordinate(idx + 1, x1, halfx, y1, halfy)
    elif target == 3:
        return getCoordinate(idx + 1, halfx, x2, y1, halfy)
    elif target == 4:
        return getCoordinate(idx + 1, halfx, x2, halfy, y2)


def find(x1, x2, y1, y2):
    global result, mx, my, d
    if d == len(result):
        return result

    halfx = (x1 + x2) // 2
    halfy = (y1 + y2) // 2

    if halfx <= mx < x2 and y1 <= my < halfy:
        result.append(1)
        return find(halfx, x2, y1, halfy)
    elif x1 <= mx < halfx and y1 <= my < halfy:
        result.append(2)
        return find(x1, halfx, y1, halfy)
    elif x1 <= mx < halfx and halfy <= my < y2:
        result.append(3)
        return find(x1, halfx, halfy, y2)
    elif halfx <= mx < x2 and halfy <= my < y2:
        result.append(4)
        return find(halfx, x2, halfy, y2)
    else:
        raise Exception(result)


d, number = (lambda x: [int(x[0]), str(x[1])])(input().split())
x, y = map(int, input().split())
qs = 2**d
result = []

ox, oy = getCoordinate(0, 0, qs, 0, qs)
mx, my = oy + x, ox + (y * -1)

if 0 <= mx < qs and 0 <= my < qs:
    print(int("".join(str(c) for c in find(0, qs, 0, qs))))
else:
    print(-1)
