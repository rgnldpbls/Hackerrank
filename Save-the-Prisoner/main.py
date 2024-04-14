def saveThePrisoner(n, m, s):
    # Write your code here
    last_pos = (s + m - 1) % n
    return last_pos if last_pos != 0 else n