import turtle  # Import badal diya

t = turtle.Turtle()
t.speed(500)  # Speed tez karne ke liye (optional)
# 1. Screen setup (Window tayyar karna)
screen = turtle.Screen()
screen.bgcolor("black")       # Background color black set kiya
screen.title("My First Turtle Program")

for steps in range(200): 
    for c in ('blue', 'red'):
        t.color(c)
        t.forward(steps)
        t.right(60)

# Ye line window ko rok ke rakhegi jab tak aap cross (X) pe click nahi karte
turtle.done()