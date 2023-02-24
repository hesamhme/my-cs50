dictkhali={}
while True:
    try:
        chichi=input("").lower()
        if chichi in dictkhali:
            dictkhali[chichi]+= 1
        else:
            dictkhali[chichi]= 1
    except EOFError:
        for hayhay in sorted(dictkhali.keys()):
            print(dictkhali[hayhay],hayhay.upper())
        break
