#Ben Shea
#Comfy Deviations
#CS112 Professor Senbel

import math

num1 = -1
num2  = -1
total = 0
squaredDiff = 0

temps = list(map(float, input("Enter 10 temperatures: ").split()))

for i in range(0,10):
    num1 = num1 + 1
    total = total + temps[num1]

mean = total / 10

for i in range(0,10):
    num2 = num2 + 1
    squaredDiff = squaredDiff + (temps[num2] - mean)**2

stanDeviation = (squaredDiff / 10)**0.5

if stanDeviation <= 1.0:
    print("COMFY")
elif stanDeviation > 1.0:
    print("NOT COMFY")

