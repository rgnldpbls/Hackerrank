def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valleyCount = 0
    for p in path:
        if p == 'U':
            altitude += 1
        if p == 'D':
            altitude -= 1
        if(altitude == 0 and p == 'U'):
            valleyCount += 1
    return valleyCount      