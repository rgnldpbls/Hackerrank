def birthday(s, d, m):
    # Write your code here
    ways = [sum(s[i:i+m]) for i in range(len(s)-m+1)]
    return ways.count(d)