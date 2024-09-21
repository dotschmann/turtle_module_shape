import turtle
import math

poly = turtle.Turtle()

# calculate side length of a triangle
base_length = 100 
angle_degree = 54
angle_radian = math.radians(angle_degree)
x_coord_point = math.cos(angle_radian)
side_length = int( base_length / (2 * x_coord_point))


 
def isosceles_tri():
    poly.fd(base_length)
    poly.lt(180 - angle_degree)

    poly.fd(side_length)
    poly.lt(180)

    poly.fd(side_length)
    poly.lt(180 + angle_degree)

    poly.fd(base_length)
    poly.lt(180 + angle_degree)

    poly.fd(side_length)



isosceles_tri()


# #Isosceles triangle with base angle 54°, base length of 100 and side length of 85

# def isosceles_tri():
#     poly.fd(100)
#     poly.lt(180-54)

#     poly.fd(85)
#     poly.lt(180)

#     poly.fd(85)
#     poly.lt(180+54)

#     poly.fd(100)
#     poly.lt(180+54)

#     poly.fd(85)



# isosceles_tri()

# equilateral triangle

# def equi_angle():
#     for _ in range(3):
#         poly.fd(100)
#         poly.lt(120)

    
# equi_angle()

turtle.mainloop()