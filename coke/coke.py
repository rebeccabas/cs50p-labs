amount = 50
while amount>0:
    print("Amount Due: ", amount)
    val = int(input("Insert Coin: "))
    if val == 25 or val == 10 or val == 5:
      amount = amount - val
    if amount == 0:
        print("Change owed: 0")
        break
    if amount<0:
        print("Change owed: ",0-amount)
        break
