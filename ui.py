# ui.py

# Starter code for assignment 2 in
# ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# PREMA SUTHAHARAN
# PSUTHAHA@UCI.EDU
# 68442150


from pathlib import Path
import a2


def menu(active_file):
    if active_file == '' or active_file is None:
        print()
        print('Choose an option:')
        print('C - create a DSU file')
        print('O - open a DSU file')
        print('D - delete a DSU file')
        print('R - read a DSU file')
        print('Q - quit')
    else:
        print()
        print(f'The active DSU file is {active_file}')
        print("* To change which file is active, select either 'C' or 'O'*")
        print()
        print('Choose an option:')
        print('C - create a DSU file')
        print('O - open a DSU file')
        print('D - delete a DSU file')
        print('R - read a DSU file')
        print('E - edit a DSU file')
        print("P - print a DSU file's profile")
        print('Q - quit')


def check_file(file):
    try:
        p = Path(file).resolve()
    except FileNotFoundError:
        print('ERROR: enter valid path')
        return ''
    except OSError:
        print('ERROR: enter a valid path')
        return ''
    else:
        return p


def get_input(user_input, active_file):
    choice = user_input[0]
    if choice == 'C':
        path = input('Enter the path to your directory: ')

        path = check_file(path)

        name = input('Enter your file name: ')
        active_file = a2.create(False, path, name)
        return active_file
    elif choice == 'D':
        file = input('Enter the path to your file: ')
        file = check_file(file)
        a2.delete(False, file)
        return ''
    elif choice == 'R':
        file = input('Enter the path to your file: ')
        file = check_file(file)
        a2.read(False, file)
        return ''
    elif choice == 'O':
        file = input('Enter the path to your file: ')
        file = check_file(file)
        return a2.open_load(False, file)
    elif choice == 'E':
        if active_file == '' or active_file is None:
            print('ERROR: Open or create a file first')
        else:
            print('What would you like to edit?')
            print("'usr' for username, 'pwd' for password,"
                  "'bio' for bio,'addpost' for adding a post,"
                  " or 'delpost' for deleting a post")
            new = str(input())
            commands = []
            commands.append(f'-{new}')
            if new == 'delpost':
                num = input('Enter the ID number of the post: ')
                commands.append(num)
            else:
                text = input('Enter the replacement data: ')
                commands.append(str(text))
            a2.edit(False, active_file, commands)
        return active_file
    elif choice == 'P':
        if active_file == '' or active_file is None:
            print('ERROR: Open or create a file first')
        else:
            print('What would you like to print?')
            print("'usr' for username, 'pwd' for password, 'bio' for bio,"
                  " 'posts' for posts, 'post' for a single post, or 'all'")
            new = str(input())
            commands = []
            commands.append(f'-{new}')
            if new == 'post':
                num = input('Enter the ID number of the post: ')
                commands.append(num)
            a2.print_file(False, active_file, commands)
        return active_file
    else:
        print('ERROR: Invalid command entered')
    return active_file


def admin_get_input(user_input, active_file):
    admin_mode = True
    if user_input[0].lower() == 'admin':
        admin_mode = True
    elif len(user_input) < 2:
        print('ERROR')
    else:
        p = Path(user_input[1]).resolve()
        if user_input[0] == 'C' and len(user_input) == 4:
            active_file = a2.create(admin_mode, p, user_input[3])
        elif user_input[0] == 'D' and len(user_input) == 2:
            a2.delete(admin_mode, p)
        elif user_input[0] == 'R' and len(user_input) == 2:
            a2.read(admin_mode, p)
        elif user_input[0] == 'O' and len(user_input) == 2:
            active_file = a2.open_load(admin_mode, p)
        elif user_input[0] == 'E':
            if active_file == '':
                print('ERROR')
            else:
                a2.edit(admin_mode, active_file, user_input)
        elif user_input[0] == 'P':
            if active_file == '':
                print('ERROR')
            else:
                a2.print_file(admin_mode, active_file, user_input)
        else:
            print('ERROR')
    return active_file
