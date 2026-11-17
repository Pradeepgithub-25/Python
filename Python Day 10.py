numbers={}
print(numbers,type(numbers))

numbers={1,2}
print(numbers,type(numbers))

india={"Tamilnadu":"Chennai","Kerala":"Kochin","Karnataka":"Bangalore"}
print(numbers,type(india))


india={"Tamilnadu":"Chennai","Kerala":"Kochin","Karnataka":"Bangalore",
       "Maharastra":"Pune","Bihar":"Pulan"}
#print(type(india))
print(india["Maharastra"])
india["Bihar"]="Patna"
print(india)

print(india.popitem())

india

india.keys()

india.values()

india.items()

res=india.get("kerala","not found")
print(res)


train={"Train number":12951,"Train name":"Mumbai Express","Source":"Mumbai",
       "Destination":"Delhi","Available_seats":120}
print("Train information:")
print(train)
print("\nTrain number:",train["Train number"])
print("Train name:",train["Train name"])
print("Source Station:",train["Source"])
print("Destination Station:",train["Destination"])
print("Available seats:",train["Available_seats"])


train={"Train_Number": 12950,"Train_Name":"Mumbai Rajdhani Express",
    "Available_Seats": 120}
print("\nTrain number:",train["Train_Number"])
print("Available seats:",train["Available_Seats"])

train["Available_Seats"]=95
print(train)


vibes=["happy","sad"]
happy_songs=["Aura 10","Aaeroplane"]
sad_songs=["Kanave","Anjala"]
playlist=dict(zip(vibes,[happy_songs,sad_songs]))
print(playlist)
print(playlist.get("sad"))
