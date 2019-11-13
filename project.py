import turtle
from JungFunctions import*
turtle.colormode(255)

bob.width(10)
bob.speed(0)

x= -750
y= 750
jump(x,y)
for times in range(255):
    c = (25,25,times)
    bob.color(c)
    bob.forward(2000)
    jump(x,y-times*6)

bob.width(1)


jump(-90,50)
#yellow firework
for times in range(255):
    bob.color(210,times,30)
    bob.forward(150)
    bob.right(169)


jump(130,120)
#green firework
for times in range(255):
    bob.color(110,210,times)
    bob.forward(150)
    bob.right(169)
    
jump(-80,220)
#blue firework
for times in range(255):
    bob.color(times,190,255)
    bob.forward(150)    
    bob.right(169)

jump(-200,-50)
#green firework
for times in range(255):
    bob.color(110,210,times)
    bob.forward(150)
    bob.right(169)

jump(80,-165)
#blue firework
for times in range(255):
    bob.color(times,190,255)
    bob.forward(150)    
    bob.right(169)

jump(210,30)
#right side
for times in range(255):
    bob.color(times,45,125)
    bob.forward(100)
    bob.right(169)

jump(360,120)
for times in range(255):
    bob.color(200,times,250)
    bob.forward(150)
    bob.right(169)

jump(430,30)
for times in range(255):
    bob.color(20,times,198)
    bob.forward(130)
    bob.right(169)

jump(630,-10)
for times in range(255):
    bob.color(times,90,170)
    bob.forward(100)
    bob.right(169)

#left side
jump(-150,75)
for times in range(255):
    bob.color(times,45,125)
    bob.forward(100)
    bob.right(169)

jump(-450,80)
for times in range(255):
    bob.color(200,times,250)
    bob.forward(150)
    bob.right(169)

jump(-560,-20)
for times in range(255):
    bob.color(20,times,198)
    bob.forward(130)
    bob.right(169)

jump(-610,30)
for times in range(255):
    bob.color(times,90,170)
    bob.forward(100)
    bob.right(169)

#top
jump(-25,350)
for times in range(255):
    bob.color(times,45,125)
    bob.forward(100)
    bob.right(169)
    
#bottom
jump(-55,-250)
for times in range(255):
    bob.color(times,45,125)
    bob.forward(100)
    bob.right(169)
