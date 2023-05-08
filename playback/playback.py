dat1=[]

def main():
    dat= input("Enter a sentence: ")
    get_dots(dat)

def get_dots(a):
    dat1 = a.split(" ")
    for data in dat1:
        print(data,end="")
        print("...", end="")

main()

