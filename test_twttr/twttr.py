def main():
    string = input("Input: ")
    print(convert(string))


def convert(string):
    vow = ["a", "e", "i", "o", "u"]
    no_vow = ""
    for char in string:
        if char.lower() not in vow:
            no_vow += char
    return no_vow


if __name__ == "__main__":
    main()