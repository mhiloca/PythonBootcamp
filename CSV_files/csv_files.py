from csv import reader, DictReader

# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     for row in csv_reader:
#         print(row)

with open('fighters.csv') as file:
    csv_dictreader = DictReader(file)
    for row in csv_dictreader:
        print(f'{row["Name"]} is from {row["Country"]}')


