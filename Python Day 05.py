'''passanger_name="Rahul Sharma"
ticket_status="Confirmed"

if ticket_status == "Confirmed":
 print("Ticket is booked")


waiting_list=3;

if waiting_list == 0:
 print("Ticked is confirmed")
else:
 print("Your ticket is in waiting list")



ticket_status="RAC"

if ticket_status == "Confirmed":
 print("Ticket is booked")
elif ticket_status == "RAC":
 print("Partial Reservation available")
else:
 print("Your ticket is in waiting list")


age=65

if age>=65:
 print("Eligible for senior citizen discount")



age=65
ticket_confirmed=True

if age>=65 and ticket_confirmed==True:
 print("Eligible for senior citizen discount benefits")



ticket_status="confirmed"
payment_status="Paid"

if ticket_status == "confirmed" and payment_status=="Paid":
 print("Ticket booked")
elif ticket_status == "RAC":
 print("Partial Reservation available")
else:
 print("Booking Pending")

 

passanger_age =26
ticket_confirmed = True

if passanger_age >=18 and  ticket_confirmed:
 print("Passenger Eligible for travel")


confirmed_seat= False
RAC_seat= True

if confirmed_seat or RAC_seat:
 print("Reservation available")
 


num=10

if (num%2==0):
 print("Even")
else:
 print("Odd")



ticket_cancelled = True

if not ticket_cancelled:
 print("Ticket booked")
else:
 print("Ticket cancelled")

passanger_age = 65
payment_completed = True

if passanger_age >=65 and payment_completed:
 print("Senior citizen reservation booked successfully")


available_seats =0
payment_status = True

if available_seats > 0 and payment_status:
 print("Your ticket is booked")
else:
 print("Ticket Confirmation Failed")



nationality = True
age = int(input("Enter the age:"))

if age>18 and nationality:
 print("Eligible to vote")
else:
 print("Not eligible")'''

 

valid_id_proof = True
booking_time_valid = True

if valid_id_proof and booking_time_valid:
 print("You are eligible for Takkal")
else:
 print("Tatkal Booking Denied")


passanger_name = "Rahul Sharma"
passanger_age = 30
available_seats = 2
payment_completed = True
ticket_cancelled = False

if ( passanger_age >= 18 and
     available_seats > 0 and
     payment_completed and
     not ticket_cancelled):
    
 print("-"*50)
 print("Welcome to Indian Railway")
 print("*"*50)
 print("Passanger_name:",passanger_name)
 print("Reservation_staus: Confirmed")
else:
 print("Reservation Failed")


for i in range(1,10,2):
 print(i);

i = 1
while i<=5:
 print(i)
i=i+i
 








