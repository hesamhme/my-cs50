def main():
    slm = input("Greeting: ")
    nat = value(slm)
    print(f"${nat}")
def value(slm):
    ns = slm.strip().lower()

    if "hello" in ns:
        return 0

    elif ns[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()