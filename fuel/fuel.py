def main():
    fraction: str = input("Fuel: ")
    percentage = convert(fraction)
    print(gauge(percentage))
def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            decimal = x / y

            if decimal <= 1:
                return round(decimal * 100)
            fraction: str = input("Fuel: ")
            continue

        except (ValueError, ZeroDivisionError):
            raise
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
if __name__ == "__main__":
    main()