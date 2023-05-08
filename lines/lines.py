import sys
lines = []
count = 0

if len(sys.argv) == 1:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2 :
    sys.exit("Too many arguments")

elif len(sys.argv) == 2:
    if ".py" not in sys.argv[1]:
        sys.exit("Incorrect file type")

    else:
        with open(sys.argv[1]) as file:
            lines = file.readlines()

            for line in lines:
                line=line.strip()
                if len(line)>0:
                    if line[0]!= "#" :
                        count +=1
                else:
                    count =count+0
        print(count)