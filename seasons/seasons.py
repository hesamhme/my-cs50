from datetime import date
import sys
import inflect


def main():

    ttavalod = input("dateof birth: ")

    m = date_format(ttavalod)

    print(f"{words(m).capitalize().replace(' and','')} minutes")


def date_format(bday):

    try:
        d = date.fromisoformat(bday)
    except ValueError:
        sys.exit("Invalid date")
    else:
        return delta(d)


def delta(d):
    rooz = date.today() - d
    return rooz.days * 24 * 60


def words(n):
    ab = inflect.engine()
    return ab.number_to_words(n)


if __name__ == "__main__":
    main()

