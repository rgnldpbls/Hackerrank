def camelcase(s):
    # Write your code here
    count = 1
    for char in s:
        if char.isupper():
            count += 1
    return count