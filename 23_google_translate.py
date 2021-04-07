import time
import pyfiglet
import termcolor2

print(termcolor2.colored("                                                    Loading", color="green"))
time.sleep(1.2)
three = pyfiglet.figlet_format("3")
print(termcolor2.colored(three, color="yellow"))
time.sleep(1.2)
tow = pyfiglet.figlet_format("2")
print(termcolor2.colored(tow, color="blue"))
time.sleep(1.2)
one = pyfiglet.figlet_format("1")
print(termcolor2.colored(one, color="red"))
time.sleep(1.2)

book = open("translate.txt", "r")
all_book = book.read()
split = all_book.split("\n")

words = []


def english_to_persian():
    i = 0
    while i < len(split):
        my_dict = {"english": split[i], "persian": split[i + 1]}
        words.append(my_dict)
        i += 2

    print(termcolor2.colored("                                                    *Welcome To Our App*",
                             color="cyan"))
    user = input("Enter Sentence: ")
    user_sentence = user.split(" ")
    for i in range(len(user_sentence)):
        for j in range(len(words)):
            if words[j]["english"] == user_sentence[i]:
                print(termcolor2.colored(words[j]["persian"], color="green"), end=" ")
                break
        else:
            print(termcolor2.colored(user_sentence[i], color="red"), end=" ")

    menu()


def persian_to_english():
    i = 0
    while i < len(split):
        my_dict = {"english": split[i], "persian": split[i + 1]}
        words.append(my_dict)
        i += 2

    print(termcolor2.colored("                                             *Welcome To Our App*", color="cyan"))
    user = input("Enter Sentence: ")
    user_sentence = user.split(" ")
    for i in range(len(user_sentence)):
        for j in range(len(words)):
            if words[j]["persian"] == user_sentence[i]:
                print(termcolor2.colored(words[j]["english"], color="green"), end=" ")
                break
        else:
            print(termcolor2.colored(user_sentence[i], color="red"), end=" ")
    menu()


def add_word():
    print(termcolor2.colored("                                             *Welcome To Our App*", color="cyan"))
    word_english = input("Enter Word English: ")
    word_persian = input("Enter Word Persian: ")
    words.append({"english": word_english, "persian": word_persian})
    book = open("translate.txt", "a")
    book.write(f"\n{word_english} \n{word_persian}")
    print(termcolor2.colored("Words Add", color="green"))

    menu()


def menu():
    menu = ["\n1_English to Persian", "2_Persian to English", "3_Add Word To File", "4_Word Exit"]
    for men in menu:
        print(men)
    select = input("\nEnter Selection: ")
    if select == "1":
        english_to_persian()
    elif select == "2":
        persian_to_english()
    elif select == "3":
        add_word()
    else:
        exit()


menu()
