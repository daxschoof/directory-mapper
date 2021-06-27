import os
import sys


def main(path, depth):
    cdcontents = []
    cddirectories = []

    for item in os.listdir(path):
        if os.path.isfile(path+'/'+item) and item[0] != '.':
            cdcontents.append(item)
        elif item[0] != '.':
            cddirectories.append(item)

    print_files(cdcontents, depth)
    print_dir(path, cddirectories, depth)


def print_files(file_list, depth):
    for file in file_list:
        substr = ''
        for _ in range(depth):
            substr += '-'

        print(substr+file)


def print_dir(path, dir_list, depth):
    for dir in dir_list:
        substr = ''
        for _ in range(depth):
            substr += '-'

        print(substr+dir)
        main(path+'/'+dir, depth+1)


if __name__ == '__main__':
    path = os.getcwd()

    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            print('[-] Invalid path given.')
            sys.exit()
    print()
    main(path, 0)
    print()
