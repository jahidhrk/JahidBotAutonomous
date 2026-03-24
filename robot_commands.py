# robot_commands.py
# Movement and fight functions for JahidBot
import time

def punch(arduino, engine):
    engine.say("Punch!")
    engine.runAndWait()
    arduino.write(b'P')
    time.sleep(0.5)

def kick(arduino, engine):
    engine.say("Kick!")
    engine.runAndWait()
    arduino.write(b'K')
    time.sleep(0.5)

def walk_forward(arduino, engine):
    engine.say("Walking forward")
    engine.runAndWait()
    arduino.write(b'F')
    time.sleep(0.5)

def walk_backward(arduino, engine):
    engine.say("Walking backward")
    engine.runAndWait()
    arduino.write(b'B')
    time.sleep(0.5)
