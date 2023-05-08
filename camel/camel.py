camelCase = list(input("camelCase: "))
print ("snake_case: ", end="")
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        print("_",end="")
        camelCase[i] = camelCase[i].lower()
        print(camelCase[i], end="")
    else:
        print(camelCase[i], end="")
print()