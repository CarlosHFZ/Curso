import phonenumbers
from phonenumbers import geocoder, carrier

PhoneNumber = phonenumbers.parse('+5548988157712')
Carrier = carrier.name_for_number(PhoneNumber, 'pt-br')
Geocode = geocoder.country_name_for_number(PhoneNumber, 'pt-br')

print(f'Seu numero de operadora é {Carrier} e sua localidade é {Geocode}')