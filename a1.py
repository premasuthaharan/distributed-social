# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# PREMA SUTHAHARAN
# PSUTHAHA@UCI.EDU
# 68442150

from pathlib import Path

def create(path, name):
    if not (path.exists() and path.is_dir()):
        print('ERROR (directory dne)')
        return True
    
    file = Path(str(path) + '/' + str(name) + '.dsu')

    if file.exists():
        print('ERROR (file alr exists)')
        return True
    
    with file.open('a+'):
        print(file)
        return False

def delete(file):
    sections = file.split('.')

    if sections[-1] != 'dsu':
        print('ERROR (not dsu)')
        return True
    
    if not file.exists():
        print('ERROR (file dne)')
        return True
    
    file.unlink()
    print(f'{file} DELETED')
    return False


def read(file):
    sections = file.split('.')

    if sections[-1] != 'dsu':
        print('ERROR (not dsu)')
        return True

    if not file.exists():
        print('ERROR (file dne)')
        return True

    with file.open('r') as f:
        content = file(read)
        if len(content) == 0:
            print('EMPTY')
        else:
            for line in content:
                print(line)

    return False


if __name__ == "__main__":

    input = input().split()

    repeat = True

    while repeat:
        p = Path(input[1])
        if input[0] == 'C':
            repeat = create(p, input[3])
        elif input[0] == 'D':
            repeat = delete(p)
        elif input[0] == 'R':
            repeat = read(p)
        else:
            print('ERROR')
            repeat = True
