

master_pwd = input('What is the master password? [2*3 = ?]')

def view():
    with open('passwords.txt', 'r') as f: #automatically closes the file for you. 
        for line in f.readlines(): 
            data = line.rstrip()
            user, passw = data.split('|')
            print("User:", user, " | Password:", passw)
        print()


def add(): 
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: #automatically closes the file for you. 
        f.write(name + "|" + pwd +'\n')



while master_pwd == '6': 
    mode = input("Would you like to add a new password or view existing ones [view, add], press q to quit? ").lower()
    if mode == 'q':
        break

    if mode == "view": 
        view()
    elif mode == 'add': 
        add()
    else:
        print('Invalid mode. ')
    while master_pwd != '6': 
        print('Invalid password, pls try again.')
        continue
