import pybullet as p
import time
import pybullet_data
from kukaMotorControl import MotorControl


p.connect(p.DIRECT)
p.resetSimulation()
p.setRealTimeSimulation(1)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
p.loadURDF("plane.urdf")

b = MotorControl()

while (1):

  time.sleep(0.05)
  b.Control()
  
