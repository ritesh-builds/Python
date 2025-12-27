words = ["Donkey","bad","ganda"]

with open("d_file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace("word", "#" * len(word))  
  
with open("d_file.txt", "w") as f:
    f.write(content)    






# words = ["Donkey", "bad", "ganda"]

# with open("d_file.txt", "r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "#" * len(word))

# with open("d_file.txt", "w") as f:
#     f.write(content)
