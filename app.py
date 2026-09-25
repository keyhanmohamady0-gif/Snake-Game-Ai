from turtle import *
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os
from random import randint

food = Turtle()
food.shape('circle')

setup(500, 500)
delay(0)

up()
goto(-200, 200)

x = 200

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model_trained = False
AI_MODE = False

if os.path.exists("X_train.npy"):
    X = list(np.load("X_train.npy", allow_pickle=True))
else:
    X = []

if os.path.exists("y_train.npy"):
    y = list(np.load("y_train.npy", allow_pickle=True))
else:
    y = []

print("lastest data : ", len(X))

for f in range(10):
    for i in range(8):
        dot(5, 'gray')
        fd(50)
        dot(5, 'gray')
    goto(-200, x)
    x -= 50

goto(0, 0)
shape('turtle')

score = 0
title(f'Score : {score}')


def checkTurtle():
    global TurtlePlace, score

    TurtleX = round(xcor() / 50) + 4
    TurtleY = round(ycor() / 50) + 4

    TurtlePlace = np.zeros((9, 9), dtype="int64")

    TurtlePlace[abs(TurtleY - 8)][TurtleX] = 1

    FoodX = round(food.xcor() / 50) + 4
    FoodY = round(food.ycor() / 50) + 4

    TurtlePlace[abs(FoodY - 8)][FoodX] = 2
    print(TurtlePlace)
    if abs(FoodY - 8) == abs(TurtleY - 8) and FoodX == TurtleX:
        score += 1
        title(f'Score : {score}')
        getfood()

    return TurtlePlace


def getfood():
    while True:
        FoodX = randint(-4, 4)
        FoodY = randint(-4, 4)

        if FoodX * 50 != xcor() or FoodY * 50 != ycor():
            break

    food.up()
    food.goto(FoodX * 50, FoodY * 50)


def up():
    if ycor() < 160:

        if not AI_MODE:
            X.append(TurtlePlace.flatten())
            y.append(0)

            np.save('X_train.npy', np.array(X))
            np.save('y_train.npy', np.array(y))

        seth(90)
        fd(50)
        checkTurtle()


def down():
    if ycor() > -160:

        if not AI_MODE:
            X.append(TurtlePlace.flatten())
            y.append(1)

            np.save('X_train.npy', np.array(X))
            np.save('y_train.npy', np.array(y))

        seth(270)
        fd(50)
        checkTurtle()


def Left():
    if xcor() > -160:

        if not AI_MODE:
            X.append(TurtlePlace.flatten())
            y.append(2)

            np.save('X_train.npy', np.array(X))
            np.save('y_train.npy', np.array(y))

        seth(180)
        fd(50)
        checkTurtle()


def Right():
    if xcor() < 160:

        if not AI_MODE:
            X.append(TurtlePlace.flatten())
            y.append(3)

            np.save('X_train.npy', np.array(X))
            np.save('y_train.npy', np.array(y))

        seth(0)
        fd(50)
        checkTurtle()


def ai_predict():

    state = TurtlePlace.flatten().reshape(1, -1)

    prediction = model.predict(state)[0]

    print("AI prediction:", prediction)

    return prediction


def ai_move():

    if not model_trained:
        return

    prediction = ai_predict()

    if prediction == 0 and ycor() < 160:
        up()

    elif prediction == 1 and ycor() > -160:
        down()

    elif prediction == 2 and xcor() > -160:
        Left()

    elif prediction == 3 and xcor() < 160:
        Right()

    else:
        goto(0,0)


def train_model():
    global model_trained

    if len(X) == 0:
        print("Data is empty")
        return

    if len(set(y)) < 2:
        print("At least 2 different movements are required")
        return

    model.fit(np.array(X), np.array(y))

    model_trained = True

    print("Training Done right")
    print("Data Lenght", len(X))
    


def ai_loop():

    if AI_MODE:
        ai_move()
        ontimer(ai_loop, 300)


def start_ai():

    global AI_MODE

    if not model_trained:
        print("first train Ai")
        return

    if AI_MODE:
        return

    AI_MODE = True
    ai_loop()


def stop_ai():

    global AI_MODE

    AI_MODE = False


getfood()
checkTurtle()

onkeypress(up, 'Up')
onkeypress(down, 'Down')
onkeypress(Left, 'Left')
onkeypress(Right, 'Right')

onkeypress(train_model, "t")
onkeypress(start_ai, "a")
onkeypress(stop_ai, "s")

listen()
mainloop()