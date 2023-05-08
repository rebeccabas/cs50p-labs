def main():
    time = input("Enter the time: ")
    n = convert(time)

    if 7<=n<=8 :
       print("Breakfast time")
    elif 12<=n<=13:
       print("Lunch time")
    elif 18<=n<=19:
       print("Dinner time")


def convert(n):
    time=n.split(":")
    h = float(time[0])
    m = (float(time[1])/60)
    t=h+m
    return t

if __name__=="__main__":
   main()



