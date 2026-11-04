i=1
while i<=10:
 print(i)
 i=i+1

num=29
check=29/10
print(check)

num=29
check=29%10
print(check)

num=29
check=29//10
print(check)

num = 29
rev = 0
while num >0:
 rem =num%10
 rev=(rev*10)+rem
 num=num//10
print(rev)

num = 2
rev = 0
while num >0:
 rem =num%10
 rev=(rev*10)+rem
 num=num//10
print(rev)

num = 1192
rev = 0
count = 0
while num >0:
 rem =num%10
 rev=(rev*10)+rem
 num=num//10
 count=count+1
print(rev)
print("no.of.digit:",count)

'''
correct_pin = "1234"
pin= ""

while pin != correct_pin:
 pin = input("Enter your Atm Pin: ")
print("Login Successfull")'''


print("-"*50)

print("Available seat number")

for seat in range (1,11):
    print("Seat number:", seat)

for i in range (1,10):
    print(i)



sum = 0
for i in range (1,6):
        sum=sum+i
        print(sum)
'''
n = int(input("Enter the number:"))
sum = 0
for i in range (1,n+1):
        sum=sum+i
        print(sum)'''

total_seats=5

for booking in range(1,10):
    if booking > total_seats:
        print("No seats available")
        break
    
    if booking == 3:
        print("check Special Reservation")
        continue
    pass
    print("Seat", booking, "Booked Successfully")



i=5
for i in range (1,10):
    if i==4:
        break
    print(i)

print("-"*50)


i=6
for i in range (1,10):
    if i==4:
        continue
    print(i)


print("-"*50)

i=6
for i in range (1,10):
    if i%2==0:
        continue
    print(i)
