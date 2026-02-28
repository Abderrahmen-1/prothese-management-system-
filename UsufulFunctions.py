from DentistClass import addToFile


class InvalideDateException(Exception):
    pass

class InvalidePriceException(Exception):
    pass

class InvalideNameException(Exception):
    pass

class InvalideIdException(Exception):
    pass

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
            if len(unique) != 10 or not unique.isdigit() or int(unique) < 0 :
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



