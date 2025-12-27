for i in range(100):
    if i == 50:
        break   #Exit the right now.
    print(i)

for a in range(100):
        if a == 60:
            continue   #Skip the current iteration.
        print(a)


l = ["Harry", "Rohan", "SkillF", "Shubham", "Vikrant","Sakshi","Salman", "Seema", "Sameeksha"]

for i in l:
    if (i.startswith("S")):
      print(f"Hello {i}")