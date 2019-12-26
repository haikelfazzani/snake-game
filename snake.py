import time, random
from init import *  

segments = []

# Snake move
def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

# keyboard handling
def go_up():
	head.direction = "up"
def go_down():
	head.direction = "down"
def go_left():
	head.direction = "left"
def go_right():
	head.direction = "right"

wn.listen()
wn.onkeypress(go_up, "z")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "d")

# Main
while True:
	wn.update()

	# check for collision with food
	if head.distance(food) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color('grey')
		new_segment.penup()
		segments.append(new_segment)

	for index in range(len(segments)-1, -1,-1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move()
	time.sleep(delay)

wn.mainloop()
