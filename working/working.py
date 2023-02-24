import re
def main():

    print(convert(input("hours: ")))
def convert(xab):

    if correctformat := re.search(
            r"^([0-9][0-2]*):*([0-5][0-9])* ([A|P]M) to ([0-9][0-2]*):*([0-5][0-9])* ([A|P]M)$", xab):


        if int(correctformat.group(1)) > 12 or int(correctformat.group(4)) > 12:
            raise ValueError

        firsttime = newformat(correctformat.group(1), correctformat.group(2), correctformat.group(3))

        lasttime = newformat(correctformat.group(4), correctformat.group(5), correctformat.group(6))
        return f"{firsttime} to {lasttime}"
    else:
        raise ValueError


def newformat(h, m, am_pm):

    if am_pm == "PM":
        if h == "12":
            hour = 12
        else:
            hour = int(h) + 12

    else:
        if h == "12":
            hour = 0
        else:
            hour = int(h)

    if m is None:
        min = '00'
        newtime = f"{hour:02}:{min}"
    else:
        newtime = f"{hour:02}:{m}"
    return newtime


if __name__ == "__main__":
    main()
