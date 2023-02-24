def main():
    vor =input('input: ')
    mwv=shorten(vor)
    print('output: '+mwv)

def shorten(word):
    wwv=""
    for kalam in word:
        if not kalam.lower() in['a','e','i','u','o']:
            wwv += kalam
    return wwv


if __name__ == "__main__":
    main()