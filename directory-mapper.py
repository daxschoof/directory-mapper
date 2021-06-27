import os
import sys


def main(path):
    cdcontents = []
    cddirectories = []

    for item in os.listdir(path):
        if os.path.isfile(path+'/'+item):
            cdcontents.append(item)
        else:
            cddirectories.append(item)

    print(cddirectories)
    print(cdcontents)


if __name__ == '__main__':
    path = os.getcwd()

    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.exists(path):
            print('[-] Invalid path given.')
            sys.exit()

    main(path)
