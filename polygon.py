import turtle


poly = turtle.Turtle()



def polygon(t):
    number_of_side = 9
    total_internal_angle = (number_of_side - 2) * 180
    per_angle = int (total_internal_angle / number_of_side)
    length = 100

    create_polygon(t,number_of_side, per_angle, length)



def create_polygon(t, n, a, l):
    for i in range(n):
        t.fd(l)
        t.lt(180 - a)

    

polygon(poly)

turtle.mainloop()