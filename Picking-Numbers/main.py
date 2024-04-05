def pickingNumbers(a):
    buckets = [0 for _ in range(100)]
    for i in a:
        buckets[i] += 1
    res = 0
    for i in range(1, 99):
        res = max(res, buckets[i] + buckets[i+1])
    return res