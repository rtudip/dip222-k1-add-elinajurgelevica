value = []
list = []
with open("data.txt", "r") as f:
    next(f)
    viss = f.readlines()
    for rindas in viss:
        row = rindas.rstrip().split(",")
        list.append(row)

    for row in list:
        if (row[4] == "Latvia"):
            
            if (".org" in row[3]) :
                value.append(row[3])
print(len(value))