import emoji

def getemoji():
    inletters = input("Input: ")
    transformemoji(inletters)

def transformemoji(n):
    print("Output: ", emoji.emojize(n))

def main():
    getemoji()

main()