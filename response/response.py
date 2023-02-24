from validator_collection import validators

def main():

    motghayr = input("What's your email address? ")
    try:
        validators.email(motghayr)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()