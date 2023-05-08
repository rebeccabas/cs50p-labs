def main():
    get_dict("")


def compute(item, dict):
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
    return dict

def sort_dict(dict):
    for i in sorted(dict):
        print(dict[i], i.upper())


def get_dict(dat):
    dict = {}
    while True:
        try:
            item = input(dat)
            dict = compute(item, dict)
        except EOFError:
            break
    sort_dict(dict)

if __name__ == "__main__":
    main()