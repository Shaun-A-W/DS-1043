"""Lab 5 DS-1043

This file includes turtle functions to draw squares, circles,
flowers, polygons, and other shapes.

Completed by Shaun W. by 2024-10-01 (YYYY-MM-DD) for DS-1043"""

import turtle
import math
import time
import stack_lab5 as stack


#general turtle
def square(t, length: int):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.setheading(0)


def polygon(t, length: int, n: int):
    ang = 360/n
    # stack.print_frame("Poly Before Loop", locals(), step=True)
    for i in range(n):
        turtle.forward(length)
        turtle.left(ang)
        # stack.print_frame("Poly End of each Loop", locals(), step=False)
    # stack.print_frame("Poly After Loop", locals(), step=True)


def circle(t, r: int):
    c = 2 * r * math.pi
    sides = 60
    dist = c/sides
    # stack.print_frame("Circle Before Poly", locals(), step=True)
    polygon(t, dist, sides)
    # stack.print_frame("Circle After Poly", locals(), step=True)


def arc(t, r: int, angle: float):
    c = 2 * r * math.pi
    arc_length = c * (angle / 360)
    n = 60
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        turtle.forward(step_length)
        turtle.left(step_angle)


# def reverse_arc(t, r: int, angle: int):
#     c = 2 * r * math.pi
#     arc_length = c * (angle / 360)
#     n = 60
#     step_length = arc_length / n
#     step_angle = angle / n
#     for i in range(n):
#         turtle.forward(step_length)
#         turtle.right(step_angle)


#flowers
def flower(petals: int, overlap: int, petal_radius: int):
    turtle.speed(0)
    if petals - overlap < 1:
        return None

    covering = petals - overlap
    for i in range(petals):
        turtle.setheading(0 + i * 360/petals)
        arc(turt, petal_radius, 360/covering)
        turtle.setheading(180 + i * 360/petals)
        arc(turt, petal_radius, 360/covering)


def pie_poly(t, r, sides: int):
    ang = 360/sides
    for i in range(sides):
        turtle.left(i * ang)
        turtle.forward(r)
        a = turtle.pos()
        turtle.home()
        turtle.left((i + 1) * ang)
        turtle.forward(r)
        b = turtle.pos()
        turtle.setpos(a)
        turtle.goto(b)
        turtle.home()


#start alphabet & writing fxs

def draw_a():
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    circle(turt, 10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(20)
    turtle.setheading(0)

def draw_b():
    turtle.setheading(0)
    square(turt, 25)
    turtle.left(90)
    turtle.forward(50)
    turtle.setheading(0)

def draw_c():
    turtle.setheading(0)
    turtle.forward(25)
    turtle.back(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.setheading(0)

def draw_d():
    turtle.setheading(0)
    square(turt, 25)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.setheading(0)

def draw_e():
    turtle.setheading(0)
    turtle.forward(25)
    turtle.backward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.setheading(0)

def draw_f():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.back(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(15)
    turtle.setheading(0)

def draw_g():
    turtle.setheading(0)
    square(turt, 25)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.setheading(0)

def draw_h():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(50)
    turtle.back(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.setheading(0)

def draw_i():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(40)
    turtle.penup()
    turtle.forward(10)
    turtle.setheading(0)
    turtle.pendown()
    circle(turt, 3)
    turtle.setheading(0)

def draw_j():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(40)
    turtle.penup()
    turtle.forward(10)
    turtle.setheading(0)
    turtle.pendown()
    circle(turt, 3)
    turtle.setheading(0)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.setheading(0)

def draw_k():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(60)
    turtle.back(40)
    turtle.setheading(0)
    turtle.left(45)
    turtle.forward(30)
    turtle.back(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.setheading(0)

def draw_l():
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(60)
    turtle.setheading(0)

def draw_m():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.back(25)
    turtle.setheading(0)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.setheading(0)

def draw_n():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.setheading(0)

def draw_o():
    turtle.setheading(0)
    turtle.forward(12.5)
    circle(turt, 25)
    turtle.setheading(0)

def draw_p():
    turtle.setheading(0)
    square(turt, 25)
    turtle.right(90)
    turtle.forward(30)
    turtle.setheading(0)

def draw_q():
    turtle.setheading(0)
    square(turt, 25)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(30)
    turtle.setheading(0)

def draw_r():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(25)
    turtle.back(5)
    turtle.setheading(0)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(5)
    turtle.setheading(0)

def draw_s():
    turtle.setheading(0)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(25)
    turtle.setheading(0)

def draw_t():
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.back(15)
    turtle.setheading(0)
    turtle.back(15)
    turtle.forward(30)
    turtle.setheading(0)

def draw_u():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(25)
    turtle.back(25)
    turtle.setheading(0)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.setheading(0)

def draw_v():
    turtle.setheading(0)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.setheading(0)
    turtle.right(60)
    turtle.forward(29)
    turtle.setheading(0)
    turtle.left(60)
    turtle.forward(29)
    turtle.setheading(0)

def draw_w():
    turtle.setheading(0)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.setheading(0)
    turtle.right(75)
    turtle.forward(26)
    turtle.setheading(0)
    turtle.left(75)
    turtle.forward(26)
    turtle.setheading(0)
    turtle.right(75)
    turtle.forward(26)
    turtle.setheading(0)
    turtle.left(75)
    turtle.forward(26)
    turtle.setheading(0)

def draw_x():
    turtle.setheading(0)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.setheading(0)
    turtle.right(45)
    turtle.forward(35)
    turtle.setheading(0)
    turtle.penup()
    turtle.back(25)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(35)
    turtle.setheading(0)

def draw_y():
    turtle.setheading(0)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.setheading(0)
    turtle.right(60)
    turtle.forward(29)
    turtle.setheading(0)
    turtle.left(60)
    turtle.back(29)
    turtle.forward(58)
    turtle.setheading(0)

def draw_z():
    turtle.setheading(0)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.left(45)
    turtle.back(35)
    turtle.setheading(0)
    turtle.forward(25)

draw_list = [
    draw_a,
    draw_b,
    draw_c,
    draw_d,
    draw_e,
    draw_f,
    draw_g,
    draw_h,
    draw_i,
    draw_j,
    draw_k,
    draw_l,
    draw_m,
    draw_n,
    draw_o,
    draw_p,
    draw_q,
    draw_r,
    draw_s,
    draw_t,
    draw_u,
    draw_v,
    draw_w,
    draw_x,
    draw_y,
    draw_z
]

def writing(words: str):
    spacing = 1
    turtle.penup()
    turtle.setpos(-500,0)
    turtle.pendown()
    for letter in words:
        if 'a' <= letter <= 'z':
            character = ord(letter) - ord('a')
            draw_list[character]()
            turtle.penup()
            turtle.setpos(x=(spacing * 50 - 500),y=0)
            turtle.setheading(0)
            spacing += 1
            turtle.pendown()
        elif letter == ' ':
            turtle.penup()
            turtle.setpos(x=(spacing * 50 - 500),y=0)
            turtle.setheading(0)
            spacing += 1
            turtle.pendown()

#end alphabet & writing fxs


#cleanup function for between function calls
def clean():
    turtle.hideturtle()
    time.sleep(x)
    turtle.clearscreen()
    turtle.home()
    turtle.settiltangle(0)
    turtle.speed(7)
    turtle.pensize(3)
    turtle.showturtle()


if __name__ == "__main__":
### MAIN BLOCK START ###

    x = 3 # SLEEP TIME FOR CLEAN FUNCTION
    turt = turtle.Turtle() # START TURTLE
    turtle.speed(7) # TURTLE DRAW SPEED
    turtle.pensize(3)
    # turtle.pencolor("Light Pink")

    # stack testing
    # stack.print_frame("Before calling Circle", globals(), step=True)
    # circle(turt,50)
    # stack.print_frame("After calling Circle", globals(), step=True)

    # square(turt,100)
    # clean()
    #
    # polygon(turt,100,10)
    # clean()
    #
    # circle(turt, 100)
    # clean()
    #
    # arc(turt, 100, 90)
    # clean()
    #
    # flower(6, 0, 200)
    # clean()
    #
    # flower(7, 3, 200)
    # clean()
    #
    # flower(15, 0, 200)
    # clean()

    # pie_poly(turt, 200, 5)
    # clean()

    # draw_a()
    # clean()
    # draw_b()
    # clean()
    # draw_c()
    # clean()
    # draw_d()
    # clean()
    # draw_e()
    # clean()
    # draw_f()
    # clean()
    # draw_g()
    # clean()
    # draw_h()
    # clean()
    # draw_i()
    # clean()
    # draw_j()
    # clean()
    # draw_k()
    # clean()
    # draw_l()
    # clean()
    # draw_m()
    # clean()
    # draw_n()
    # clean()
    # draw_o()
    # clean()
    # draw_p()
    # clean()
    # draw_q()
    # clean()
    # draw_r()
    # clean()
    # draw_s()
    # clean()
    # draw_t()
    # clean()
    # draw_u()
    # clean()
    # draw_v()
    # clean()
    # draw_w()
    # clean()
    # draw_x()
    # clean()
    # draw_y()
    # clean()
    # draw_z()
    # clean()

    # writing("abcdefghijklmnopqrstuvwxyz")
    # clean()
    # writing("shaun")
    # clean()

    turt.screen.mainloop() # PAUSE SCREEN AT END

### MAIN BLOCK END ###