from PIL import Image,ImageOps
import os.path
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3 :
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 3:
        f1= os.path.splitext(sys.argv[1])
        f2= os.path.splitext(sys.argv[2])

        ext = [".jpg",".jpeg",".png"]

        if f1[1]  in ext or f2[1]  in ext:

            if f1[1].lower()==f2[1].lower():

                try:
                    image= Image.open(sys.argv[1])
                except FileNotFoundError:
                    sys.exit("Input doesnot exist")

                shirt=Image.open("shirt.png")
                size = shirt.size
                muppet = ImageOps.fit(image,size)
                muppet.paste(shirt,shirt)
                muppet.save(sys.argv[2])
            else:
                sys.exit("Input and output have different extensions")

        else:
            sys.exit("Invalid Output")