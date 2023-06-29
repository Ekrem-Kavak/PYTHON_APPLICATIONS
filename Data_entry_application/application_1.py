import re
import time


class data_input:
    def __init__(self,programName):
        self.programName = programName
        self.loop = True


    def program(self):
        pass

    def menu(self):
        pass

    def data_add(self):
        pass

    def data_del(self):
        pass

    def data_read(self):
        pass

    def exit(self):
        pass

    def back_menu(self):
        pass 




system = data_input("Data Entering System")
while system.loop:
    system.program()