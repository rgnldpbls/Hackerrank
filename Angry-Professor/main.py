def angryProfessor(k, a):
    # Write your code here
    on_time_stud = sum(1 for time in a if time <= 0)
    return "YES" if on_time_stud < k else "NO"