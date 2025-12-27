word = "Donkey"

with open("d_file.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")  
  
with open("d_file.txt", "w") as f:
    f.write(contentNew)
