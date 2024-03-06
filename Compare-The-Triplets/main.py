def compareTriplets(a, b):
    # Write your code here
    c = 0
    d = 0
    if a[0] > b[0]:
        c += 1
        if a[1] > b[1]:
            c += 1
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
        elif a[1] == b[1]:
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
        else:
            d += 1
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
    elif a[0] == b[0]:
        if a[1] > b[1]:
            c += 1
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
        elif a[1] == b[1]:
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
        else:
            d += 1
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
    else:
        d += 1
        if a[1] > b[1]:
            c += 1
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
        elif a[1] == b[1]:
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]
        else:
            d += 1
            if a[2] > b[2]:
                c += 1
                return [c, d]
            elif a[2] == b[2]:
                return [c, d]
            else:
                d += 1
                return [c, d]