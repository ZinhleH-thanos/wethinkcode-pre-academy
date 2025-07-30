while True:
    try:
        fraction = input("Fraction: ")
        x, y = map(int, fraction.split('/'))
        if x > y or y == 0:
            raise ValueError
        percent = round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break
