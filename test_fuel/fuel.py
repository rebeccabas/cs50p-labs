def main():
    convert("Fraction: ")


def convert(fraction):
    while True:
        try:
            x = input(fraction)
            a, b = x.split("/")
            a = int(a)
            b = int(b)
            percentage =(a/b)*100
            gauge(percentage)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break



def gauge(percentage):
     if int(percentage) == 0:
        print("E")
     elif int(percentage) == 100:
        print("F")
     else:
        print(f"{int(percentage)}%")


if __name__ == "__main__":
    main()