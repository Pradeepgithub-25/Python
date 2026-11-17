#set

a={1,2,3}
print(type(a))
print(a)


#string

colors={"red","green","blue"}
print(colors)

#mixed

colors={"Red",1,True}
print(colors)

#set

numbers={1,2,3,4,5}
print(type(numbers))
print(numbers)

#update
numbers.update({7,14})
print(numbers)

#add
numbers.add(20)
print(numbers)

#pop

numbers.pop()
print(numbers)

#list

k=list(numbers)
print(k[3])

#sort

s=sorted(numbers)
print(s)

#reverse

s=sorted(numbers,reverse=True)
print(s)

#remove
color={"red","blue","white"}
color.remove("blue")
print(color)

#discard
color.discard("redo")
print(color)

print("-"*50)

#union

raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja | rani
print(colors)


raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja.union(rani)
print(colors)

s=sorted(colors)
print(s)


#intersection

raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja & rani
print(colors)

raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja.intersection(rani)
print(colors)

#Difference

raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja - rani
print(colors)

raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja.difference(rani)
print(colors)

#symmetric(leave common elements in both set)

raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja ^ rani
print(colors)


raja={"red","green","blue","pink"}
rani={"green","pink","white"}
colors=raja.symmetric_difference(rani)
print(colors)



list=[4,7,8,10,45]
for i in list:
    if i%2==0:
       print(i)


list=[4,7,8,10,45]
em=[]
for i in list:
    if i%2==0:
        em.append(i)
print(em)

res=[s for s in range(1,20) if s%2==0]
print(res)

res=[s**3 for s in range(1,5)]
print(res)


res=[s**3 for s in range(1,20) if s%2==0]
print(res)

res=[s for s in range(1,20) if s%2==0 or s%3==0]
print(res)

res=[s for s in range(1,20) if s%2==0 and s%3==0]
print(res)


seats={1,2,3,4,5,6,7,8,9,10}
even_seats =[seat for seat in seats if seat % 2==0]
print("Available seats:",seats)

print("\nEven number seats:",even_seats)


