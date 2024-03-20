def breakingRecords(scores):
    # Write your code here
    if len(scores) == 0:
        return 0, 0
    
    min_score = max_score = scores[0]
    min_count = max_count = 0
    
    for score in scores:
        if score < min_score:
            min_score = score
            min_count += 1
        elif score > max_score:
            max_score = score
            max_count += 1
    
    return max_count, min_count