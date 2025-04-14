# Import math module to use square root
import math

# Request 3 side lengths of a triangle from the user
print("Give the lengths of three sides of a triangle:")
side1 = int(input("side 1: "))
side2 = int(input("side 2: "))
side3 = int(input("side 3: "))

# Calculate the area using Heron's Formula
s = (side1+side2+side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

# Print the area
print(f"The area of that triangle is {round(area,2)}")