from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: \nred, orange, yellow, green, blue, purple").lower()
colors= ["red", "orange", "yellow","green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
movement = [0, 5, 10]
turtle_players = []

if user_bet:
    is_race_on = True

# set variation details for each 6 turtle like color, andy position
# so 6 different turtles appear in the screen
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    turtle_players.append(new_turtle)

# make a while loop for the 6 turtles to actually move forward
# in each random pace
while is_race_on:

    for turtle in turtle_players:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won the race!")
                is_race_on = False
            else:
                print("You've lost the race...")
                is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()




