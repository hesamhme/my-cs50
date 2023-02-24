import sys
def main():
    
    file = checkarg(sys.argv)
    lines = file.readlines()
    shomar = 0
    for line in lines:
        if hesam(line):
            continue
        shomar += 1
    print(shomar)


def checkarg(argv):
    
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    
    if ".py" not in argv[1]:
        sys.exit("Not a Python file")
    
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    return file


def hesam(line):
    if line.strip().startswith("#") or line.isspace():
        return True
    return False


if __name__ == "__main__":
    main()
