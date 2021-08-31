from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a snake made of 3 squares"""
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, i):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.goto(i)
        self.segments.append(self.segment)

    def extend_tail(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Gives the snake movement forwards"""
        for segment_nmbr in range (len(self.segments) - 1, 0, -1):
            x = self.segments[segment_nmbr-1].xcor()
            y = self.segments[segment_nmbr-1].ycor()
            self.segments[segment_nmbr].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        """Manda a la serpiente a un lugar inobservable. Limpia la lista y crea una nueva serpiente tss(sonido de serpiente)"""
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



    def right(self):
        """Makes the first segment face right or  0 degrees"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        """Makes the first segment face left or 180 degrees"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        """Makes the first segment face downwards or 270 degrees"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def up(self):
        """Makes the first segment face upwards or 90 degrees """
        if self.head.heading() != 270:
            self.head.setheading(90)