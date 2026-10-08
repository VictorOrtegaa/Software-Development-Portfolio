from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]


def play_game():
    screen.clear()
    screen.setup(width=500, height=400)
    is_race_on = False
    u_bet = screen.textinput(title="Make THE bet", prompt=" Which turtle will win the race? Enter a color: ")
    all_turtles = []
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, 160)
    writer.color("Darkblue")
    writer.write("PLACE YOUR BET ON A TURTLE!!!", align="center", font=("Arial", 16, "bold"))

    writer.goto(220, 140)
    writer.setheading(270)
    writer.pensize(3)
    writer.color("black")

    for _ in range(14):
        writer.pendown()
        writer.forward(10)
        writer.penup()
        writer.forward(10)


    writer.goto(220, 145)
    writer.write("FINISH ", align="center", font=("Arial", 9, "bold"))

    for i in range(6):
        timmy = Turtle(shape="turtle")
        timmy.penup()
        timmy.color(colors[i])
        timmy.goto(x=-230, y=y_positions[i])
        all_turtles.append(timmy)

    if u_bet:
        is_race_on = True

    while is_race_on:
        for t in all_turtles:
            if t.xcor() > 230:
                is_race_on = False
                winning_color = t.pencolor()
                if winning_color == u_bet.lower():
                    message = f"You've won the race! The {winning_color} turtle is the winner!\n\nPress 'SPACE' to play again."
                else:
                    message = f"You've lost buddy! The {winning_color} turtle is the winner!\n\nPress 'SPACE' to play again."
                writer.goto(0, 0)
                writer.write(message, align="center", font=("Arial", 12, "bold"))
                break

            rand_distance = random.randint(0, 10)
            t.forward(rand_distance)

    screen.listen()
    screen.onkey(key="space", fun=play_game)


play_game()

screen.exitonclick()
