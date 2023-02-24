import sys
import csv


def main():

    file = bbin()


    csvkhan = csv.DictReader(file)

    sadade = []
    for satr in csvkhan:
        fam, nam = satr["name"].split(",")
        house = satr["house"]
        sadade.append({"first": nam.strip(), "last": fam, "house": house})


    fja = sys.argv[2]
    with open(fja, "w", newline='') as f:
        csvnvis = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        csvnvis.writeheader()
        for info in sadade:
            csvnvis.writerow(info)


def bbin():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

    try:
        file = open(sys.argv[1], "r")
        return file
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()