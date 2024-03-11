def timeConversion(s):
    hour, minute, second = map(int, s[:-2].split(':'))
    meridiem = s[-2:]
    
    if meridiem == 'PM' and hour < 12:
        hour += 12
    elif meridiem == 'AM' and hour == 12:
        hour = 0
        
    return '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)