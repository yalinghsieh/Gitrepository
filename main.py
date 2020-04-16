import requests
from data import Location, WeatherElement

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)

json_content = html_content.json()
#print(json_content)

records = json_content.get('records')
location = records.get('location')
#print(location)
#for i in range(len(location)):
#    print(location[i])

allLocations = []
for item in location:
    l = Location()
    l.from_json(item)

    weather_element_json = item.get('weatherElement')
    element = WeatherElement()
    element.from_json(weather_element_json)
    l.weather_element = element

    allLocations.append(l)

'''
locations = []
for l in location:

    location_site = Location()
    location_site.from_json(l)
    locations.append(location_site)

    lat = l.get('lat')
    lon = l.get('lon')
    location_name = l.get('locationName')
    station_id = l.get('stationId')
    time = l.get('time').get('obsTime')
    print(location_name, station_id, time)


    weather_element = l.get('weatherElement')
    for element in weather_element:
        element_name = element.get('elementName')
        element_value = element.get('elementValue')
        print(element_name, element_value)
'''
