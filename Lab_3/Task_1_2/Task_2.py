import csv
from Person import Person


def modifier(filename):

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        fieldnames = reader.fieldnames

    fullname_index = fieldnames.index('first_name') + 1
    new_fieldnames = fieldnames[:fullname_index] + ['fullname'] + fieldnames[fullname_index:] + ['age']

    updated_rows = []
    for row in rows:
        person = Person(
            surname=row['surname'],
            first_name=row['first_name'],
            birth_date_str=row['birth_date'],
            nickname=row.get('nickname')
        )

        new_row = row.copy()
        new_row['fullname'] = person.get_fullname()
        new_row['age'] = person.get_age()
        updated_rows.append(new_row)

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=new_fieldnames)
        writer.writeheader()
        for row in updated_rows:
            writer.writerow(row)