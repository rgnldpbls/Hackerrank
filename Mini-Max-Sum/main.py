def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum =  sum(arr[1:])
    print(min_sum, max_sum)