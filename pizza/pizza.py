from tabulate import tabulate
import sys
import csv
def main():

    varagh = checkkon()

    mikhune = csv.DictReader(varagh)

    print(tabulate(mikhune, headers="keys", tablefmt="grid"))


def checkkon():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

    try:
        varagh = open(sys.argv[1], "r")
        return varagh
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
