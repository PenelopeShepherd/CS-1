import random

def win(winner, score):
    print(f'{winner} won this round')
    score += 1
    return score
def main():
    weapons = ['rock','paper','scissors']
    user_score = 0
    bot_score = 0

    while user_score < 5 and bot_score < 5:
        while True:
            user_choice = str.lower(input('Rock paper scissors: '))

            if user_choice not in weapons:
                print('try typing rock paper or scissors')
            else:
                break

        bot_choice = random.choice(weapons)
        print(f'computer role: {bot_choice} \nuser role: {user_choice}')

        if (bot_choice == 'rock') and (user_choice == 'paper'):
            user_score = win('user', user_score)
        elif (bot_choice == 'paper') and (user_choice == 'rock'):
            bot_score = win('computer', bot_score)
        elif (bot_choice == 'paper')and (user_choice == 'scissors'):
            user_score = win('user', user_score)
        elif (bot_choice == 'rock') and (user_choice == 'scissors'):
            win('computer', bot_score)
        elif(bot_choice == 'scissors') and (user_choice == 'paper'):
            bot_score = win('computer', bot_score)
        elif(bot_choice == 'scissors') and (user_choice == 'rock'):
            user_score = win('user', user_score)
        else:
            print('tie')
        print(f'\nthe score is: user - {user_score} | computer: {bot_score}\n')
main()