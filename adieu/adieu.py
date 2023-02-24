import inflect
hes = inflect.engine()

namha = []
while True:
    try:

        esm: str = input("here: ").title()

    except EOFError:
        print()
        break

    if esm not in namha:
        namha.append(esm)

jav = hes.join(namha)
print(f"Adieu, adieu, to {jav}")