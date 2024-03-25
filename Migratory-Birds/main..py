def migratoryBirds(arr):
    # Write your code here
    count = {}
    for type in arr:
        if type in count:
            count[type] += 1
        else:
            count[type] = 1
    
    max_count = max(count.values())
    common_bird = [type for type, count in count.items() if count == max_count]
    return min(common_bird)