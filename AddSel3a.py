from SqlConnection import *
from UsufulFunctions import *



class InvalidePriceException(Exception):
    pass

def addSel3a():

    name = input("whats the name of sel3a : ")

    while True :
        try :
            price = float(input("whats the price : "))
            if price < 0 :
                raise InvalidePriceException
            break

        except ValueError :
            print("enter a number :")
            continue
        except InvalidePriceException as e :
            print("the should not be negative ")


    date = Get_Date()

    sql = """
            INSERT INTO sel3a (sel3a_name , sel3a_price , buy_date ) 
            VALUES ( %s , %s , %s ) 
    """

    infos = [(name , price , date) ]

    cursor.executemany(sql , infos)

