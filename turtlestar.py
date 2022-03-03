from turtle import *
from math import *


def formulaX(R, r, p, t):
    x = (R-r)*cos(t) - (r+p)*cos((R-r)/r*t)

def formulaY(R, r, p, t):
    y = (R-r)*sin(t) - (r+p)*sin((R-r)/r*t)

def t_iterating(R, r, p):
    t = 2*pi
    up()
    goto(formulaX, formulaY)
    down()

    while (True):
        t = t+0.01
        formulaX(R, r, p, t)
        formulaY(R, r, p, t)


def main():
    R = int(input("The radius of the fixed circle: "))
    r = int(input("The radius of the moving circle: "))
    p = int(input("The offset of the pen point, between <10 - 100>: "))

    if p < 10 or p > 100:
        input("Incorrect value for p!")

    t_iterating(R, r, p)

    input("Hit enter to close...")

main()