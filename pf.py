# burning ship fractal

def ship_loop(x, iy, MAXitercount = 50, threshold = 5):    
    """ returns None if the number stays bounded
    returns the number of iterations if the number escapes
    takes RELx, IMGy for a complex number, max iteration count,
    escape threshold hold """

    ic = complex(x, iy)
    Z = ic
    for itercount in range(MAXitercount):
        if abs(Z) > threshold:
            return itercount
        Z = (abs(Z.real) + abs(Z.imag))**2 + ic
    return None

def ComplexFractalSetCreator(Xaxis , iYaxis ,  Func, looplength = 10, threshold = 2):
    """ function takes x axis, iy axis lists, Func fractal function, setaccuracy, looplength, threshold ints
    returns a 2d array[x][y] of the return of the given Func for values in the x and iy range """

    FractalSet = []
    for i in Xaxis:
        ySet = []
        for j in iYaxis:        
            ySet.append(Func(i , j, looplength, threshold))
        FractalSet.append(ySet)

    return FractalSet

def CreatListForRange(Range, Accuracy = 2):
    """ takes Range tulep or list returns List form the start 
    of the list to the end incrementing by 10**(-Accuracy) """

    List = []
    i = Range[0]
    while i < Range[1]:
        List.append(i)
        i += 10**(-Accuracy)
    
    return List

# x = CreatListForRange((0, 4))
# y = CreatListForRange((0, 4))

# set = ComplexFractalSetCreator(x, y, ship_loop, threshold = 5)
# file = open("output.txt", "w")
# file.write(str(set))
# file.close()
