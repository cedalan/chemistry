import numpy as np 

def numerical_derivative(x , y, method = "forward"):
    """
    Parameters:
    -----------
    x:
    One-dimensional array of x-values.

    y:
    One-dimensional array of y-values corresponding to the array of x-values.

    method:
    Specifies which method is used. Default is forward-method. Backwards derivative is also possible.

    Returns:
    --------
    fder - Array of estimated derivatives. 

    NB: if forward is chosen, the numerical derivative is calculated for f[0:-2], while for backward it is calculated for f[1:-1]
    """
    fder = np.zeros(len(y) - 1)

    if method == "forward":
        for i in range(len(y) - 1):
            fder[i] = (y[i + 1] - y[i])/(x[i + 1] - x[i])
        
        return fder

    if method == "backward":
        for i in range(len(y) - 1):
            fder[i] = (y[i + 1] - y[i])/(x[i + 1] - x[i])
        
        return fder

def pH(H = None, OH = None):

    msg = "You need to provide the concentration of either H3O+ or OH-!"

    assert (H != None and OH != None), msg

    if H == None:
        return 14 + np.log10(OH)
    
    else:
        return np.log10(H)


def dillution(c1 = None, c2 = None, V1 = None, V2 = None, printMessages = False):

    msg = "You need to provide 3 variables for this equation to make sense!!"
    noneCount = 0
    variables = [c1, c2, V1, V2]
    for v_ in variables:
        if v_ == None:
            noneCount += 1
    
    assert noneCount < 2, msg
    
    if c1 == None:
        c1 = c2 * V2 / V1
        if printMessages:
            print(f"Old concentration was: {c1}")
        return c1
    
    if c2 == None:
        c2 = c1 * V1 / V2
        if printMessages:
            print(f"New concentration is: {c2}")
        return c2
            
    if V1 == None:
        V1 = c2 * V2 / c1
        if printMessages:
            print(f"Old volume was: {V1}")
        return V1
            
    if V2 == None:
        V2 = c1 * V1 / c2
        if printMessages:
            print(f"New volume is: {V2}")
        return V2


