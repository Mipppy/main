import os

print("\n\nTalk to me and see if I care\n")
iput = input("what would like to say? \n")

myfile = "/workspaces/main/responsder.py"

if iput == "kys":
    print("Deleting myself :D")
    os.remove(myfile)







