def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
   val,dat= d.split("$")
   return float(dat)


def percent_to_float(p):
    dat,val= p.split("%")
    return float(dat)*0.01

main()

