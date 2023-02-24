def main():
    facestr=input("please input your text here -----> ")
    print(convert(facestr))


def convert(x):

   return x.replace(":)","🙂").replace( ":(" , "🙁" )


main()