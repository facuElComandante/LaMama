from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

Motor_de = Motor(Port.A)
Motor_iz= Motor(Port.B)
# sensor_de = ColorSensor(Port.D)
# sensor_iz = ColorSensor(Port.C)
# sensor_fr = ColorSensor(Port.F)

hub.imu.reset_heading(0)
while True:
    print(hub.imu.heading())
    # hub.imu.reset_heading(0)
    # while hub.imu.heading() > -90:
    #     Motor_de.run(80)
    #     Motor_iz.run(80)
    # break

