'''
Obstacle program for the Finch robot
Written by Wyatt Miller
Copyright (c) 2017, MIT

Read the intro message to get a breif run down what this program does.
This does somewhat the wanderer.py file does, but with FUNCTIONS!
And other added stuff...
You need Python 3 and the Finch robot!
Don't have a Finch? http://www.finchrobot.com
Don't have Python?? www.python.org
'''

from finch import Finch
from time import time, sleep

finch = Finch() # Initialize!

# Blinking blue lights!
finch.led(0, 0, 255)
sleep(0.2)
finch.led(0, 0, 0)
sleep(0.2)
finch.led(0, 0, 255)
sleep(0.2)
finch.led(0, 0, 0)
sleep(0.2)
finch.led(0, 0, 255)
sleep(0.2)
finch.led(0, 0, 0)
sleep(0.2)
finch.led(0, 0, 255)

# Intro message, blah blah blah
print('Welcome to the Finch obstacle program!')
print('This robot is called [the] Finch, made by BirdBrain Technologies.')
print("It's a program that the Finch moves and when it detects an obstacle, ")
print('the Finch will stop, go in reverse, and goes forward again. That is it!')
sleep(3)
print("**STATUS** Finch has started!")

# Fuctions, yay
def startFinch():
    finch.led(0, 255, 0)
    finch.wheels(1.0, 1.0)
    sleep(0.1)

def checkObstacle():
    while True:
        left_obstacle, right_obstacle = finch.obstacle()
        if left_obstacle:
            print('**STATUS** Finch is turning left!')
            finch.led(255, 0, 0)
            finch.wheels(-1.0, -0.3)
            sleep(1.2)
            finch.wheels(0, 0)
            startFinch()
        elif right_obstacle:
            print('**STATUS** Finch is turning right!')
            finch.led(255, 0, 0)
            finch.wheels(-0.3, -1.0)
            sleep(1.2)
            finch.wheels(0, 0)
            startFinch()
        else:
            pass

# Starting functions...
startFinch()
checkObstacle()
