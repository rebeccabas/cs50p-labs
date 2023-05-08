import sys
import re


def main():
    print(count(input("Text: ")))


def count(s):
   try:
    dat= len(re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE))
    return dat
   except:
    sys.exit()


if __name__ == "__main__":
    main()