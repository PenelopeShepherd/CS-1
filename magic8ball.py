import random

responses = ['yes','no','maybe','ask again later','definetly no','definetly correct']

question = input("Enter your question: ")


if '?' in question:
    print(random.choice(responses))
else:
    print('''
this is not a question
try adding a question mark
''')