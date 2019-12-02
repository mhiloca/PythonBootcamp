from csv import DictReader, DictWriter


def cm_in(c):
    return float(c) * 0.393701


with open('fighters.csv') as file_r:
    csv_reader = DictReader(file_r)
    with open('fighters_inches.csv', 'w') as file_w:
        headers = ('Name', 'Country', 'Height (in In)')
        csv_writer = DictWriter(file_w, fieldnames=headers)
        csv_writer.writeheader()
        for fighter in csv_reader:
            csv_writer.writerow({
                'Name': fighter['Name'],
                'Country': fighter['Country'],
                'Height (in In)': round(cm_in(fighter['Height (In Cm)']), 1)
            })
