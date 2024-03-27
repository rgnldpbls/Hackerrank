def sockMerchant(n, ar):
    # Write your code here
    color_counts = {}
    for color in ar:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    
    pairs = 0
    for count in color_counts.values():
        pairs += count // 2
        
    return pairs