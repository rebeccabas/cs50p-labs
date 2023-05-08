import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    readf = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")

reader = csv.reader(readf, delimiter=',')
next(reader, None)
fieldnames = ["first", "last", "house"]


with open(sys.argv[2], "w") as writef:
    w = csv.DictWriter(writef, fieldnames=fieldnames)
    w.writeheader()

    for row in reader:
        name, house = row
        last, first = name.strip("\"\"").strip(" ").split(",")
        w.writerow({'first': first.strip(" "), 'last': last, 'house': house})
readf.close()