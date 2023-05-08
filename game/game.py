import random

def is_pint(a):
    if a.isalpha() == True:
        return False
    else:
       if int(a)>0:
        return True
       else:
        return False

def goto_game(n):
    val = random.randrange(1,int(n))


    while True:
        try:
         dat = input("Guess: ")
         if is_pint(dat)== True:
            
          if int(dat)>int(val):
              print("Too large!",end="\n")

          elif int(dat)<int(val):
              print("Too small!",end="\n")

          if int(dat)==int(val):
              print("Just right!",end="\n")
              break
        except (TypeError,ValueError):
         pass

def main():
    dat= input("Level: ")

    if is_pint(dat)==True:
     try:
        goto_game(dat)
     except (TypeError,ValueError):
        return main()
    else:
        return main()


if __name__ =="__main__":
    main()
