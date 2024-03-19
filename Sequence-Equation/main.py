def permutationEquation(p):
    # Write your code here
    n = len(p)
    index_dict = {p[i]: i+1 for i in range(n)}
    result = []
    for x in range(1, n+1):
        y = index_dict[index_dict[x]]
        result.append(y)
    return result