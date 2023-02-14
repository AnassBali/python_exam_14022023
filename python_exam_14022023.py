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
