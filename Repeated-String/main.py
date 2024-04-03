def repeatedString(s, n):
    # Write your code here
    count_a = s.count('a')
    num_repetitions = n // len(s)
    remaining_chars = n % len(s)
    count_a_remain = s[:remaining_chars].count('a')
    total_a_count = count_a * num_repetitions + count_a_remain
    return total_a_count