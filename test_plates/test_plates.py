from plates import is_valid


def main():
    
    test_length()
    test_isalpha()
    test_number_at_middle()
    test_first_num_zero()
    test_punctuation()


def test_length():

    assert is_valid("OUTATIME") == False
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS1234") == True
    assert is_valid("C") == False


def test_isalpha():

    assert is_valid("CS") == True
    assert is_valid("C1") == False
    assert is_valid("1C") == False
    assert is_valid("11") == False


def test_number_at_middle():

    assert is_valid("CS50") == True
    assert is_valid("CS50CS") == False
    assert is_valid("C5S0C") == False


def test_first_num_zero():

    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False


def test_punctuation():

    assert is_valid("CS50") == True
    assert is_valid("CS5!") == False
    assert is_valid("CS5,") == False


if __name__ == "__main__":
    main()