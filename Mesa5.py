from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

Motor_de = Motor(Port.E)
Motor_iz= Motor(Port.A)
sensor_de = ColorSensor(Port.D)
sensor_iz = ColorSensor(Port.C)
sensor_fr = ColorSensor(Port.F)

hub.imu.reset_heading(0)


Color.WHITE = Color(h=0, s=0, v=100)
Color.BLACK = Color(h=205, s=18, v=28)
Color.GREEN = Color(h=162, s=75, v=52)
my_colors = (Color.BLACK,Color.WHITE,Color.GREEN)

sensor_de.detectable_colors(my_colors)

sensor_iz.detectable_colors(my_colors)

sensor_fr.detectable_colors(my_colors)

while True:
    print(hub.imu.heading())
    hub.imu.reset_heading(0)
    while hub.imu.heading() > -90:
      Motor_de.run(80)
      Motor_iz.run(80)
      
    break
print("ñlkjhgfv")

while True:
    print("Derecho", sensor_de.reflection())
    print("Izquierdo", sensor_iz.reflection())
    if sensor_de.reflection() > 90: 
        Motor_de.dc(30)
    else: 
        Motor_de.dc(-30)
    if sensor_iz.reflection() > 90:
        Motor_iz.dc(-30)
    else:
        Motor_iz.dc(30) 
        """   
    if sensor_de.reflection() < 90:
        Motor_de.dc(-20)  
    if sensor_iz.reflection() < 90:
        Motor_iz.dc(20)
    """



























