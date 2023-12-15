value = []
list = []
with open("data.txt", "r") as f:
    next(f)
    for rindas in f:
        row = rindas.rstrip().split(",")
        list.append(row)

    for row in list:
        if (row[4] == "Latvia"):
            if (row[7] == "Telecommunications") :
                value.append(int(row[8]))
print(sum(value))