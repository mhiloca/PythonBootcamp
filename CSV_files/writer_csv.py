from csv import writer, reader

# with open('example.csv', 'w') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['Character', 'Move'])
#     csv_writer.writerow(['Ruy', 'Hadouken'])

# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     with open('screaming_fighters.csv', 'w') as f:
#         csv_writer = writer(f)
#         for fighter in csv_reader:
#             csv_writer.writerow([r.upper() for r in fighter])


with open('fighters.csv') as fi:
    csv_reader = reader(fi)
    fighters = [[r.upper() for r in row] for row in csv_reader]
with open('screaming_fighters.csv', 'w') as fil:
    csv_writer = writer(fil)
    for fighter in fighters:
        csv_writer.writerow(fighter)

