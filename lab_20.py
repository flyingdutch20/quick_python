import csv
input = [fields for fields in csv.reader(open("illinois_weather_1979-2011.txt",
                                               newline=''), delimiter="\t")]
def cleanse(record):
    ints = [2,6,10,14]
    floats = [5,7,8,9,11,12,13,15,16]
    perc = [17]
    for i in ints:
        try:
            record[i] = int(record[i])
        except ValueError:
            record[i] = None
    for j in floats:
        try:
            record[j] = float(record[j])
        except ValueError:
            record[j] = None
    for k in perc:
        try:
            my_str = record[k]
            my_perc = float(my_str[:-1])
            my_float = my_perc / 100
            record[k] = my_float
        except ValueError:
            record[k] = None



result = []
result.append(input[0])

for record in input:
    try:
        if record[4] == "17031":
            cleanse(record)
            result.append(record)
    except IndexError:
        pass

from openpyxl import Workbook
data_rows = [fields for fields in result]
wb = Workbook()
ws = wb.active
ws.title = "Temperature data"
for row in data_rows:
    ws.append(row)
wb.save("temp_data.xlsx")
