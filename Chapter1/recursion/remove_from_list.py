def remove(l,word):
    for i in l:
       l.remove(word)
       return l



l = ["Ritesh","Sakshi", "Ritansh", "Ajayshree","an"]    
print(remove(l,"an"))



list = ["Lucky", "Gunno", " Pari", "Meethi", "Kakka", "and"]
for i in list:
    list.remove("and")
    print(list)
    break