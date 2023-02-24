from twttr import shorten


def main():
    testcharcase()
    testnumbercase()
    testpunctuation()


def testcharcase():

    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwITTer") == "TwTTr"


def testnumbercase():

    assert shorten('1234') == '1234'

def testpunctuation():

    assert shorten('!,.?#$%') == '!,.?#$%'


if __name__ == "__main__":
    main()