import turtle
import math

poly = turtle.Turtle()



def polygon(t):
    number_of_side = 9
    total_internal_angle = (number_of_side - 2) * 180
    per_angle = int(total_internal_angle / number_of_side)
    base_length = 150
    print(per_angle)
    create_polygon(t,number_of_side, per_angle, base_length)



def create_polygon(t, n, a, l):
    for i in range(n):
        t.fd(l)
        t.lt(180 - a)
    
    for i in range(n-1):
        triangle(t, n, a, l)
        t.lt(180 - a)
    




def triangle(t, n, a, l):
     
    angle_degree = a / 2
    angle_radian = math.radians(angle_degree)
    x_coord_point = math.cos(angle_radian)
    side_length = math.ceil(l / (2 * x_coord_point))

    triangle_drawing(l, angle_degree, side_length)


 
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