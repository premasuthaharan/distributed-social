# a1.py

from pathlib import Path

def create(path, name):
    if not (path.exists() and path.is_dir()):
        print('ERROR') # path does not exist and/or path does not point to a directory
        return True
    
    file = Path(str(path) + '/' + str(name) + '.dsu')

    if file.exists():
        print('ERROR') # file already exists
        return True
    
    with file.open('a+'):
        print(file)
        return False

def delete(file):
    sections = str(file).split('.')

    if sections[-1] != 'dsu':
        print('ERROR') # file is not a .dsu
        return True
    
    if not file.exists():
        print('ERROR') # file does not exist
        return True
    
    file.unlink()
    print(f'{file} DELETED')
    return False


def read(file):
    sections = str(file).split('.')

    if sections[-1] != 'dsu':
        print('ERROR') # file is not a .dsu
        return True

    if not file.exists():
        print('ERROR') # file does not exist
        return True

    with file.open('r') as f:
        content = f.read()
        if len(content) == 0:
            print('EMPTY') # file is empty
        else:
            print(content)

    return False


if __name__ == "__main__":

    user_input = input().split()

    repeat = True

    while repeat:
        p = Path(user_input[1])
        if user_input[0] == 'C':
            repeat = create(p, user_input[3])
        elif user_input[0] == 'D':
            repeat = delete(p)
        elif user_input[0] == 'R':
            repeat = read(p)
        else:
            print('ERROR') # invalid command entered
            repeat = True
        if repeat == True:
            user_input = input().split()
