import string
import argparse
from random import choice
from pyperclip import copy


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(integer=8, quiet=False):
    char = string.ascii_letters + string.punctuation + string.digits
    paswd = ''.join(choice(char) for x in range(integer))
    if quiet:
        return copy(paswd)
    elif not quiet:
        return print(color.BOLD+color.OKGREEN+paswd+color.END)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process length of password, default length is 8")
    parser.add_argument("length",
                        default=15,
                        nargs='?',
                        metavar='INT',
                        type=int,
                        help="Length of password")
    parser.add_argument("-q", "--quiet",
                        default=False,
                        action="store_true",
                        help="Do not echo a password in terminal and send it into clipboard")
    args = parser.parse_known_args()
    length = args[0].length
    if args[0].quiet:
        main(length, args[0].quiet)
    else:
        main(length)
