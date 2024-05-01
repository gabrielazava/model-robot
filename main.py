# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:49:49 2024

@author: Hp
"""

from robot_model import RobotModel
from robot_view import RobotView
from robot_controller import RobotController

model = RobotModel()
view = RobotView()
controller = RobotController(model, view)

controller.run()

