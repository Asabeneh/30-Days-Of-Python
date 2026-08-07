import math


## Euclidean distance 2 point of (x1, y1) and (x2, y2)
## (square root((x1 - x2)^2 + (y1 - y2)^2))

def calcEuclidean(point1, point2): 
    '''Calcualte the distance between 2 points
        using the Euclidean formula'''
    return math.sqrt((point1["X"] - point2["X"])**2 + (point1["Y"]- point2["Y"])**2)
    
    
    
testPoint1 = {
    "X": 1,
    "Y": 4
}

testPoint2 = {
    "X": 3,
    "Y": 3
}

print(calcEuclidean(testPoint1, testPoint2))