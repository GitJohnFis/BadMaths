#Floor division is the # of wholes times num can fit into nom and the fraction is discarded
def floor_division(num, nom):
    """Returns the floor division of num divided by nom (rounded towards negative infinity)"""
    if nom == 0:
        raise ValueError("Cannot divide by zero")
    result = num / nom
    if result >= 0:
        return int(result)
    else:
        integer_part = int(result)
        if result == integer_part:
            return integer_part
        else:
            return integer_part - 1
        
    print(floor_division(num, nom))

    