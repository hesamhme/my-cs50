import re
def main():

    print(count(input("Text: ")))


def count(x):
    um: list = re.findall(r"\b\W*um\W*", x, re.IGNORECASE)
    return len(um)
if __name__ == "__main__":
    main()
