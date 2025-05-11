from turtle import Turtle, Screen
import random
race_on = False
turtle_list = []
color = ["green", "red", "orange", "yellow", "blue", "purple"]
set_y = -500
screen = Screen()
user_input = screen.textinput(title= "Make your bet", prompt = "What colour do you like? Enter your colour: ")
if user_input:
    race_on = True

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.shapesize(stretch_len= 3, stretch_wid= 3)
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -900, y = set_y)
    set_y += 200
    turtle_list.append(new_turtle)

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 920:
            if turtle.pencolor() == user_input:
                game_announcement = f"You win! The winning turtle is {turtle.pencolor()}"
                print(game_announcement)
            else:
                game_announcement = f"You lose! The winning turtle is {turtle.pencolor()}"
                print(game_announcement)
            race_on = False
            break
        else:
            turtle.forward(random.randint(0,10))












screen.exitonclick()