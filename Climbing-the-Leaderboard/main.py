def climbingLeaderboard(ranked, player):
    # Write your code here
    distinct_scores = sorted(set(ranked), reverse=True)
    result = []
    l = len(distinct_scores)
    i = l - 1
    
    for p in player:
        while i >= 0 and p >= distinct_scores[i]:
            i -= 1
        result.append(i+2)
        
    return result