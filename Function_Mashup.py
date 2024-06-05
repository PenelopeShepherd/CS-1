import random

def add(num1, num2):
    print(num1 + num2)
def check_int(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False
def get_int():
    while True:
        try:
            number = int(input("Enter number: "))
            return number
        except ValueError:
            print("Please enter a number!")
def get_random():
    num1 = get_int()
    num2 = get_int()
    print(random.randint(num1, num2))
def voice():
    print("ee ay ee ay oo")
def melody():
    print("Old McDonald had a farm")
    voice()
    print("and on that farm he had a cow")
    voice()
    print("with a moo moo here and a moo moo there")
    print("here a moo, there a moo, everywhere a moo-moo")
def list_organizer(items):
    for element in items:
        print(element)
def in_list(items, element):
    return element in items
def replace_character(string, old_character, new_character):
    new_string = ''

    for ch in string:
        if ch == old_character:
            new_string += new_character
        else:
            new_string += ch
    return new_string
def main():
    num1 = get_int()
    num2 = get_int()

    add(num1, num2)
    number = input("Enter number: ")
    check_int(number)
    get_random()

    items = ['a', 'b', 'c']
    list_organizer(items)
    print(in_list(items, 'a'))

    melody()

    print(replace_character('hello world', 'l', 'a'))
main()