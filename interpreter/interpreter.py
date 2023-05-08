x, y, z = input("Expression: ").split(" ")
x = float(x)
z = float(z)
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "/":
        print(x/z)
    case "*":
        print(x*z)