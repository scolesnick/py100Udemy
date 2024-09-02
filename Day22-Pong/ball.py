from turtle import Turtle

MOVE_DISTANCE = 5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
        self.x_increment = MOVE_DISTANCE
        self.y_increment = MOVE_DISTANCE
        self.move_speed = 0.03

    def move(self):
        self.wall_collision()
        new_x = self.xcor() + self.x_direction*self.x_increment
        new_y = self.ycor() + self.y_direction*self.y_increment
        self.goto(new_x,new_y)

    def wall_collision(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_direction *= -1

    def paddle_collision(self, paddle):
        p_x = paddle.xcor()
        p_y = paddle.ycor()
        b_x = self.xcor()
        b_y = self.ycor()

        # This lets the ball bounce off of the side of the paddle rather than in the middle
        x_bound = p_x-10*self.x_direction
        if (p_y - 50 <= b_y <= p_y + 50 ) and b_x == x_bound:
            self.x_direction *= -1
            self.move_speed *= 0.9


    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.03
        self.x_direction *= -1