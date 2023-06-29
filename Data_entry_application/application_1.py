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
        def control(select):
            if re.search("[^1-4]",select):
                raise Exception("Please choose a number between 1 and 4")
            elif len(select)!= 1:
                raise Exception("Please choose a number between 1 and 4")
        while True:
            try:
                select = input("Hello, {} welcome. \n\n Please select the option you want to make.. \n\n [1]- Add data\n [2]- Delete data\n [3]- Read data\n [4]-Exit\n\n".format(self.programName))
                control(select)
            except Exception as exc:
                print(exc)
                time.sleep(3)
            else:
                break
            return select

    def data_add(self):
        def controlName(name):
            if name.isalpha() == False:
                raise Exception("Entry only alphabetic characters.")
        while True:
            try:
                name = input("Name: ")
                controlName(name)
            except Exception as exc_name:
                print(exc_name)
                time.sleep(3)
            else:
                break
        
        def controlSurname(surname):
            if name.isalpha() == False:
                raise Exception("Entry only alphabetic characters.")
        while True:
            try:
                name = input("Surname: ")
                controlSurname(surname)
            except Exception as exc_surname:
                print(exc_surname)
                time.sleep(3)
            else:
                break

        def controlAge(age):
            if age.isdigit() == False:
                raise Exception("Enter only numeric characters.")
        while True:
            try:
                name = input("Age: ")
                controlAge(age)
            except Exception as exc_age:
                print(exc_age)
                time.sleep(3)
            else:
                break
        
        def controlID(identity):
            if identity.digit() == False:
                raise Exception("Enter only numeric characters.")
        while True:
            try: 
                identity = input("Identity: ")
                controlID(identity)
            except Exception as exc_ID:
                print(exc_ID)
                time.sleep(3)
            else:
                break

        def controlMail(Mail):
            if not re.search("@" and ".com",Mail):
                raise Exception("PLease enter a valid email address")
        while True:
            try:
                Mail = input("Mail")
                controlMail(Mail)
            except Exception as exc_Mail:
                print(exc_Mail)
                time.sleep(3)
            else:
                break
        

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