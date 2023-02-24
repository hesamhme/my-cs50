def main():
 cc=sep(input('CamelCase: '))

def sep(x):
 print ('snake_case: ',end="")
 for kal in x:

    if kal.isupper():
        print( '_'+ kal.casefold() , end="" )
    else:
        print(kal, end='' )
main()
print()