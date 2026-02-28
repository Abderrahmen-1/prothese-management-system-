from SqlConnection import *
from UsufulFunctions import *

class InvalideDateException(Exception):
    pass

class InvalidePriceException(Exception):
    pass

class InvalideNameException(Exception):
    pass

class InvalideIdException(Exception):
    pass

def addToFile(choice):
    with open ("khedma.txt" , "a+") as file :
        file.seek(0) # we wanna go to the first line in the file

        content = file.read()
        if choice not in content :
            file.write(choice + "\n")

def Get_names() -> list :
    while True :
        try:
            firstname = input("put the patient first name :")
            lastname = input("put the patient last name : ")
            if not firstname.strip() or not lastname.strip():
                raise InvalideNameException
            break
        except ValueError:
            print("name must not be empty ")
            continue
        except InvalideNameException as e:
            print("name must not be empty ")
            continue

    return [firstname , lastname]


def Get_ID() -> int :
    while True:
        try:
            unique = input("whats the unique number of the patient ?? : ")
            if len(unique) <= 4 or not unique.isdigit() or int(unique) < 0 :
                raise InvalideIdException
            break
        except ValueError:
            print("the id must be a number ")
            continue
        except InvalideIdException as e:
            print("Invalide unique number ")
            continue

    return unique

def Get_Price(choice):
    while True:
        try:
            price = float(input(f"whats the price of the {choice} ?? "))
            if price < 0:
                raise InvalidePriceException
            break
        except ValueError:
            print("invalide price ")
            continue
        except InvalidePriceException as e:
            print("Invalide price ")
            continue
    return price


def Get_Choice():
    while True:
        try:
            choice = input("what the work that you toke it ?? :").strip()
            if not choice.strip():
                raise InvalideNameException
            break
        except ValueError:
            print("Invalide choice ")
            continue
        except InvalideNameException as e:
            print("the choice must not be empty ")
            continue

    addToFile(choice)
    price = Get_Price(choice)
    return [choice, price]


def Get_Date():
    while True:
        try:
            day = int(input("put the day of the enter : "))
            mouth = int(input("put the mouth : "))
            year = int(input("put the year : "))

            if year < 2025 or mouth < 0 or mouth > 12:
                raise InvalideDateException

            if mouth in [1, 3, 5, 7, 8, 10, 12]:
                if day > 31 or day < 0:
                    raise InvalideDateException
            elif mouth in [4, 6, 9, 11]:
                if day < 0 or day > 30:
                    raise InvalideDateException
            elif mouth == 2:
                if year % 4 == 0:
                    if day < 0 or day > 29:
                        raise InvalideDateException
                else:
                    if day < 0 or day > 28:
                        raise InvalideDateException
            break

        except InvalideDateException as e :
            print("Invalide DATE ")

    date = str(year) + "-" + str(mouth) + "-" + str(day)

    return date


class Dentist:

    def __init__(self,cursor,connection):
        self.__cursor = cursor
        self.__connection = connection

    def AddTable(self):
        new_name = input("what is the name of the new dentist ?? : ").strip().lower()

        sqladd = f"""  CREATE TABLE IF NOT EXISTS {new_name}(
                       id INT PRIMARY KEY AUTO_INCREMENT ,
                       patient_firstname VARCHAR(50),
                       patient_lastname VARCHAR(50),
                       patient_number VARCHAR(20) UNIQUE,
                       Dkhedma VARCHAR(50) ,
                       price FLOAT ,
                       finished VARCHAR(10) ,
                       khalsa VARCHAR(10) ,
                       date DATE  
                       );    
        """

        new_table = cursor.execute(sqladd)
        print("Dentist Added")


    def Get_Dentist_Choice(self):
        choice , price = Get_Choice()
        return  choice , price


    def Get_From_Dentist(self):
        while True:
            dentist = input("wich dentist you toke a work from it ?? ").strip().lower()

            cursor.execute("""
                           SELECT 1 
                           FROM information_schema.tables 
                           WHERE table_schema = %s AND TABLE_NAME = %s 
                           LIMIT 1 
                           """, ('labo_sys', dentist))

            exist = cursor.fetchone()

            if exist:
                break
            else:
                print("dentist not found ")
                again = input("wanna try again ?? (put yes/no) : ")
                if again.lower() == 'no':
                    break


        choice , price = self.Get_Dentist_Choice()

        firstname , lastname = Get_names()

        unique = Get_ID()
        date = Get_Date()

        while True :
            khalsa = input("did the dentist khelsek ?? (put yes or no) ")
            if khalsa.lower() in ['yes' , 'no']:
                break


        sql = f"""
                     INSERT INTO {dentist}(patient_firstname , patient_lastname , patient_number , Dkhedma , price ,  finished , khalsa , date) 
                     VALUES (%s , %s , %s , %s , %s , %s , %s ,%s ) """

        if khalsa.lower() == 'yes':
            infos = (firstname, lastname, unique, choice, price , False, True, date)
        else:
            infos = (firstname, lastname, unique, choice, price , False, False, date)

        self.__cursor.execute(sql, infos)
        self.__connection.commit()

        # insirt into the KHEDMA table
        sqlk = """  INSERT INTO Khedma ( khedman , khedma_price , khedma_date ,
                                khedma_dentist , khedma_patient , khedma_wajda , khedma_khalsa ) 
                        VALUES (%s , %s , %s , %s , %s , %s  , %s )    """

        infos = (
            choice, price, date, f"Dr.{dentist}", unique, 'no' , khalsa
        )

        self.__cursor.execute(sqlk, infos)
        self.__connection.commit()

        print("KHEDMA ADDED")




