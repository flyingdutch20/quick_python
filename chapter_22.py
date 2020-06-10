import requests
metoffice_url = "http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt"
mars_rover_url = "http://marsweather.ingenology.com/v1/latest/?format=json"
response = requests.get(mars_rover_url)
print(response.text)