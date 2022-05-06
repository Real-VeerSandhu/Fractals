from turtle import *

shape("arrow")
width(2)
speed(20)
screensize(100, 100)


def fractal_side(length, n):
    if n == 0:
        forward(length)
        return

    length /= 3.0
    fractal_side(length, n - 1)
    left(60)
    fractal_side(length, n - 1)
    right(120)
    fractal_side(length, n - 1)
    left(60)
    fractal_side(length, n - 1)

def build_fractal(sides, length, n):
    for i in range(sides):
        fractal_side(length, n)
        right(360 / sides)

# fractal_side(200, 2)

build_fractal(3, 600, 3)

