# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

from pathlib import Path

def create(path, name):
    if not (path.exists() and path.is_dir()):
        print('ERROR (directory dne)')
        return
    
    file = Path(str(path) + '/' + str(name) + '.dsu')

    if file.exists():
        print('ERROR (file alr exists)')
        return
    
    with file.open('a+'):
        print(file)
        return

def delete(file):
    sections = file.split('.')

    if sections[-1] != 'dsu':
        print('ERROR (not dsu)')
        return
    
    if not file.exists():
        print('ERROR (file dne)')
        return
    
    file.unlink()
    print(f'{file} DELETED')


def read(file):
    sections = file.split('.')

    if sections[-1] != 'dsu':
        print('ERROR (not dsu)')
        return

    if not file.exists():
        print('ERROR (file dne)')
        return


if __name__ == "__main__":
    input = input().split()
    p = Path(input[1])
    if input[0] == 'C':
        create(p, input[3])
    elif input[0] == 'D':
        delete(p)
    elif input[0] == 'R':
        read(p)

