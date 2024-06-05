def add_entry(websites, usernames, passwords):
    websites.append(input("Enter website: "))
    usernames.append(input( "Enter username: " ))
    passwords.append(input("Enter password: "))
def main():
    websites = []
    usernames = []
    passwords = []

    add_entry(websites, usernames, passwords)

    while True:
        mode = input("What would you like to do? 1. Add entry, 2. Print all entries, 3. Print specific entry, 4. Change entry, 5. Exit: ")

        if mode == "5":
            break
        elif mode == "1":
            add_entry(websites, usernames, passwords)
        elif mode == "2":
            for i in range(len(passwords)):
                print(f"Website: {websites[i]}, Username: {usernames[i]}, Password: {passwords[i]}")
        elif mode == "3":
            print("Your saved websites:", websites)
            web = input("For which saved website would you like to examine? ")

            if web in websites:
                index = websites.index(web)
                print(f'''
    Website: {websites[index]}
    Username: {usernames[index]})
    Password: {passwords[index]}
    ''')
            else:
                print("That is not in your list of websites!")
        elif mode == '4':
            print("Your saved websites:", websites)
            web = input("For which saved website would you like to examine?:")

            if web in websites:
                index = websites.index(web)
                usernames[index] = input("\nSet new username: ")
                passwords[index] = input("Set new password: ")
            else:
                print("That is not in your list of websites!")
        else:
            break
        print()
main()