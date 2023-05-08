import sys
from validator_collection import checkers

def main():
    try:
        dat = input("Email: ")
        is_email_address = checkers.is_email(dat)
        if is_email_address == True:
            print("Valid")
        else:
            print("Invalid")
    except:
        sys.exit

if __name__ == "__main__":
    main()