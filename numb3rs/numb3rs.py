import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", ip):
        list=[]
        list=ip.split(".")
        if int(list[0])<=255 and int(list[1])<=255 and int(list[2])<=255 and int(list[3])<=255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
