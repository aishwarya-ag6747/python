import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobilelo = input("Enter Mobile Number with Country code: ")
mobileNo= phonenumbers.parse(mobileNo) 
print (timezone.time_zones_for_number (mobileNo))
print(carrier.name_for_number(mobileNo, "en"))
print(geocoder.description_for_number(mobileNo, "en"))
print("Valid Mobile Number :",phonenumbers.is_valid_number(mobileNo))
print("checking possibility of number :",phonenumber.is_possible_number(mobile))
