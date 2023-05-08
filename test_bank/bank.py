def main():
    greeting = str(input("Greeting: ")).strip()
    val = value(greeting)
    if val == 0:
        print("$0")
    elif val ==20:
        print("$20")
    elif val == 100:
        print("$100")




def value(greeting):
    if greeting.startswith("Hello") or greeting.startswith("hello")   == True:
      return 0
    elif greeting.startswith("H") or greeting.startswith("h") == True:
      return 20
    else:
        return 100


if __name__ == "__main__":
    main()