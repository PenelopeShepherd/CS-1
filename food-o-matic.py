import random
starters = ['land of ','kingdom of ', 'the magical ','the stink of ']
names = ['narnia', 'knights','flowers','uhhh stuff']

while True:
    items = input('Enter the number of items you want: ')

    if items.isnumeric():
        break
    else:
        print('Please enter a positive number')
for i in range(int(items)):
    print(random.choice(starters)+random.choice(names))