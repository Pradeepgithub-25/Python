
#store ticket price and seat number
train_name="Rajdhani Express"
train_number=12951
source_station="Mumbai"
destination_station="Delhi"
ticket_price=2450.7
journey_date="25-May-2026"

print(train_name,type(train_name))
print(type(train_number))
print(type(ticket_price))

print("Welcome to Indian Railway Reservation System")
print("Train Name :", train_name)
print("Train Number :", train_number)
print("Source Station :", source_station)
print("Destination Station :", destination_station)
print("journey:",journey_date)

#perform ticket fare calculation

no_of_passangers=3
ticket_price=2450
total_fare=no_of_passangers*ticket_price
print("Total fare:",total_fare)

#calculate GST on ticket fare
gst_percent=5
gst_amount=(total_fare*5)/100
print("Gst amount:",gst_amount)
Include_gst=total_fare+gst_amount
print("Total_price:",Include_gst)



#float convert to int
ticket_price_integer=int(ticket_price)
print(type(ticket_price_integer))
print(ticket_price_integer)

#int to string

train_number_string=str(train_number)
print(type(train_number_string))
print(train_number_string)

#passenger details
passanger_name="Rahul sharma"
seat_number="B2-45"

#ticket_confirmation_status
'''is_confirmed=true'''

confirmation_status="confirmed"

print("-"*20)
print("-"*50)
print("-----------Railway ticket------------")
print("passanger_name:",passanger_name)
print("Seat_no:",seat_number)
print("ticket_satus:",confirmation_status)
print("-"*50)

print("-"*50)
print("-----------Budget info------------")
print("-"*50)


# monthly expenses
salary=50000
food=3000
mobile=1000
groceries=3200
dress=1000
eb_bill=2000
fuel=3000
pocket_money=4000

expenses=food+mobile+groceries+dress+eb_bill+fuel+pocket_money

print("Person_salary:",salary)
print("Expenses amount:",expenses)
remaining_amount=salary-expenses
print(remaining_amount)


print("-----------Indian Railway ticket------------")
print("passanger_name\t\t:",passanger_name)
print("Seat_no:",seat_number)
print("ticket_satus:",confirmation_status)
print("Seat Number    :", seat_number)
print("journey_date:",journey_date)
print("Ticket Fare:", total_fare)
print("-"*50)

