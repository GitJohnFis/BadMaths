# All productss raised 
# to the level of the raised power
#For example, 2^3 = 2*2*2 = 8
def exponents(base, power):
    #Tbh all this is already python native and expressed with two
    #asterisks, but some nuances on the 1 and 0 powers
if power == 1:
        """If the power is 1, then the base is retuned as it is"""
        return base
elif power == 0:
        """If the power is 0, then 1 is returned as the result of any n raised"""
        return 1