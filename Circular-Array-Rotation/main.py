def circularArrayRotation(a, k, queries):
    # Write your code here
    n = len(a)
    k = k % n # Ensure k is within the range [0, n)
    rotated_arr = a[-k:] + a[:-k]
    return [rotated_arr[q] for q in queries]