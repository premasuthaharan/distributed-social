from pathlib import Path
import shlex
import Profile
import ui


def create_profile():
    while True:
        print('Enter username:')
        username = input()
        if username != '' and username != ' ':
            break
    while True:
        print('Enter password:')
        password = input()
        if password != '' and password != ' ':
            break
    while True:
        print('Enter a short bio:')
        bio = input()
        if bio != '' and bio != ' ':
            break

    user = Profile.Profile(None, username, password)
    user.bio = bio

    return user


def open_load(mode, file):
    line = str(file).strip('"')
    sections = line.split('.')

    if sections[-1] != 'dsu':
        if mode:
            print('ERROR')
        else:
            print('ERROR: File is not .dsu')
        return ''

    if not file.exists():
        if mode:
            print('ERROR')
        else:
            print('ERROR: File does not exist')
        return ''

    if not mode:
        print(f'{file} opened successfully.')

    return file


def create(mode, path, name):
    if not (path.exists() and path.is_dir()):
        if mode:
            print('ERROR')
        else:
            print('ERROR: Make sure path exists / points to a directory')
        return ''

    file = Path(str(path) + '/' + str(name) + '.dsu')

    if file.exists():
        if not mode:
            print('File already exists. Opening file...')
        return open_load(mode, file)

    user_profile = create_profile()

    with file.open('a+'):
        print(file)

    user_profile.save_profile(file)

    return file


def delete(mode, file):
    line = str(file).strip('"')
    sections = line.split('.')

    if sections[-1] != 'dsu':
        if mode:
            print('ERROR')
        else:
            print('ERROR: File is not .dsu')
        return

    if not file.exists():
        if mode:
            print('ERROR')
        else:
            print('ERROR: File does not exist')
        return

    file.unlink()
    print(f'{file} DELETED')
    return


def read(mode, file):
    line = str(file).strip('"')
    sections = line.split('.')

    if sections[-1] != 'dsu':
        if mode:
            print('ERROR')
        else:
            print('ERROR: File is not .dsu')
        return

    if not file.exists():
        if mode:
            print('ERROR')
        else:
            print('ERROR: File does not exist')
        return

    with file.open('r') as f:
        content = f.read()
        if len(content) > 0:
            print(content.strip('\n'))
            return
        elif len(content.strip()) == 0:
            print('EMPTY')
            return
        else:
            print('EMPTY')
            return

    return


def edit(mode, file, commands):
    if mode:
        commands.pop(0)
    current_profile = Profile.Profile()
    try:
        current_profile.load_profile(file)
    except Profile.DsuProfileError:
        print('ERROR: this file does not have a profile')
        print('Create one? (y/n)')
        if input().lower() == 'y':
            current_profile = create_profile()
            current_profile.save_profile(file)
            return
        else:
            return
    for index, line in enumerate(commands):
        if index % 2 == 0:
            try:
                new_data = commands[index + 1]
            except IndexError:
                if mode:
                    print('ERROR')
                else:
                    print('ERROR: non-whitespace data required')
                return
            if line == '-usr':
                current_profile.username = new_data
                if not mode:
                    print(f'Changed username to "{new_data}" successfully')
            elif line == '-pwd':
                current_profile.password = new_data
                if not mode:
                    print(f'Changed password to "{new_data}" successfully')
            elif line == '-bio':
                current_profile.bio = new_data
                if not mode:
                    print(f'Changed bio to "{new_data}" successfully')
            elif line == '-addpost':
                new_post = Profile.Post(new_data)
                current_profile.add_post(new_post)
                if not mode:
                    print(f'Added post "{new_data}" successfully')
            elif line == '-delpost':
                posts = current_profile.get_posts()
                try:
                    int(new_data)
                except ValueError:
                    if mode:
                        print('ERROR')
                    else:
                        print('ERROR: invalid post ID')
                if 0 <= int(new_data) < len(posts):
                    success = current_profile.del_post(int(new_data))
                    if success and not mode:
                        print(f'Deleted post {new_data} successfully')
                    elif not success:
                        print('ERROR')
                else:
                    if mode:
                        print('ERROR')
                    else:
                        print('ERROR: invalid ID')
                    return
            else:
                if not mode:
                    print('ERROR: invalid option')
                else:
                    print('ERROR')
                return

            current_profile.save_profile(file)


def print_file(mode, file, commands):
    current_profile = Profile.Profile()
    try:
        current_profile.load_profile(file)
    except Profile.DsuProfileError:
        print('ERROR: this file does not have a profile')
        print('Create one? (y/n)')
        if input().lower() == 'y':
            current_profile = create_profile()
            current_profile.save_profile(file)
            return
        else:
            return

    if mode:
        index = 1
    else:
        index = 0
        print()

    while index < int(len(commands)):
        line = commands[index]
        if line == '-usr':
            if mode:
                print(current_profile.username)
            else:
                print(f'Username is "{current_profile.username}"')
            index += 1
        elif line == '-pwd':
            if mode:
                print(current_profile.password)
            else:
                print(f'Password is "{current_profile.password}"')
            index += 1
        elif line == '-bio':
            if mode:
                print(current_profile.bio)
            else:
                print(f'Bio is "{current_profile.bio}"')
            index += 1
        elif line == '-posts':
            posts = current_profile.get_posts()
            num = 0
            if not mode:
                print('Posts:')
            for post in posts:
                print(f'{num} {post.get_entry()}')
                num += 1
            index += 1
        elif line == '-post':
            id = int(commands[index + 1])
            posts = current_profile.get_posts()

            if 0 > id or id >= len(posts):
                if not mode:
                    print('ERROR: invalid ID')
                else:
                    print('ERROR')
                return

            print_post = posts[id]
            if mode:
                print(print_post.get_entry())
            else:
                print(f'Post {id}: "{print_post.get_entry()}"')
                print(f'Time: {print_post.get_time()}')
            index += 2
        elif line == '-all':
            commands_new = ['-posts', '-bio', '-pwd', '-usr']
            for item in commands_new:
                commands.insert(index + 1, item)
            index += 1
        else:
            if not mode:
                print('ERROR: invalid command')
            else:
                print('ERROR')
            return


def main():
    active_file = ''

    ui.menu(active_file)

    user_input = shlex.split(input())

    if user_input[0].lower() == 'admin':
        admin_mode = True
    else:
        admin_mode = False

    while True:
        if user_input[0] == 'Q':
            break

        if admin_mode:
            active_file = ui.admin_get_input(user_input, active_file)
        else:
            active_file = ui.get_input(user_input, active_file)
            ui.menu(active_file)

        user_input = shlex.split(input())


if __name__ == "__main__":

    main()
