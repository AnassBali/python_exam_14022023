"""from prettytable import PrettyTable
from colorama import *

guides = {"id 1": {"name": "John", "age": 25, "gender": "man", "salary": 2500, "list_cities": ["Rome", "Venice"]},
          "id 2": {"name": "Mark", "age": 20, "gender": "man", "salary": 4000, "list_cities": ["Madrid", "Barcelona"]},
          "id 3": {"name": "Lisa", "age": 35, "gender": "woman", "salary": 3800, "list_cities": ["Berlin"]},
          "id 4": {"name": "Lien", "age": 40, "gender": "woman", "salary": 3600, "list_cities": ["Paris "]},
          "id 5": {"name": "Jordy", "age": 37, "gender": "man", "salary": 3000, "list_cities": ["Stockholm"]}}

admin = {"admininfo": {"username": "admin", "password": "admin"}}


def admin_login():
    print("Enter your login details, write 'stop' to quit the program")
    username = input("Enter your username as admin:")
    password = input("Enter your password:")
    for info, details in admin.items():
        if username.lower() == 'stop' or password == 'stop':
            break
        while not username == details["username"] or not password == details["password"]:
            print(Fore.RED, "\nIncorrect login credentials!", Fore.RESET)
            print("Type 'stop' to quit te program")
            username = input("\n\nEnter your username again as admin:")
            password = input("Enter your password:")
        print("LOGIN SUCCESSFUL!")


def show_guides():
    guides_information = PrettyTable(["ID", "name", "age", "gender", "salary", "list_cities"])
    for id, guide in guides.items():
        guides_information.add_row(
            [id, guide["name"], guide["age"], guide["gender"],
             guide["salary"], guide["list_cities"]])
    print(guides_information)


def add_guide():
    id = "id " + str(len(guides) + 1)
    name = input("What is the name of the guide?")
    age = int(input(f"What is the age of {name.title()}"))
    gender = input("What is his / her gender?")
    salary = input(f"What is the monthly salary of {name.title()}?")
    list_cities = input("In which city / cities is he a guide?")
    guides.update({id: {"name": name, "age": age, "gender": gender,
                        "salary": salary, "list_cities": list_cities}})
    show_guides()
    print(Fore.GREEN, f"\nNew guide got successfully added, welcome on board! \n", Fore.RESET)
    functions()


def add_city():
    show_guides()
    print("Enter admin login to add a city to a guide: ")
    username = input("Enter your username as admin:")
    password = input("Enter your password:")
    for info, details in admin.items():
        while not username == details["username"] or not password == details["password"]:
            print(Fore.RED, "\nIncorrect login credentials!", Fore.RESET)
            username = input("\n\nEnter your username again as admin:")
            password = input("Enter your password:")
    id = input("Enter the id of the guide who you want to add a city to:")
    id_guide = "id " + id
    while id_guide not in guides:
        print(Fore.RED, "Incorrect ID, try again", Fore.RESET)
        id = input("Enter the id of the guide where you want to add a city to:")
        id_guide = "id " + id
    add_city = input(f"Enter the city which you would like to add for id {id} ")
    guides[id_guide]['list_cities'].append(add_city)
    show_guides()
    print(Fore.GREEN, f"\nThe city {add_city} got successfully added to ID {id} ! \n", Fore.RESET)
    functions()


def delete_guide():
    show_guides()
    print("Enter admin login to delete a guide: ")
    username = input("Enter your username as admin:")
    password = input("Enter your password:")
    for info, details in admin.items():
        while not username == details["username"] or not password == details["password"]:
            print(Fore.RED, "\nIncorrect login credentials!", Fore.RESET)
            username = input("\n\nEnter your username again as admin:")
            password = input("Enter your password:")
    id = input("Enter the id of the guide who you want to delete: ")
    id_guide = "id " + id
    while id_guide not in guides:
        print(Fore.RED, "Incorrect ID, try again", Fore.RESET)
        id = input("Enter the id of the guide where you want to delete: ")
        id_guide = "id " + id
    del guides[id_guide]
    show_guides()
    print(Fore.GREEN, f"\nID {id} got successfully deleted! \n", Fore.RESET)
    functions()


def change_password():
    print("Enter current password")
    current_password = input(": ")
    for info, details in admin.items():
        while not current_password == details["password"]:
            print("Password is not correct")
            current_password = input(": ")
        new_password = input("Enter your new password")
        new_password2 = input("Enter your new password again")
        if new_password == new_password2:
            details["password"] = new_password
            print("Password is changed successfully")
        else:
            print("New password doesn't match")
            new_password = input("Enter your new password")
            if new_password == new_password2:
                details["password"] = new_password
                print("Password is changed successfully")


def functions():
    print("Choose a function:", Fore.BLACK)
    print(
        "\n1: Add guide \n2: Add city\n3: Delete guide\n4: "
        "Add city to all guides\n5: Change password \n", "6: Choose filter \n", Fore.RESET)
    functions_guide = input("Enter a number: ")
    print(Fore.RESET)
    if functions_guide == "1":
        add_guide()
    elif functions_guide == "2":
        add_city()
    elif functions_guide == "3":
        delete_guide()
    elif functions_guide == "4":
        add_city_to_all_guides()
    elif functions_guide == "5":
        change_password()
    elif functions_guide == "6":
        choose_filter()
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET), functions_guide


def add_city_to_all_guides():
    add_city = input("Which city would you like to add to every guide?")
    for id, details in guides.items():
        details['list_cities'].append(add_city)
    show_guides()
    print(Fore.GREEN, f"\nEveryone got {add_city} added to their cities!\n ", Fore.RESET)
    functions()


def men_and_women():
    gender = input("Do you want to see all men or women? (man / woman)")
    print(Fore.RESET)
    if gender.lower() == "man" or gender.lower() == "woman":
        for id, details in guides.items():
            if details["gender"] == gender:
                guides.update(
                    {"id": {"name": details, "age": details, "gender": details, "salary": details,
                            "list_cities": details}})
                print(id, end="\t")
                for info in guides.values():
                    print(info, end="\t\t")
                print("")
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET)
        men_and_women()
    functions()


def city():
    city_choice = input("Which city would you like to view?")
    print(Fore.RESET)
    for id, details in guides.items():
        if details["list_cities"] == city_choice:
            guides.update(
                {"id": {"name": details, "age": details, "gender": details, "salary": details, "list_cities": details}})
            print(id, end="\t")
            for info in guides.values():
                print(info, end="\t\t")
            print("")
        else:
            print(Fore.RED, "Incorrect input", Fore.RESET)
            city()
    functions()


def salary_comparison():
    salary_to_compare = int(input("Enter a monthly salary (e.g.: 2500) and a list will be shown of everyone who earns "
                                  "more"))
    print(Fore.RESET)
    for details in guides.values():
        if salary_to_compare < details['salary']:
            guides.update({"id": {"name": details, "age": details, "gender": details,
                                  "salary": details, "list_cities": details}})
            print(id, end="\t")
            for info in details.values():
                print(info, end="\t\t")
            print("")
    functions()


def city_and_gender():
    city_choice = input("Which city would you like to view?")
    gender_choice = input(f"Which gender would you like to view to the city {city_choice}? (man or woman)")
    print(Fore.RESET)
    for id, details in guides.items():
        if city_choice.title() in details["list_cities"] and details["gender"] == gender_choice.lower():
            guides.update(
                {"id": {"name": details, "age": details, "gender": details, "salary": details,
                        "list_cities": details}})
            print(id, end="\t")
            for info in guides.values():
                print(info, end="\t\t")
            print("")
        else:
            print(Fore.RED, "Incorrect input", Fore.RESET)
            city_and_gender()
    functions()


def choose_filter():
    print(Fore.YELLOW,
          "\n----------------------------------------------------------------------------------------------------------"
          "-")
    print("-----------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\tWelcome to the filter system!")
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------",
          Fore.LIGHTYELLOW_EX)
    print("Choose a filter:", Fore.BLACK)
    print(
        "\n0: Go back to admin functions\n1: Filter man / woman\n2: Filter by city\n3: Monthly "
        "salary higher than..\n4: "
        "All males or females:\n", Fore.RESET)
    function_guides = input("Enter a number: ")
    print(Fore.RESET)
    if function_guides == "1":
        men_and_women()
    elif function_guides == "2":
        city()
    elif function_guides == "3":
        salary_comparison()
    elif function_guides == "4":
        city_and_gender()
    elif function_guides == "0":
        functions()
    else:
        print(Fore.RED, "Incorrect input", Fore.RESET), function_guides()


admin_login()
show_guides()
functions()
def menu_filters():
    print("Menu Filters:")
    print("a. Alle man/vrouw gidsen")
    print("b. Alle gidsen die stad x gidsen")
    print("c. Alle gidsen met een hoger loon dan x")
    print("d. Alle man of vrouw die een stad gidse")

    choice = input("Kies een optie (a, b, c, d) of typ 'stop' om te stoppen: ").lower()"""

"""word_list = ["Knight", "Bishop", "Queen", "Pawn"]
encrypted_dict = {}


def add_word():
    word = input("Which word would you like to add?")
    word_list.append(word)
    print(f"{word} has been added to the list.")
    print(word_list)
    functions()


def remove_word():
    remove_word = input("Which word would you like to remove?")
    while not remove_word.title() in word_list:
        print("Wrong input, try again..")
        remove_word = input("Which word would you like to remove?")
    word_list.remove(remove_word)
    print(f"{remove_word} has been deleted from the list.")
    print(word_list)
    functions()


def switch_list_to_dict():

    for word in word_list:
        encrypted_dict = {}
        id = "W " + str(len(word_list) + 1)
        encrypted_dict = dict.fromkeys(id, word)
        encrypted_dict[f"W{id}"] = word
        encrypted_dict.update({id: word})
        print("The list has been changed to a dictionary.")
        print(encrypted_dict)
        functions()


def encrypt_dict(text, s):
    for words in word_list:
        switch_list_to_dict()
        result = words
        for i in range(len(id)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)

        return result
    functions()


def print_dictionary():
    print(word_list, encrypted_dict)
    functions()


def functions():
    for id, details in encrypted_dict.items():
        print(f"{id}: {details}")
    functie = input("Wat would you like to do?\nadd\ndelete\nswitch\nencrypt\nprint\nstop\n: ")
    if functie == "add":
        add_word()
    elif functie == "delete":
        remove_word()
    elif functie == "switch":
        switch_list_to_dict()
    elif functie == "encrypt":
        encrypt_dict()
    elif functie == "print":
        print_dictionary()
    elif functie == "stop":
        print("Program is closed!")
    else:
        print("Wrong input!")


functions()
"""
