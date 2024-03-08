def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    
    dOne = 0
    dTwo = 0
    
    for i in range(n):
        dOne += arr[i][i]
        dTwo += arr[i][n-i-1]
    
    diff = abs(dOne - dTwo)
    
    return diff