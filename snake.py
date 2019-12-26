import turtle, time
from init import *  

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
	move()
	time.sleep(delay)

wn.mainloop()
