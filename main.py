import random
import sys


def main():
    caract = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", "@", "/", "&", "-", "(", ")", "=", "$", "1", "2", "3", "4", "5", "6", "7", "8",
              "9", "0", ";", "#", "[", "?", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
    quantity = sys.argv[1]
    quantity = int(quantity)
    password = ''

    """for i in range(quantity):
        password = password + chr(random.randint(ord('!'), ord('~')))"""

    for i in range(quantity):
        password = password + random.choice(caract)

    print(password)


if __name__ == "__main__":
    main()
