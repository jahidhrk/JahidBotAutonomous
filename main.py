# main.py
# JahidBot by Jahid Hassan Rakib
import serial
import time
import pyttsx3
from robot_commands import *

engine = pyttsx3.init()
engine.say("JahidBot activated")
engine.runAndWait()

# Connect to Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # wait for Arduino

# Simple control loop
print("Use commands: punch, kick, walk_forward, walk_backward, exit")
while True:
    cmd = input("Command: ").lower()
    if cmd == "exit":
        break
    elif cmd == "punch":
        punch(arduino, engine)
    elif cmd == "kick":
        kick(arduino, engine)
    elif cmd == "walk_forward":
        walk_forward(arduino, engine)
    elif cmd == "walk_backward":
        walk_backward(arduino, engine)
    else:
        engine.say("Unknown command")
        engine.runAndWait()
