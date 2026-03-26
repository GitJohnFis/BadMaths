#base = log(base in subscript)(product)
# The logarithm of a product is the sum of the logarithms of the factors
# For example, log(2*3) = log(2) + log(3)


def logarithms(base, product):
    # The logarithm of a product is the sum of the logarithms of the factors
    # For example, log(2*3) = log(2) + log(3)
    if product == 1:
        """The logarithm of 1 is always 0, regardless of the base."""
        return 0
    elif product == base:
        """The logarithm of a number to its own base is always 1."""
        return 1
    else:
        """For other products, we can use the change of base formula to calculate the logarithm."""
        return log(product) / log(base)