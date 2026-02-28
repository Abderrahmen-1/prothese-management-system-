from SqlConnection import *

def Khalsa():

    while True:
        name = input("which (dentist / patient) that his work khalsa ?? : ")

        if name.lower() == "dentist":
            dentist = input("wich dentist ?? :")

            cursor.execute("""  
                           SELECT 1
                           FROM information_schema.tables
                           WHERE table_schema = %s AND TABLE_NAME = %s
                           LIMIT 1
                           """, ('labo_sys', dentist ))

            exist = cursor.fetchone()

            if exist:
                name = dentist
                break
            else:
                print("table not found ")

        if name.lower() == 'patient':
            break

    while True:
        unique = int(input("what the unique number of the patient ?? "))

        cursor.execute(f"""
                       SELECT {name}.patient_number FROM {name}
                       WHERE {name}.patient_number = %s """
                       , (unique,))

        exist = cursor.fetchone()

        if exist:
            break
        else:
            print("table not found ")

    cursor.execute(f"""
                   UPDATE {name} 
                   SET khalsa = %s , b9aw = %s
                   WHERE patient_number = %s """
                   , ('yes', 0 , unique))

    cursor.execute(f"""
               DELETE FROM {name}
               WHERE finished = %s AND khalsa = %s """
                ,('yes','yes'))













