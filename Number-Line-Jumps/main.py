def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 == v2:
        return "NO"
    else:
        num_jumps = (x2 - x1) / (v1 - v2)
        if num_jumps.is_integer() and num_jumps >= 0:
            return "YES"
        else:
            return "NO"