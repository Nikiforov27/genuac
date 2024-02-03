import random

big_consonants = ['Q', 'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
small_consonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
big_vowels = ['A', 'E', 'Y', 'U', 'I', 'O']
small_vowels = ['a', 'e', 'y', 'u', 'i', 'o']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['*', '#', '@', '&', '-', '+', '/', '?', '!', ':', ';', '%', '=', '~', '[', ']', '(', ')', '_', '^', '$', '[', ']']

def add_record_name():
    pass

def gen_name(lenght: int, use_big_letters: str, ubl_num: int):#, use_numbers: str, un_num: int):
    
    name = ""

    for i in range(int(lenght / 2)):
        name = name + random.choice(small_consonants)
        name = name + random.choice(small_vowels)


    if use_big_letters == 'b':
        name = name.replace(name[ubl_num], random.choice(big_consonants + big_vowels))

    #if use_numbers == 'n':
     #   name = name.replace(name[un_num], random.choice(numbers))


    return name

def gen_pass(lenght: int, use_symbols: str, use_letters: str, use_big_letters: str):
    
    password = ""

    for i in range(lenght):
        password = password + random.choice(numbers)

    if use_symbols == 's':
        for n in range(int(lenght / 4)):
            password = password.replace(str(random.randint(0 , lenght-1)), random.choice(symbols))

    if use_letters == 'a':
        for m in range(int(lenght / 4)):
            password = password.replace(str(random.randint(0 , lenght-1)), random.choice(small_vowels + small_consonants))

    if use_big_letters == 'b':
        for g in range(int(lenght / 4)):
            password = password.replace(str(random.randint(0 , lenght-1)), random.choice(big_vowels + big_consonants))
    

    return password

def add_description():
    pass

def crypt_record():
    pass

def main():
    pass

print(gen_name(12, 'b', 0))
print(gen_pass(16, 's', 'a', 'b'))
