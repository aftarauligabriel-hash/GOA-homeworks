from turtle import*
#step one: draw a square
width(7)
color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(200)
#we want to paint a house
left(90)
#and of square

#drawing a door





forward(70)


color("yellow")
begin_fill()

left(90)
forward(100)   #height of the door
right(90)
forward(60)





right(90)
forward(100)
end_fill()



penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(120)

forward(120)
left(60)

forward(115)

end_fill()


penup()
goto(180, 150)
pendown()
left(60)
#painting a window

color("blue")
begin_fill()
forward(40)

right(90)

forward(40)

right(90)

forward(40)

right(90)

forward(40)
end_fill()
#painting a second window

color("blue")
begin_fill()
penup()
goto(60, 106)
pendown()

left(90)

forward(40)

left(90)

forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()



exitonclick()