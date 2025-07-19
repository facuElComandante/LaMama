from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

motorizq = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motorder = Motor(Port.F)

sensor = ColorSensor(Port.C)

while True:
    color = sensor.color()
    print(color)
    if color == Color.BLUE:
        motorder.run(100)
        motorizq.run(100)
        wait(500)
    elif color == Color.WHITE: 
        motorder.stop()
        motorizq.stop()
    wait(100)