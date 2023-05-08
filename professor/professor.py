import random


def main():
    level=get_level()
    score=0
    for _ in range(10):
            x=generate_integer(level)
            y=generate_integer(level)
            val= x+y
            count=0
            for _ in range(3):
                try:
                    get = int(input(f"{x} + {y} = "))
                    if get != val:
                            count+=1
                            print("EEE")
                            if count == 3:
                             print(x ,"+", y ,"=", val)
                             break


                    if get==val:
                        score+=1
                        break


                except ValueError:
                    print("EEE")
                    pass

    print("Score:",score)



def get_level():

 while True:
        try:
            level =input("Level: ")
            if int(level) >= 1 and int(level) <= 3:
                break

        except ValueError:
            pass
 return int(level)




def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level ==2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()