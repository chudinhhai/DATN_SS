file = open("1.txt", 'r')
readFile = file.readlines()
for line in readFile:
    print(type(float(line.split(',')[0])))
# lineID = readFile.split(",")
# print(lineID[1])