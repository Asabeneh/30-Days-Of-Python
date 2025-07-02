# Challenge #3 
# Calculate the Euclidian Distance between 2 points (2,3) and (10,8)
import math

def calcEuclidianDistance(x1,y1,x2,y2):
    #Calc the differnce between 2 points
    deltaX = x2-x1
    deltaY = y2-y1
    
    # Square the difference 
    sq_deltaX = deltaX**2
    sq_deltaY = deltaY**2
    
    # Sum of squares
    sum_sq_Delta = sq_deltaX+sq_deltaY
    
    # square root for final calculation
    EuclidianDistance = f"{(math.sqrt(sum_sq_Delta)):.2f}"

    print("DeltaX = " + str(deltaX))
    print("DeltaY = " + str(deltaY))
    print("DeltaX ^2 = " + str(sq_deltaX))
    print("DeltaY ^2 = " + str(sq_deltaY))
    print("Sum of the Squares = " + str(sum_sq_Delta))
    print("The Eclidian Distance for (" + (str(x1)) + (", ") + (str(y1)) + (") and (") + (str(x2)) + (", ") + (str(y2)) + (") = ") + (str(EuclidianDistance)))

calcEuclidianDistance(2,3,10,8)
print('\n' + "Congrats Pac! You did it🚀 \n Day 1 in the book! \n Don't forget to upload!\n")