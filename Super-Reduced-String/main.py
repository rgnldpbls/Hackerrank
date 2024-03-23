def superReducedString(s):
    # Write your code here
    stack = []
    for char in s:
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    if not stack:
        return "Empty String"
    else:
        return ''.join(stack)