import sys
from os.path import splitext
from PIL import Image, ImageOps

mojaz = [".jpg", ".jpeg", ".png"]

def main():
    argch()
    try:
        ax = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    fixmup = ImageOps.fit(ax, size)
    fixmup.paste(shirt, shirt)
    fixmup.save(sys.argv[2])


def argch():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = sys.argv[1].lower()
    file2 = sys.argv[2].lower()
    file1_extention = splitext(file1)
    file2_extention = splitext(file2)

    if not file1_extention[1] in mojaz or not file2_extention[1] in mojaz:
        sys.exit("Invalid input")

    if file1_extention[1] != file2_extention[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()

