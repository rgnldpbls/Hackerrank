def getMoneySpent(keyboards, drives, b):
    max_spent = -1
    for keyboard in keyboards:
        for drive in drives:
            total_price = keyboard + drive
            if total_price <= b and total_price > max_spent:
                max_spent = total_price
    return max_spent