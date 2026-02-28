from LaboDics import *
from SqlConnection import *
from SendMessage import sendmessage


def Finished():

    while True:
        name = input("which (dentist / patient) you finished his work ?? : ")

        if name.lower() == "dentist":
            dentist = input("put the name of the dentist : ")
            cursor.execute("""  
                           SELECT 1
                           FROM information_schema.tables
                           WHERE table_schema = %s AND TABLE_NAME = %s
                           LIMIT 1
                           """, ('labo_sys', dentist))

            exist = cursor.fetchone()

            if exist:
                name = dentist
                break
            else:
                print("table not found ")
        if name.lower() == "patient":
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
                         SET finished = %s 
                         WHERE patient_number = %s """
                   , ('yes', unique))

    cursor.execute(f"""
                    DELETE FROM {name}
                    WHERE finished = %s AND khalsa = %s """
                   , ('yes', 'yes'))

    cursor.execute("""
                   UPDATE khedma 
                   SET khedma_wajda = %s 
                   WHERE khedma_patient = %s """

                   , ( 'yes' , unique ) )

    cursor.execute(f"""
                        DELETE FROM khedma
                        WHERE khedma_wajda = %s """
                   , ('yes',) )

    cursor.execute( f"""
                  DELETE FROM {name} 
                  WHERE finished = %s AND khalsa = %s """
                  , ('yes' , 'yes') )

    connection.commit()


    #if name.lower() == "patient" :
     #   sendmessage(unique)
