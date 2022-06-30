#Importing the libraries
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

#Taking input number
number = input('Enter your mobile number with +880: ')

#Processing number details
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')

#Printing number details
print(phone)
print(time)
print(car)
print(reg)