month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date_format()


def get_month_number(str, month):
    for i in month:
        if str == i:
            return month.index(i)


def date_format():
    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                try:
                    m, d, y = date.split("/")
                    m, d, y = int(m), int(d), int(y)
                except ValueError:
                    continue

            elif "," in date:
                mon, d, y = date.split(" ")
                try:
                    mon = get_month_number(mon, month)
                    m = int(mon) + 1
                    d = d.split(",")
                    d, y = int(d[0]), int(y)
                except TypeError:
                    continue


            if m <= len(month) and d <= 31:
                print(f"{y}-{m:02}-{d:02}")
                break
            else:
                pass
        except UnboundLocalError:
            pass

if __name__ =="__main__":
    main()