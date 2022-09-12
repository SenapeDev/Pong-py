from pong_classes import *

game_on = True
player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(player1.move_up, "Up")
screen.onkeypress(player1.move_down, "Down")
screen.onkeypress(player2.move_up, "w")
screen.onkeypress(player2.move_down, "s")

while game_on:
    screen.update()
    scoreboard.refresh_score()
    
    # se la palla colpisce il paddle del giocatore
    if ball.distance(player1) <= 50 and ball.xcor() >= 340 or ball.distance(player2) <= 50 and ball.xcor() <= -340:
        ball.x_direction *= -1

    # se supera il bordo sinistro, assegna il punteggio e riavvia la partita
    if ball.xcor() >= 365:
        scoreboard.p1 += 1
        ball.reset_position()

    # se supera il bordo destro, assegna il punteggio e riavvia la partita
    if ball.xcor() <= -365:
        scoreboard.p2 += 1
        ball.reset_position()

    ball.move()