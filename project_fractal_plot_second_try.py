# project fractal plot second try
import matplotlib.pyplot as plt
from mandel_brot_fractal import InsideMandelBrotSet
import pf
from datetime import datetime

Xrange = (-3, 2) # lim for mandelbrot (-2, 0.5) 
Yrange = (-2, 2) # lim for mandelbrot (-1.15, 1.15)
SetLoopLength = 50
AccuracyFactor = 3
EscapeThreshold = 5
DotSize = 0.001
ColorFade = 1 # 1 for no color fade (real values)

TimeForAll = datetime.now()

TimeForSetCreation = datetime.now()
x = pf.CreatListForRange(Xrange, AccuracyFactor)
y = pf.CreatListForRange(Yrange, AccuracyFactor)
# Set = pf.ComplexFractalSetCreator(x, y, InsideMandelBrotSet, SetLoopLength, EscapeThreshold)
Set = pf.ComplexFractalSetCreator(x, y, pf.ship_loop, SetLoopLength, EscapeThreshold)
TimeForSetCreation = datetime.now() - TimeForSetCreation

XLength = len(Set)
YLength = len(Set[0])

print("\ndone crearing mandelbrot set")
print("set creation time", TimeForSetCreation)
print('set length is X' + str(XLength) + ' by Y' + str(YLength))

TimeForAxisCreation = datetime.now()
xAxis = [[]]
yAxis = [[]]
Xindex = 0
def AxisUpdate(Axis, SetValue):
    if not len(Axis) - 1 < SetValue:
        return
    LengthToMatch = len(Axis) - 1
    while LengthToMatch < SetValue:    
        xAxis.append([])
        yAxis.append([])
        SetValue -= 1
    return

for i in x:
    Yindex = 0
    for j in y:
        SetIndexValue = Set[Xindex][Yindex]
        if not SetIndexValue == None :
            AxisUpdate(xAxis, SetIndexValue)
            xAxis[SetIndexValue].append(i)
            yAxis[SetIndexValue].append(j)
        Yindex += 1
    Xindex += 1

print("done crearing mandelbrot axis")
print("axis creation time", datetime.now() - TimeForAxisCreation)

def ColorSelect(i, lenx, z):
    c = i/len(xAxis)*z
    if c > 1:
        return "1"
    return str(c)

TimeOfPloting = datetime.now()
plt.figure('fractal')
plt.clf()
plt.title('mandelbrot')
# plt.xlim(Xrange)
# plt.ylim(Yrange)
for i in range(len(xAxis)):
    plt.plot(xAxis[i], yAxis[i], "o",
    color= ColorSelect(i, len(xAxis), ColorFade),
    markeredgewidth= DotSize)

TimeOfPloting = datetime.now() - TimeOfPloting
print("done ploting mandelbrot set")
print('ploting time', TimeOfPloting)

TimeForAll = datetime.now() - TimeForAll
print('\ntotal time', TimeForAll)
plt.show()

