def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    # Write your code here
    lcm_a = a[0]
    for num in a[1:]:
        lcm_a = lcm(lcm_a, num)
        
    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = gcd(gcd_b, num)
        
    count = 0
    for i in range(lcm_a, gcd_b+1, lcm_a):
        if gcd_b%i == 0:
            count += 1
    return count