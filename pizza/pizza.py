import sys
from tabulate import tabulate

table=[]
header=[]

if len(sys.argv) == 1:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2 :
    sys.exit("Too many arguments")

elif len(sys.argv) == 2:
    if ".csv" not in sys.argv[1]:
        sys.exit("Incorrect file type")
    else:
        if sys.argv[1]== "regular.csv":
            with open("regular.csv") as file:
                lines = file.readlines()
                header = (lines[0].split(","))
                table =[lines[1].split(","),lines[2].split(","),lines[3].split(","),lines[4].split(","),lines[5].split(",")]
                print(tabulate(table,header, tablefmt="grid"))

        if sys.argv[1]== "sicilian.csv":
            with open("sicilian.csv") as file:
                lines = file.readlines()
                header = (lines[0].split(","))
                table =[lines[1].split(","),lines[2].split(","),lines[3].split(","),lines[4].split(","),lines[5].split(",")]
                print(tabulate(table,header, tablefmt="grid"))

        else:
            sys.exit("Non-existent file")