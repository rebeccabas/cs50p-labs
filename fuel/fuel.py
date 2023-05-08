def main():
    get_fraction("Fraction: ")


def compute(a, b):
    if (a == 0) or (a/b <= 0.01):
        print("E")
    elif (b == 100) and (a/b <= 0.99) or (a == b):
        print("F")
    else:
        print(f"{round((a/b) * 100)}%")


def get_fraction(prompt):
    while True:
        try:
            x = input(prompt)
            a, b = x.split("/")
            a = int(a)
            b = int(b)
            if (a/b > 1):
                continue
            else:
                compute(a, b)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

if __name__ == "__main__":
    main()