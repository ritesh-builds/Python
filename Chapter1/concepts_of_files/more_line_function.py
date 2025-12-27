f = open("file.txt","r")
# data = f.read()
# print(data)
# f.close()


line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()