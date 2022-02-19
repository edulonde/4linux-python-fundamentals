from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes")  # Nome do seu aplicativo
location = geolocator.geocode("Rua Lírio do Amazonas, 395, Campinas, SP, Brazil")
print(location.address)
print((location.latitude, location.longitude))

location_string = str(location.address).split(",")

if location_string[0] != 'None':
    print("Bairro......", location_string[1])
    print("Cidade......", location_string[2])
    print("Região......", location_string[3])
