# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:23:20 2024

@author: Hp
"""

class RobotModel:
    def __init__(self):

        self.elevation = 0
        self.rotation = 1
        self.length = 2
        self.is_moving = False

    def move_elevation(self, elevation):
        
        self.elevation = elevation
        
    def move_rotation(self, rotation):
        
        self.rotation = rotation
        
    def move_length(self, length):
        
        self.length = length
        
    def stop_movement(self):
        
        self.is_moving = False
