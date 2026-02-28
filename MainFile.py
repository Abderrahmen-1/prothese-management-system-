from AddSel3a import *
from FinishedFile import *
from KhalsaFile import *
from SqlConnection import *
from PatientClass import *
from DentistClass import *


class InvalideChoiceException(Exception):
    pass


print("ABDERRAHMEN")

patient = Patient(cursor,connection)
dentist = Dentist(cursor,connection)

while True :
    while True:
        try:
            choice = int(input("what you wanna do ? : \n"
                               " 1) Add_Patient \n"
                               " 2) Del_Patient \n"
                               " 3) Add_Dentist \n"
                               " 4) Bring_From_Dentist \n"
                               " 5) Add_Sel3a \n"
                               " 6) finished \n"
                               " 7) khalsa \n"
                               " 8) send_Whatsapp \n"
                               " 0) exit \n"))
            if choice > 7 or choice < 0:
                raise InvalideChoiceException
            break

        except ValueError:
            print("must enter a number ")
            continue

        except InvalideChoiceException as e:
            print("you can just put [ 1 , 2 , 3 , 4 , 5 , 6 or 7 ] ")
            continue

    if choice == 1 :
        patient.AddPatient()
    elif choice == 3 :
        dentist.AddTable()
    elif choice == 4 :
        dentist.Get_From_Dentist()
    elif choice == 5 :
        addSel3a()
    elif choice == 6 :
        Finished()
    elif choice == 7:
        Khalsa()
    elif choice == 0 :
        break
        
print("\n\n\n")

sql = """
         SELECT * FROM Patient ; 
         """
cursor.execute(sql)

for row in cursor.fetchall():
    print(row)

print("\n\n\n")

sql = """
        SELECT * FROM Khedma 
        """
cursor.execute(sql)

for row in cursor.fetchall():
    print(row)


connection.commit()










