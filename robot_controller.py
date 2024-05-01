# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:26:43 2024

@author: Hp
"""

class RobotController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process_command(self):
        elevation, rotation, length = self.view.get_user_input()
        try:
            self.model.move_elevation(elevation)
            self.model.move_rotation(rotation)
            self.model.move_length(length)
        except ValueError as e:
            self.view.show_error_message(str(e))

    def stop_movement(self):
        self.model.stop_movement()

    def run(self):
        while True:
            command = input("Ingrese un comando (mover/detener): ")
            if command == "mover":
                self.process_command()
            elif command == "detener":
                self.stop_movement()
                break
