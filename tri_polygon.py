import turtle
import math

poly = turtle.Turtle()



def polygon(t):
    number_of_side = 5
    total_internal_angle = (number_of_side - 2) * 180
    per_angle = int (total_internal_angle / number_of_side)
    length = 100

    create_polygon(t,number_of_side, per_angle, length)



def create_polygon(t, n, a, l):
    for i in range(n):
        t.fd(l)
        t.lt(180 - a)
    
    for i in range(n):
        triangle()
        t.lt(180 - a)
    




def triangle():
    base_length = 100 
    angle_degree = 54
    angle_radian = math.radians(angle_degree)
    x_coord_point = math.cos(angle_radian)
    side_length = math.ceil( base_length / (2 * x_coord_point))

    triangle_drawing(base_length, angle_degree, side_length)


 
def triangle_drawing(b, a, s):
    poly.fd(b)
    poly.lt(180 - a)

    poly.fd(s)
    poly.lt(180)

    poly.fd(s)
    poly.lt(180 + a)

    poly.fd(b)
    poly.lt(180 + a)

    poly.fd(s)
    poly.lt(180)

    poly.fd(s)

    poly.lt(180 - a)
    poly.fd(b)
    


polygon(poly)

turtle.mainloop()