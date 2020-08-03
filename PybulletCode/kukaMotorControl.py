import pybullet as p
import time
import pybullet_data
from kukaKey import KukaKey


class MotorControl:
    def __init__(self):
        self.index = [0,1,2,3,4,5,6]
        self.target = [1,2,3,4,5,6,7,8]
        self.force = 500
        self.a = KukaKey()
        self.kuka = p.loadURDF("kuka_iiwa/model.urdf")

    def Control(self):
        right_left, up_down, up_dow, rig_lef = self.a.IsPressed()

        self.target[0] = right_left
        p.setJointMotorControl2(self.kuka,
                                self.index[0],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[0],
                                force=self.force)

        self.target[1] = up_down
        p.setJointMotorControl2(self.kuka,
                                self.index[1],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[1],
                                force=self.force)

        self.target[2] = right_left
        p.setJointMotorControl2(self.kuka,
                                self.index[0],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[2],
                                force=self.force)

        self.target[3] = up_down
        p.setJointMotorControl2(self.kuka,
                                self.index[1],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[3],
                                force=self.force)

        self.target[4] = rig_lef
        p.setJointMotorControl2(self.kuka,
                                self.index[2],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[4],
                                force=self.force)

        self.target[5] = rig_lef
        p.setJointMotorControl2(self.kuka,
                                self.index[2],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[5],
                                force=self.force)                                                                                                        

        self.target[6] = up_dow
        p.setJointMotorControl2(self.kuka,
                                self.index[3],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[6],
                                force=self.force)

        self.target[7] = up_dow
        p.setJointMotorControl2(self.kuka,
                                self.index[3],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[7],
                                force=self.force)

        p.setJointMotorControl2(self.kuka,
                                self.index[4],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[6],
                                force=self.force)  

        p.setJointMotorControl2(self.kuka,
                                self.index[4],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[7],
                                force=self.force)

        p.setJointMotorControl2(self.kuka,
                                self.index[5],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[6],
                                force=self.force)                                                                                              

        p.setJointMotorControl2(self.kuka,
                                self.index[5],
                                p.POSITION_CONTROL,
                                targetPosition=self.target[7],
                                force=self.force)
