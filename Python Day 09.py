age = 18

if age>18:
    print("Not eligible")
else:
    print("Eligible")


acc_bal = 22000,0,45000,20000,0,39000
print(acc_bal)
print("Minimum balance:",min(acc_bal))
print("Maximum balance:",max(acc_bal))
print(len(acc_bal))
print(acc_bal.count(0))
print("Total account holders balance:",sum(acc_bal))
print(type(acc_bal))

print("-"*50)


acc_bal=[22000,0,45000,22000,0,39000]
acc_bal[2]=23000
print(acc_bal)

yellow=["well","Yell","Lowly","owl"]
monkey=["monk","Key","money","yoke"]

subwords=[yellow,monkey]
print(subwords)

print("-"*50)


msoffice=["word","excel","powerpoint"]
Ds=["Msexcel","Powerbi","Tableau"]
Ds.extend(msoffice)
print(Ds)

print(Ds.pop())

print(Ds.pop(2))

Ds.insert(2,'Access')

DS=[]

subject=["sub","jet","cute","tub","tube"]
DS.append(subject)
print(DS)









