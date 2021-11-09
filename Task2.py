#Task 2 Below:

# The area of rectangle 7cm long and 4cm wide
L = 7
B = 4
Area = L * B
print (Area)
print (f"The area of a circle with a length of {L} and breadth of {B} is {Area}")


#Task 2

#1. The area of a circle with a radius of 7,  given pi to be 3.142  (area of a circle = 𝛑r2)

pi = 3.142
radius = 7
area_of_a_circle = (pi * radius**2)
print (f"The area of a circle with a radius of {radius} equals {area_of_a_circle}")


#2. The volume of a cylinder with a depth of 20cm, and whose circular end has a radius of 2.5cm. (volume of a cylinder = 𝛑r2h)

height = 20
radius = 2.5
pi = 3.142
volume_of_a_cylinder = (pi) * (radius**2) * (height)
print (f"The volume of a cylinder with a depth of 20cm, and whose circular end has a radius of 2.5cm is {volume_of_a_cylinder} cm³")


#3. A cubic box with the dimensions 15cm width, 25cm length and 5 cm height has a volume of? (volume of a cuboid = length x breadth x height)

width = 15
length = 25
height = 5
vol_of_cuboid = width * length * height
print (f"A cubic box with the dimensions 15cm width, 25cm length and 5 cm height has a volume of {vol_of_cuboid}")


#4. What is the area of a triangle whose base is 8cm and height is 12cm? (1/2bh)

base = 8
height = 12
area_of_triangle = (1/2) * (base) * (height)
print (f"The area of triangle whose base is 8cm and height is 12cm equals {area_of_triangle} cm2 ")


#5. 
"""The volume of the concrete needed for a slab spanning 20 metres in length, 
with a thickness of 0.225m and a width of 5 metres. 
(Hint: Volume of a concrete = multiply the length by the width, and thickness)
"""

length = 20
thickness = 0.225
width = 5

volume_of_a_concrete = length * thickness * width
print(f"The volume of the concrete needed is: {volume_of_a_concrete} cubic metres ")
