d = {} #Empty dictionary 

marks = {
    "Ritesh": 100,
    "Shivam": 90,
    "Tanya": 78,
    "Ishika": 88,
    1: "Ritesh "
}
# print(marks,type(marks))
# print(marks["Ritesh"])

print(marks.items())
print(marks.keys()) 
print(marks.values())
marks.update({
     "Ritesh": 10,
    "Shivam": 20,
    "Gargi": 38,
    "Ishika": 48,
    1: "ram",
    "Saanvi": 100
})
print(marks.keys())
print(marks.values())

print(marks.get("Ritesh"))
print(marks["Ritesh"])

# print(marks.get("Namrata"))
# print(marks["Namrata"])

print(type(d))