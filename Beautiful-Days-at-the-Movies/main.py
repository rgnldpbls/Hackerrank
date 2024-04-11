def reverse_number(n):
    return int(str(n)[::-1])

def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for day in range(i, j + 1):
        rev_day = reverse_number(day)
        if abs(day - rev_day) % k == 0:
            count += 1
    return count