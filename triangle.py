import turtle

poly = turtle.Turtle()

#Isosceles triangle with base angle 54°, base length of 100 and side length of 85

def isosceles_tri():
    poly.fd(100)
    poly.lt(180-54)

    poly.fd(85)
    poly.lt(180)

    poly.fd(85)
    poly.lt(180+54)

    poly.fd(100)
    poly.lt(180+54)

    poly.fd(85)



isosceles_tri()

# equilateral triangle

# def equi_angle():
#     for _ in range(3):
#         poly.fd(100)
#         poly.lt(120)

    
# equi_angle()

turtle.mainloop()