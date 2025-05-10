import turtle as t
import random

violet = t.Turtle()
blue = t.Turtle()
green = t.Turtle()
yellow = t.Turtle()
orange = t.Turtle()
red = t.Turtle()

for turtle in t.turtles():
    turtle.shape("turtle")

violet.color('violet')
blue.color("blue")
green.color('green')
yellow.color("yellow")
orange.color("orange")
red.color("red")

y=200
for turtle in t.turtles():
    turtle.teleport(-250, y)
    y-=80

# violet.teleport(-200, 200)
# blue.teleport(-200, 150)
# green.teleport(-200, 100)
# yellow.teleport(-200, 50)
# orange.teleport(-200, 0)
# red.teleport(-200, -50)
all_turtles = [violet, blue, green, red, yellow, orange]
screen = t.Screen()
screen.title("Turtle Race")
user_bet = screen.textinput("bet", "Choose your turtle from the available colors")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        move = random.randint(0,30)
        turtles.forward(move)
        if(turtles.xcor() >= 250):
            is_race_on = False
            if user_bet == turtles:
                print("You Win!")
            else:
                print(f"You lose! The {turtles.pencolor()} turtle won the race.")
            break

screen.exitonclick()