import matplotlib.pyplot as plt
import numpy as np
import math
import sympy
from sympy import *


def eulersMethod(differential,step,initX,initY,finalX):
    currY = initY
    currX = initX
    print("( " + str(currX) + "," + str(currY) + " )")
    xArr = []
    yArr = []
    while (currX < finalX):
        xArr.append(currX)
        yArr.append(currY)
        tempDiff = list(differential)
        valueDict = {"x": str(currX), "y": str(currY), "e": str(math.e), "pi": str(math.pi)}
        currDifferential = "".join(valueDict.get(ele, ele) for ele in tempDiff)
        x, y = sympy.symbols('x y')
        currDifferential = sympify(currDifferential)
        currY += (currDifferential.evalf())*step
        currX += step
        print("( " + str(currX) + "," + str(currY) + " )")
    plt.plot(xArr, yArr)
    plt.show()  


print("Lets use Eulers Method to approximate solution curves!")
print("Please make sure to keep PEMDAS in mind when using this tool. Parenthesis can be used.")
print("=======================================================")
userDifferential = str(input("Enter the differential equation(use ** for exponentiation, * for multiplication and / for division): "))
stepSize = float(input("Enter the step size: "))
initialX = float(input("Enter the initial X value: "))
initialY = float(input("Enter the initial Y value: "))
finalX = float(input("Enter the final X value: "))
print("=======================================================")
eulersMethod(userDifferential,stepSize,initialX,initialY,finalX)

