def hurdleRace(k, height):
    # Write your code here
    max_height = max(height)
    doses_needed = max_height - k
    return max(0, doses_needed)