import bs4
import csv
html = open("code/chs21-24_code/forecast.html")
bs = bs4.BeautifulSoup(html, "html.parser")
days = [x.text for x in bs.select(".forecast-label")]
forecast = [x.text for x in bs.select(".forecast-text")]
output = list(zip(days,forecast))
csv.writer(open("forecast.csv","w",newline='')).writerows(output)

#rows = bs.select(".row")
#output = []
#for row in rows:
#    day = row[0].text
#    forecast = row[1].text
#    output.append([day, forecast])
