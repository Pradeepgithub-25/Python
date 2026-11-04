num = 23
rev = 0
while num >0:
    rem =num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)

'''
correct_pin = "1234"
pin = ""

while pin != correct_pin:
    pin = input("Enter your Atm Pin: ")
print("Login Successfull")'''



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
