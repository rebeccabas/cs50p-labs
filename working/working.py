import re

def main():
    print(convert(input("Hours: ").upper()))

def convert(s):
    if val := re.search(r"^([0-2]?[0-9]):?([0-5]?[0-9]?) (AM|PM)? to ([0-2]?[0-9]):?([0-5]?[0-9]?) (AM|PM)?", s,re.IGNORECASE):
        dat = val.groups()
        if int(dat[0]) > 12 or int(dat[3]) >12:
            raise ValueError
        t1= new_frmt(dat[0],dat[1],dat[2])
        t2= new_frmt(dat[3],dat[4],dat[5])
        return f"{t1} to {t2}"
    else:
        raise ValueError



def new_frmt(hours, min, am_pm):
    if am_pm == "PM":
        if int(hours) == 12:
            hour = 12
        else:
            hour = int(hours) + 12
    else:
        if int(hours) == 12:
            hour = 0
        else:
            hour = int(hours)
    if min == '':
        new_min = "00"
        new_time = f"{hour:02}:{new_min}"
    else:
        new_time = f"{hour:02}:{min}"
    return new_time



if __name__ == "__main__":
    main()