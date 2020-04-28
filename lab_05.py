temperatures = []
with open('./exercise_answers/lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

sorted = sorted(temperatures)

print('min: ' + str(sorted[0]) + ' max: ' + str(sorted[-1]) + ' average: ' + str(sum(temperatures)/len(temperatures)) +
      ' median: ' + str(sorted[(len(sorted)//2)]) + ' unique: ' + str(len(set(temperatures))))
