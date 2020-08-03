import pybullet as p
import time
import numpy as np 

p.connect(p.GUI)


class KukaKey:
    
    def __init__(self):
        self.up_down = 0
        self.right_left = 0

        self.rig_lef = 0
        self.up_dow = 0

    def IsPressed(self):
        
        keys = p.getKeyboardEvents()

        if keys.get(65297):
            self.up_down -=0.1
            if self.up_down < -4:
                self.up_down = -4
            
            # return self.up
            

        if keys.get(65298):
            self.up_down += 0.1
            if self.up_down > 4:
                self.up_down = 4
               
            # return self.down
           

        if keys.get(65296):
            self.right_left += 0.1
            if self.right_left > 4:
                self.right_left = 4
         
            print("R:",self.right_left)    
                
            # return self.right
        

        if keys.get(65295):
            self.right_left -= 0.1
            if self.right_left < -4:
                self.right_left = -4
             
            print("L:",self.right_left)    
            # return self.left


        if keys.get(97):
            self.rig_lef +=0.1
            if self.rig_lef > 4:
                self.rig_lef = 4 

        if keys.get(100):
            self.up_dow +=0.1
            if self.up_dow > 4:
                self.up_dow = 4

        if keys.get(111):
            self.up_dow -=0.1
            if self.up_dow < -4:
                self.up_dow = -4        

        if keys.get(116):
            self.rig_lef -=0.1
            if self.rig_lef < -4:
                self.rig_lef = -4                   

        # return pad(self.up, self.down, self.right,self.left)
        return self.right_left, self.up_down, self.up_dow, self.rig_lef

    


    
             

         

                 
         
                          
