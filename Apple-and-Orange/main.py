def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleCnt = sum(1 for apple in apples if s <= a + apple <= t)
    orangeCnt = sum(1 for orange in oranges if s <= b + orange <= t)
    print(appleCnt)
    print(orangeCnt)