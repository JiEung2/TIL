import math
r = 5.73
def getDistance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calTheta(hole, target, myBall):

    a = getDistance(hole, myBall)
    b = getDistance(hole, target)
    c = getDistance(target, myBall)

    Ga = math.degrees(math.atan(abs(hole[1] - myBall[1]) / abs(hole[0] - myBall[0])))
    Da = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))

    d = math.sqrt(a**2 + (b+r)**2 - 2*a*(b+r) * math.cos(math.radians(Da)))
    Na = math.degrees(math.acos((a**2 + d**2 - (b+r)**2) / (2*a*d)))

    return Ga + Na

def select_hole(holes, target, myBall):
    angle = []

    if target[0] < myBall[0] and target[1] < myBall[1]:
        angle.append(calTheta(hole, target, myBall))
    elif myBall[0] < target[0] and target[1] < myBall[1]:
    elif target[0] < myBall[0] and myBall[1] < target[1]:
    elif myBall[0] < target[0] and myBall[1] < target[1]:

    else:




h = [25, 27]
m = [3, 3]
t = [13, 14]

print(calTheta(h, t, m))
print(math.cos(math.radians(45)))