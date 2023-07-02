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
                surname = input("Surname: ")
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
                age = input("Age: ")
                controlAge(age)
            except Exception as exc_age:
                print(exc_age)
                time.sleep(3)
            else:
                break
        
        def controlID(identity):
            if identity.isdigit() == False:
                raise Exception("Enter only numeric characters.")
            elif len(identity)!= 11:
                raise Exception("Your ID number must consist of 11 digits.")
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
            if not re.search(".com", Mail):
                raise Exception("Please enter a valid email address")
            elif not re.search(".com",Mail):
                raise Exception("Please enter a valid email address")
        while True:
            try:
                Mail = input("Mail: ")
                controlMail(Mail)
            except Exception as exc_Mail:
                print(exc_Mail)
                time.sleep(3)
            else:
                break
        
        with open("C:/Users/ekvk4/Downloads/Python_Applications/Python_Applications/Data_entry_application/information.txt","r",encoding= "utf-8") as file:
            numberLines = file.readlines()
        if len(numberLines) == 0:
            Id = 1
        else:
            with open("C:/Users/ekvk4/Downloads/Python_Applications/Python_Applications/Data_entry_application/information.txt","r", encoding= "utf-8") as file:
                Id = int(file.readlines()[-1].split("-")[0])+1
                
        with open("C:/Users/ekvk4/Downloads/Python_Applications/Python_Applications/Data_entry_application/information.txt","a+", encoding= "utf-8") as file:
            file.write("{} {} {} {} {} {}\n".format(Id,name,surname,age,identity,Mail))
            print("The data has been processed.") 
        self.back_menu()

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