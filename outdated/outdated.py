mahs = ["January", "February", "March", "April", "May", "June", "July",

          "August", "September", "October", "November", "December"]
while True:
    tarikh = input("here: ").rstrip()
    if "/" in tarikh:
        mah, rooz, sal= tarikh.split("/")
    elif "," in tarikh:
        tarikh = tarikh.replace(",", "")
        mah, rooz, sal = tarikh.split(" ")
        if mah in mahs:
            mah = mahs.index(mah) + 1
    elif "/" or "," in tarikh:
        continue
    try:

        if int(mah) > 12 or int(rooz) > 31:
            continue
        else:
            break
    except ValueError:
        continue
print(sal , f"{int(mah):02}" , f"{int(rooz):02}",sep="-")