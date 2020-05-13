import random
hads = random.randint(1,99)
print (hads)
javab = input("num= ")
while javab!="d":
    if javab == "b":
        hads = random.randint(hads,99)
        print(hads)
    elif javab == "k":
        hads = random.randint(1,hads)
        print(hads)
    javab = input("num= ")
print("Wow! u rock")
