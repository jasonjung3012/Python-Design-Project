#game file
from gamelib import*

#variables
game= Game(800,600, "Basketball game")

bk= Image("basketball court.jpg",game)
bk.resizeTo(800,600)

player1= Image("jordan.png",game)
player1.resizeBy(-70)
player1.setSpeed(6,90)

player2= Image("lebron.png",game)
player2.resizeBy(-80)
player2.setSpeed(8,90)

ball= Image("basketball.jpg",game)
ball.resizeBy(-100)
#essential game loop
while not game.over:
    game.processInput()
    bk.draw()
    player1.move(True)
    player2.move(True)
    ball.draw()
    ball.moveTo(mouse.x, mouse.y)
    game.update(40)

game.quit()
