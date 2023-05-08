file = str(input("File name:")).lower().strip()
if file.endswith(".gif")== True:
    print("image/gif")
elif file.endswith(".jpg")== True:
    print("image/jpeg")
elif file.endswith(".jpeg")== True:
    print("image/jpeg")
elif file.endswith(".png")== True:
    print("image/png")
elif file.endswith(".pdf")== True:
    print("application/pdf")
elif file.endswith(".txt")== True:
    print("text/plain")
elif file.endswith(".zip")== True:
    print("application/zip")
else:
    print("application/octet-stream")