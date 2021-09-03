import csv


with open('Crimes.csv', 'r', encoding='utf-8') as file:
    reader = list(csv.reader(file))
    crimes_2015 = [line for line in reader if line[2][8:10] == '15']
    print(crimes_2015)
    crime_types = set()
    for el in crimes_2015:
        crime_types.add(el[5])
    crime_types.discard('')
    crimes_count = dict.fromkeys(crime_types, 0)
    for el in crimes_2015:
        crimes_count[el[5]] += 1
    print(crimes_count)
    max_count, max_crime = 0, ''
    for key, value in crimes_count.items():
        if value > max_count:
            max_count = value
            max_crime = key
    print(max_crime, crimes_count[max_crime])