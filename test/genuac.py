import random
import sys

big_consonants = ['Q', 'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
small_consonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
big_vowels = ['A', 'E', 'Y', 'U', 'I', 'O']
small_vowels = ['a', 'e', 'y', 'u', 'i', 'o']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['*', '#', '@', '&', '-', '+', '/', '?', '!', ':', ';', '%', '=', '~', '[', ']', '(', ')', '_', '^', '$', '[', ']']

def add_record_name():
    pass

def gen_name(lenght: int, args: str, int_args: int):#, use_numbers: str, un_num: int):
    
    name = ""

    for i in range(int(lenght / 2)):
        name = name + random.choice(small_consonants)
        name = name + random.choice(small_vowels)

    if args == 'b' or 'y':
        name = name.replace(name[int_args], random.choice(big_consonants + big_vowels))
    
    #elif args == 'n':
     #   name = name.replace(name[int_args], random.choice(numbers))


    return name

def gen_pass(lenght: int, args: str):
    
    password = ""

    for i in range(lenght):
        password = password + random.choice(numbers)

    if len(args) > 1:
        for k in range(len(args)):           
            if args[k] == 's' or 'y':
                for n in range(int(lenght / 4)):
                    password = password.replace(str(random.randint(0 , lenght-1)), random.choice(symbols))

            elif args[k] == 'm' or 'y':
                for m in range(int(lenght / 4)):
                    password = password.replace(str(random.randint(0 , lenght-1)), random.choice(small_vowels + small_consonants))

            elif args[k] == 'b' or 'y':
                for g in range(int(lenght / 4)):
                    password = password.replace(str(random.randint(0 , lenght-1)), random.choice(big_vowels + big_consonants))
        

    return password

def crypt_record():
    pass

def main():
    
    if sys.orig_argv[2] == "--help":
        print("\nGenuac is account generator, and password manager")
        print("")
        print("How to usage:\n\tgenuac [MODE] [your_args]")
        print("")
        print("MODE:\t--gen-account, --gen-password, --gen-name, --interactive\n")
        print("args:\n\tb - use big letters\n\ts - use symbols\n\tm - use small letters")
        print("")
        print("For example:\n\t --gen-account b 10 smb 10")


    elif sys.orig_argv[2] == "--gen-account":       
        print(gen_name(int(sys.orig_argv[3]), sys.orig_argv[4], int(sys.orig_argv[5])))
        print(gen_pass(int(sys.orig_argv[6]), sys.orig_argv[7]))

    elif sys.orig_argv[2] == "--gen-password":
        print(gen_pass(int(sys.orig_argv[3]), sys.orig_argv[4]))

    elif sys.orig_argv[2] == "--gen-name":
        print(gen_name(int(sys.orig_argv[3]), sys.orig_argv[4], int(sys.orig_argv[5])))


    elif sys.orig_argv[2] == "--interactive":


        print("how lenght do you want the name?:")
        lenght_name = int(input())

        print("Do you want use a big letters in your name? [y or n]:")
        use_big_letters = input()
        if use_big_letters == "y":
            print(use_big_letters + ": Where will a stand it big letter?:")
            big_letters_num = int(input())
        elif use_big_letters == "n":
            print(use_big_letters +": ok")
        else:
            print(use_big_letters + ":Your response unsiutable")



        print("How lenght do you want the password?:")
        lenght_password = int(input())
        
        print("Do you want use a symbols in your password? [y or n]:")
        use_symbols = input()
        if use_symbols == "y":
            print(use_symbols + ": ok")
        elif use_symbols == "n":
            print(use_symbols + ": ok")
        else:
            print(use_symbols + ": Your response unsiutable")
        
        print("Do you want use a big letters in your password? [y or n]:")
        use_big_letters_in_password = input()
        if use_big_letters_in_password == "y":
            print(use_big_letters_in_password + ": ok")
        elif use_big_letters_in_password == "n":
            print(use_big_letters_in_password + ": ok")
        else:
            print(use_big_letters_in_password + ": Your response unsiutable")
        
        print("Do you want use a small letters in your name? [y or n]:")
        use_small_letters = input()
        if use_small_letters == "y":
            print(use_small_letters + ": ok")
        elif use_small_letters == "n":
            print(use_small_letters + ": ok")
        else:
            print(use_small_letters + ": Your response unsiutable")

        
        print("Do you want add descripion ? [y or n]:")
        add_description = input()
        if add_description == "y":
            print(add_description + ": ok")
            print("Enter the description:\n")
            description = input()
        elif add_description == "n":
            print(add_description + ": ok")
        else:
            print(add_description + ": Your response unsiutable")
        

        print("\nYour name: " + gen_name(lenght_name, use_big_letters, big_letters_num))

        args_for_password = use_symbols + use_big_letters_in_password + use_small_letters
        print("Your password: " + gen_pass(lenght_password, args_for_password))
        print("Your description:\n" + description)
main()
