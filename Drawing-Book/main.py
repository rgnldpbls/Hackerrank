def pageCount(n, p):
    # Write your code here
    ffront = p // 2
    fback = (n // 2) - (p // 2)
    return min(ffront, fback)