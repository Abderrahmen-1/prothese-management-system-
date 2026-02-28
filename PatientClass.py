#from SqlConnection import cursor, connection
from UsufulFunctions import *
from DentistClass import addToFile

class Patient:

    def __init__(self,cursor,connection):
        self.__cursor = cursor
        self.__connection = connection

    def AddPatient(self):
        first_name, last_name = Get_names()

        # Check if patient number exists
        while True:
            number = Get_ID()
            self.__cursor.execute("SELECT COUNT(*) FROM Patient WHERE patient_number = %s", (number,))
            exist = self.__cursor.fetchone()[0]
            if exist > 0:
                print("User already exists")
            else:
                break

        # Get choice and price
        choice, price = self.Get_Patient_Choice()
        date = Get_Date()

        # Input khalsa
        while True:
            khalsa = input("Did the patient khelsek? (yes/no) ").lower()
            if khalsa in ['yes', 'no']:
                break
        khalsa_str = 'yes' if khalsa == 'yes' else 'no'

        versa = price if khalsa_str == 'yes' else 0

        # Input versa if khalsa is no
        if khalsa_str == 'no':
            while True:
                Versa = input("Did the patient versa drahem? (yes/no) ").lower()
                if Versa in ['yes', 'no']:
                    break
            if Versa == 'yes':
                while True:
                    try:
                        versa = float(input("How much? "))
                        if versa < 0 or versa > price:
                            raise ValueError("Invalid amount")
                        break
                    except ValueError as e:
                        print(e)

        b9aw = price - versa if khalsa_str == 'no' else 0
        if b9aw == 0 :
            patient_infos = (first_name, last_name, number, choice, date, False, 'yes', versa, b9aw)
        else :
            patient_infos = (first_name, last_name, number, choice, date, False, 'no', versa, b9aw)

        # Insert into Patient table
        sqlp = """
            INSERT IGNORE INTO Patient(
                patient_firstname, patient_lastname, patient_number,
                T_ype , la_date, finished, khalsa, versa, b9aw
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.__cursor.execute(sqlp , patient_infos)
        self.__connection.commit()

        # Insert into Khedma table
        khedma_infos = (choice, price, date, 'NO', number, 'no', khalsa_str)

        sqlk = """
            INSERT INTO Khedma(
                khedman, khedma_price, khedma_date,
                khedma_dentist, khedma_patient, khedma_wajda, khedma_khalsa
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.__cursor.execute(sqlk , khedma_infos)
        self.__connection.commit()

    def Get_Patient_Choice(self):
        choice, price = Get_Choice()
        #addToFile(choice)
        return choice, price