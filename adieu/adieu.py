import inflect
p = inflect.engine()

names = []

while True:
    try:
        name=input("Name: ")
        names.append(name)

    except EOFError:
        end = p.join(names[0:])
        print(f"Adieu, adieu, to {end}")
        break
