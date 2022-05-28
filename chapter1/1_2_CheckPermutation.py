from collections import defaultdict


def check_permutation(s1: str, s2: str) -> bool:

    d = defaultdict()

    for letter in s1:
        if not d.get(letter):
            d[letter] = 1
        else:
            d[letter] += 1

    for letter in s2:
        if not d.get(letter):
            return False
        else:
            d[letter] -= 1
            if d[letter] == 0:
                d.pop(letter)

    if d:
        return False

    return True


if __name__ == '__main__':
    if check_permutation('abc','cba'):
        print('SAME')

