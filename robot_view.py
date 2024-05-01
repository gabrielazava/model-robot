# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:25:14 2024

@author: Hp
"""

class RobotView:
    def get_user_input(self):
        # Obtener los valores
        elevation = input("Ingrese el valor de elevación: ")
        rotation = input("Ingrese el valor de giro: ")
        length = input("Ingrese el valor de longitud: ")
        return elevation, rotation, length

    def show_error_message(self, error_message):
        # Mensaje de error en caso de que ocurra alguna operación incorrecta
        print("Error:", error_message)
