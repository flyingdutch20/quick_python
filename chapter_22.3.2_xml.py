import requests
import xmltodict
from datetime import date, timedelta


xml_page = requests.get("https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?whichClient=NDFDgen&lat=41.87&lon=+-87.65&product=glance")
dict = xmltodict.parse(xml_page.content)
tomorrow = date.today() + timedelta(days=1)
tomorrow_str = tomorrow.strftime("%Y-%m-%d")
dates = dict["dwml"]["data"]["time-layout"][0]["start-valid-time"]

temps = dict["dwml"]["data"]["parameters"]["temperature"][0]["value"]

for i in range (len(dates)):
    my_date = dates[i]["#text"]
    if my_date.find(tomorrow_str) > -1:
        print(temps[i])
        break
