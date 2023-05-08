import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fontss = figlet.getFonts()

if len(sys.argv)==1 :
        val = input("Input: ")
        ran = random.choice(fontss)
        text = figlet.setFont(font = ran)
        print(figlet.renderText(val))

elif len(sys.argv)== 3:
    if sys.argv[1] in ["-f", "--font"]:

        if not sys.argv[2] in figlet.getFonts():
           sys.exit("Invalid Usage")

        val = input("Input: ")

        text = figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(val))
    else:
        sys.exit("Invalid Usage")

else:
    sys.exit("Invalid Usage")
