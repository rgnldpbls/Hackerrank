def plusMinus(arr):
    # Write your code here
    n = len(arr)
    a = 0
    b = 0
    c = 0
    
    for i in arr:
        if i > 0:
            a += 1
        elif i < 0:
            b += 1
        else:
            c += 1
            
    pos = a / n
    neg = b / n
    zero = c / n
    
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zero))