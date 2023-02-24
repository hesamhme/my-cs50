gheymat = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cp=0
while True:

    try:
        chimikhay=input("Item: ").title()
        if chimikhay in gheymat:
         cp += gheymat[chimikhay]
         print('total: $'+"{:.2f}".format(cp))
    except EOFError:
        print("\n")
        break
