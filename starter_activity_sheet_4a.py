from turtle import *

def square():
    color('red', 'green')
    begin_fill()
    for _ in range(4):
        forward(200)
        right(90)
    end_fill()
    done()

def triangle():
    color('blue', 'yellow')
    begin_fill()
    for _ in range(3):
        forward(200)
        right(120)
    end_fill()
    done()

def square_triangle():
    color('red', 'green')
    begin_fill()
    for _ in range(4):
        forward(200)
        right(90)
    end_fill()
    penup()
    forward(200)
    pendown()
    color('blue', 'yellow')
    begin_fill()
    for _ in range(3):
        forward(200)
        right(120)
    end_fill()
    done()

choice = input("Which shape do you want to draw? (square/triangle/both): ").strip().lower()

if choice == "square":
    square()
elif choice == "triangle":
    triangle()
elif choice == "both":
    square_triangle()
else:
    print("Invalid choice.")
