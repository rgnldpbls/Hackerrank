def catAndMouse(x, y, z):
    dist_a = abs(z-x)
    dist_b = abs(z-y)
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"