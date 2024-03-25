def bonAppetit(bill, k, b):
    # Write your code here
    actual_cost = (sum(bill) - bill[k]) // 2
    if actual_cost == b:
        print("Bon Appetit")
    else:
        print(b - actual_cost)