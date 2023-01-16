import turtle
def koch_curve(t, iterations, length, shortening_factor, angle):
    if iterations == 0:
        t.forward(length)
    else:
        iterations = iterations - 1
        length = length / shortening_factor    
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.right(angle * 2)
        koch_curve(t, iterations, length, shortening_factor, angle)
        t.left(angle)


t = turtle.Turtle()
t.speed(0)
t.hideturtle()

for i in range(3):
  koch_curve(t, 400, 600, 5, 81)
  t.right(120)
  turtle.mainloop()