import re
import time


class data_input:
    def __init__(self,programName):
        self.programName = programName
        self.loop = True

    def program(self):
        select = self.menu()

        if select == "1":
            print("Data entry menu activated.")
            time.sleep(3)
            self.data_add()

        if select == "2":
            print("Data delete menu activated.")
            time.sleep(3)
            self.data_del()

        if select == "3":
            print("Data read menu activated.")
            time.sleep(3)
            self.data_read()

        if select == "4":
            self.exit()

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