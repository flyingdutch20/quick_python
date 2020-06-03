# variable 'records'
# open file
# read line
# split line
# write to records

import datetime
def convert_to_date(str):
    try:
        return datetime.strptime(str, "%Y/%m/%d")
    except:
        return str

def convert_to_float(str):
    try:
        return float(str)
    except:
        return str

def convert_to_int(str):
    try:
        return int(str)
    except:
        return str


records = []
#file = open("exercise_answers/temp_data_01a.txt").read()
#for line in file:
#    records.append(line.split("|"))

with open(r"exercise_answers/temp_data_01a.txt") as infile:
    for line in infile:
#        my_line = line.replace("\n","")
        record = line.replace("\n","").split("|")
        if len(record) == 4:
            record[1] = convert_to_date(record[1])
            record[2] = convert_to_float(record[2])
            record[3] = convert_to_int(record[3])
        records.append(record)

