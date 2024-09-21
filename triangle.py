import turtle
import math

poly = turtle.Turtle()

# calculate side length of a triangle

def triangle():
    base_length = 200 
    angle_degree = 30
    angle_radian = math.radians(angle_degree)
    x_coord_point = math.cos(angle_radian)
    side_length = math.ceil( base_length / (2 * x_coord_point))

    isosceles_tri(base_length, angle_degree, side_length)


 
def isosceles_tri(b, a, s):
    poly.fd(b)
    poly.lt(180 - a)

    poly.fd(s)
    poly.lt(180)

    poly.fd(s)
    poly.lt(180 + a)

    poly.fd(b)
    poly.lt(180 + a)

    poly.fd(s)



triangle() 


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