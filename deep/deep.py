val = str(input("What is the answer to the Great Question of life, the universe, and everything?")).lower().strip()
if val == "42" or val == "forty two" or val == "forty-two":
    print("Yes")
else:
    print("No")