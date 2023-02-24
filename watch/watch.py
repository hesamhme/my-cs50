import re
def main():
    print(parse(input("HTML: ")))


def parse(ab):

    if re.search(r"<iframe(.)*<\/iframe>", ab, re.IGNORECASE):

        if dastan := re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)", ab):
            nati = f"https://youtu.be/{dastan.group(1)}"
            return nati


if __name__ == "__main__":
    main()
