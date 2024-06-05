import sys

print('wake up!')
lateness = 0
time = 80 
print(f'{time} minutes to get ready')
smart_person = True

tired = str.lower(input('did you stay up late last night? '))

if tired == 'yes' and lateness <= 3:
    print('pressed snooze')
    lateness += 1
    time -= 10

    while True:
        snooze = str.lower(input('press snooze again? '))

        if lateness <=2 and snooze == 'yes':
            lateness += 1
            time -= 10
            print('pressed snooze')

            if lateness >= 3 and snooze == 'yes':
            	break
            	print('YOURE LATE GET UP')
        elif lateness <= 3 and snooze == 'no':
            break
        elif snooze != 'yes' and snooze != 'no':
            print('try typing yes or no')
            smart_person = False
            sys.exit()
elif tired != 'yes' and tired!='no':
    print('try typing yes or no')
    smart_person = False
    sys.exit()

print(f'{time} minutes to get ready')
raining = str.lower(input('is it raining? '))

if raining == 'yes':
    print('put on a jacket')
    time -= 5
    print(f'{time} minutes to get ready')
elif raining != 'yes' and raining != 'no':
    print('try typing yes or no')
    print('smart_person = False')

clean = str.lower(input('brush your teeth? '))

if clean == 'yes':
    print('good job')
    time -= 5
elif tired != 'yes' and tired != 'no':
    print('try typing yes or no')
    smart_person = False
else:
    print('your breath smells like dead fish')

makeup = str.lower(input('put on makeup? '))

if makeup == 'yes':
    print('pretty!')
    time -= 10
   
    print(f'{time} minutes to get ready')
elif makeup == 'yes' and time < 50:
    print(f'{time} minutes to get ready')
elif makeup != 'yes' or 'no':
    print('try typing yes or no')
    smart_person = False

coffee = str.lower(input('make coffee? '))

if coffee =='yes':
    print('energized!')
    time -=15
    print(f'{time} minutes to get ready')
    brush = str.lower(input('brush teeth? '))

    if brush == 'yes':
        print('your breath is minty fresh')
        time -= 10 
    elif brush == 'no' and clean == 'no':
        print('your breath smells really bad')
    elif brush == 'no':
        print('you have coffee breath')
    elif coffee == 'no' and lateness >= 1:
        print('I thought you said you were tired? ')
    elif brush != 'yes' and brush != 'no':
        print('try typing yes or no')
        smart_person = False

eat = str.lower(input('eat breakfast? '))

if eat == 'yes':
    print('you are not hungry anymore')
    time -= 15
    print(f'{time} minutes to get ready')
elif eat == 'yes' and time < 30:
    print('EAT QUICKLY!')
    time -= 10
    print(f'{time} minutes to get ready')
elif eat != 'yes' and eat != 'no':
    print('try typing yes or no')
    smart_person = False

bike = str.lower(input('bike to school? '))

if bike == 'yes' and raining == 'no':
    print('you make it to school on time and enjoyed your bike ride')
    print('the end!')
    sys.exit()
elif bike != 'yes' and bike != 'no':
    print('try typing yes or no')
    smart_person = False
elif bike == 'yes' and raining == 'yes':
    print('why are you biking in the rain?')
    print('you made it to school but at what cost??')
    time -= 20
    print(f'{time} minutes to get ready')

drive = str.lower(input('drive to school? '))

if drive=='yes':
    print('You made it to school!')
elif tired != 'yes' and tired != 'no':
    print('try typing yes or no')
    smart_person = False
else:
    print('have fun skipping school!')