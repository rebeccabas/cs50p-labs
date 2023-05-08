from datetime import date
import inflect
import sys
import re

p=inflect.engine()

def main():
   dat=get_birthdate()
   convert(dat)


def get_birthdate():
    date=validate(input("Enter you date of birth in YYYY-MM-DD format: "))
    return date

def validate(dat):
    if re.search(r"[0-9]+\-[0-9]+\-[0-9]", dat):
        return  dat
    else:
        sys.exit("Enter in the given format")

def convert(val):
   today = date.today()
   dat = date.fromisoformat(val)
   if today>dat:
    difference = today - dat
    minutes = int(difference.total_seconds() / 60)
    words = p.number_to_words(minutes, andword="")
    print(str.capitalize(words),"minutes")
   else:
    sys.exit()

if __name__ == "__main__":
    main()
