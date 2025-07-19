from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

Motor_de = Motor(Port.B)
Motor_iz= Motor(Port.A)
sensor_de = ColorSensor(Port.D)
sensor_iz = ColorSensor(Port.C)
sensor_fr = ColorSensor(Port.F)

while True:
    print("Derecho", sensor_de.reflection())
    print("Izquierdo", sensor_iz.reflection())
    if sensor_de.reflection() > 90: 
        Motor_de.dc(50)
    if sensor_iz.reflection() > 90:
        Motor_iz.dc(-50)
    if sensor_de.reflection() < 90: 
        Motor_de.dc(-40)  
    if sensor_iz.reflection() < 90:
        Motor_iz.dc(40)
    




