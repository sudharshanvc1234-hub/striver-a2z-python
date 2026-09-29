def print_rangoli(size):
    width = 4 * size - 3

    for i in range(size - 1, -1, -1):
        letters = []

        for j in range(size - 1, i - 1, -1):
            letters.append(chr(97 + j))

        row = letters + letters[::-1][1:]
        print("-".join(row).center(width, "-"))

    for i in range(1, size):
        letters = []

        for j in range(size - 1, i - 1, -1):
            letters.append(chr(97 + j))

        row = letters + letters[::-1][1:]
        print("-".join(row).center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)