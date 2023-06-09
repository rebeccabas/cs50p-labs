def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isspace():
        return False
    if s.isalnum() == False:
        return False
    length = len(s)
    if  length < 2 or length > 7:
        return False
    digit = 0
    end = 0
    for char in s:
        if char.isdigit():
            digit += 1
    for char in reversed(s):
        if char.isalpha():
            break
        else:
            end += 1
    if digit == 0 and end == 0:
        return True
    if end == digit:
        findzero = s.find("0")
        if s[findzero - 1].isdigit():
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()