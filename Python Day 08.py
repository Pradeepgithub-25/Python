s = "Python program"
print(s.swapcase())

s = "Python program"
print(s.capitalize())


s = "Python program"
print(s.istitle())

s = "Python program"
print(s.title())

s = "python program"
print(s.upper())


s = "Python PRogram"
print(s.lower())

s = "Pradeep kumar"
res=s.split(' ')
print(res)

system = "Computer"
print(system.index('t'))

system = "Computer"
print(system.find('T'))

s = "python program"
print(s.endswith("m"))

s = "python program"
print(s.startswith("p"))


s = "pradeep kumar"
print(s.count('p'))

num= "78"
print(num.zfill(5))


name = "Pradeep kumar"

for char in name:
    print(char,"=",name.count(char))
