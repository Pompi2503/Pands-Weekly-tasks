FILENAME = "count.txt"
def writeNumber(number):
    with open(FILENAME, "w") as f:
        f.write(str(number))
writeNumber(8)