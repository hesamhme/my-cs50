from bank import value


def main():
    testz()
    testtwn()
    testhun()


def testz():

    assert value("Hello") == 0
    assert value("Hello, Hesam") == 0


def testtwn():

    assert value("How you doin") == 20
    assert value("Hey") == 20


def testhun():

    assert value("What'sup?") == 100
    assert value("I'am great") == 100


if __name__ == "__main__":
    main()
