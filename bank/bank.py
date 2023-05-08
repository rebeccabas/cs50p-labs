def get_greeting():
    greeting = str(input("Greeting: ")).strip()
    check_greeting(greeting)

def check_greeting(g):
    if g.startswith("Hello") or g.startswith("hello")   == True:
      print("$0")
    elif g.startswith("H") or g.startswith("h") == True:
      print("$20")
    else:
        print("$100")

def main():
    get_greeting()

if __name__ == "__main__":
    main()