import randompro
def main():
    mar: int = mb()

    score: int = bes(mar)

    print(f"Score: {emt}")
def mb() -> int:

    while True:
        try:
            mar = int(input("Level: "))
            if mar in [1, 2, 3]:
                return mar
        except ValueError:
            pass

def ssaz(mar):

    if mar == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
    elif mar == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    else:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
    return a, b


def jsa(a, b):

    sh = 1
    while sh <= 3:
        try:
            jj = int(input(f"{a} + {b} = "))
            if jj == (a+b):
                return True
            else:
                sh += 1
                print("EEE")
        except:
            sh += 1
            print("EEE")
    print(f"{a} + {b} = {a+b}")
    return False


def besh(mar):

    emt = 0
    for _ in range(0, 10):
        a, b = ssaz(mar)
        nat = jj(a, b)
        if nat:
            emt += 1
    return emt


if __name__ == "__main__":
    main()
