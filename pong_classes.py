from turtle import Turtle, Screen, ycor

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")


class Paddle(Turtle):

    def __init__(self, coord):
        
        super().__init__()
        self.penup()
        self.goto(coord)
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+25)


    def move_down(self):
        self.goto(self.xcor(), self.ycor()-25)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.p1 = 0
        self.p2 = 0

    def refresh_score(self):
        self.clear()
        self.write(f"P1: {self.p1} | P2: {self.p2}", False, "center", font=('Courier', 17,'bold'))



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(20)
        self.color("white")
        self.shape("circle")
        self.shapesize(0.7, 0.7)
        self.y_direction = 0.50
        self.x_direction = 0.50
    
    def move(self):

        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_direction *= -1

        self.goto(self.xcor()+self.x_direction, self.ycor()+self.y_direction)

    # resetta la posizione della pallina quando un giocatore fa punto
    def reset_position(self):
        self.home()
        self.x_direction *= -1
        