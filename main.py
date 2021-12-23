# This is a sample Python script.
import string

alphabet = string.ascii_lowercase


def lettersum(word):
    if not len(word):
        return 0
    return alphabet.find(word[0]) + 1 + lettersum(word[1:])


def find_word_with_lettersum(somme):
    with open('enable1.txt') as file:
        for line in file:
            word = line.strip()
            if len(word) >= (somme/26) and lettersum(word) == somme:
                return word


if __name__ == '__main__':
    print(lettersum('z'))
    print(find_word_with_lettersum(319))
