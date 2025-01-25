# a1.py

from pathlib import Path

def create(path, name):
    if not (path.exists() and path.is_dir()):
        print('ERROR') # path does not exist and/or path does not point to a directory
        return
    
    file = Path(str(path) + '/' + str(name) + '.dsu')

    if file.exists():
        print('ERROR') # file already exists
        return
    
    with file.open('a+'):
        print(file)
        return

def delete(file):
    sections = str(file).split('.')

    if sections[-1] != 'dsu':
        print('ERROR') # file is not a .dsu
        return
    
    if not file.exists():
        print('ERROR') # file does not exist
        return
    
    file.unlink()
    print(f'{file} DELETED')
    return


def read(file):
    sections = str(file).split('.')

    if sections[-1] != 'dsu':
        print('ERROR') # file is not a .dsu
        return

    if not file.exists():
        print('ERROR') # file does not exist
        return

    with file.open('r') as f:
        content = f.read()
        if len(content) > 0:
            print(content.strip('\n'))
            return
        elif len(content.strip()) == 0:
            print('EMPTY') # file is empty
            return
        else:
            print('EMPTY') # file is empty
            return

    return


if __name__ == "__main__":

    user_input = input().split()

    while True:
        if user_input[0] == 'Q':
            break
        elif len(user_input) < 2:
            print('ERROR')
        else:
            p = Path(user_input[1])
            if user_input[0] == 'C' and len(user_input) == 4:
                create(p, user_input[3])
            elif user_input[0] == 'D' and len(user_input) == 2:
                delete(p)
            elif user_input[0] == 'R' and len(user_input) == 2:
                read(p)
            else:
                print('ERROR') # invalid command entered

        user_input = input().split()
