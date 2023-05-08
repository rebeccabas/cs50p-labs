data=[]
def main():
    val= input("Enter your sentence: ")
    convert(val)

def convert(a):
    data=a.split(" ")
    for dat in data:
        if dat==":)" :
            print("🙂", end=" ")
        elif dat == ":(" :
            print("🙁", end=" ")
        else:
            print(dat,end=" ")

    print()

main()

