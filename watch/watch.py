import re
import sys


def main():
    print(parse(input("HTML: ")))
    sys.exit()


def parse(s):
    try:
        link_match = re.search(r"src=([a-z0-9A-Z/:.\"]+)", s)
        match = link_match.group(1)
        end = re.search(r"http(?:s)?://(?:www\.)?youtube.com/embed/([a-zA-z0-9]+)", match)
        return 'https://youtu.be/' + end.group(1)
    except AttributeError:
        return "None"

if __name__ == "__main__":
    main()