# >:(
def InsideMandelBrotSet(x, iy, looplength = 10, threshold = 2):
    """ function takes x and iy ints values and returns a bool
    value for if the point is inside the Mandel Brot set or not """
    # Zn = (Zn-n)^2+ic
    # ic = x + iy
    ic = complex(x, iy)
    Zn = ic
    for itercount in range(looplength):
        if abs(Zn) > threshold:
            return itercount 
        # old version smh
        # sqrZn = (Zn[0] * Zn[0] + (-1*(Zn[1] * Zn[1])), Zn[0] * Zn[1] + Zn[1] * Zn[0])
        # Zn = (sqrZn[0] + x, sqrZn[1] + iy)
        Zn = Zn**2 + ic
    return None
    
def Mandel_Brot_Set(xrange = (-2, 2), iyrange = (-2, 2), setaccuracy = 2, looplength = 10):
    """ Mandel_Brot_Set function takes in xrange and yrange tuples
    setaccuracy and looplength ints and returns a 2d list[x][y] of bools
    for if a courdenate is in the MandelBrot set or not """
    
    MandeBrotSet = []
    NumIncrease = 1 * 10**(-setaccuracy)
    Xi, Xf = xrange[0], xrange[1]
    Yi, Yf = iyrange[0], iyrange[1]
    Xiter, iYiter = Xi, Yi

    while Xiter < Xf:
        iYiter = Yi
        Ylist = []
        while iYiter < Yf:
            Ylist.append(InsideMandelBrotSet(Xiter , iYiter, looplength))
            iYiter += NumIncrease
        MandeBrotSet.append(Ylist)
        Xiter += NumIncrease
    
    return MandeBrotSet