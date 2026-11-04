'''for i in range(5):
    n = int(input("Enter the number:", ))
print(n)




sum = 0
for i in range(5):
    n = int(input("Enter the number:", ))
    sum=sum+n
print(sum)

print("*"*50)'''

'''

i = 1
total = 0

while i <= 5:
    n = int(input("Enter the number:", ))
    total += n
    i += 1
print("Total =",total)'''

'''
# nested if

mark=90
if mark>=35:
    print("Pass")
    if mark>80:
        print("O Grade")
    elif mark>60:
        print("A Grade")
    else:
        print("B Grade")
else:
    print("Re-Appearance")'''



msg="Python world"

print(msg[0])
print(msg[5])
print(msg[9])
print(msg[-1])
print(msg[1:9:2])
print(msg[3:])
print(msg[:3])
print(msg[::2])
print(msg[::-1])
print(msg[4:-5])

s= "Madam"
print(s[::-1])



name = "Pradeep"
Place = "Chennai"

print("My name is:", name.upper())
print("I'm from:", Place.lower())
print("Hello:", name.strip().title())

Updated_place = Place.replace("Chennai", "Coimbatore")

print("Current place:", Updated_place)

age = 25

print(f"My age is: {age}")

Name = "Pradeep", "Kumar"

rejoin = "-".join(Name)

print(rejoin)
