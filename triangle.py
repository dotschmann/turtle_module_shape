import turtle

poly = turtle.Turtle()

# equilateral triangle

def equi_angle():
    for _ in range(3):
        poly.fd(100)
        poly.lt(120)

    
equi_angle()

turtle.mainloop()