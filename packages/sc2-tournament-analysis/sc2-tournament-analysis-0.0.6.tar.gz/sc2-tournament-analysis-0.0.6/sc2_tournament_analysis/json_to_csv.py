import json
import csv
import logging


def json_to_csv(headers, filename=None):
    logging.basicConfig(filename='json_to_csv.log', level=logging.DEBUG)

    if filename:
        with open(filename, 'r', encoding='utf-8') as data:
            match_info = json.load(data)[filename]
    else:
        with open('match_info.json', 'r', encoding='utf-8') as data:
            match_info = json.load(data)['match_info']

    if type(headers) is not list:
        csv_rows = [tuple(headers)]
    else:
        logging.critical('Error: headers argument is not a list')
        return

    for unit_record in match_info:
        csv_rows.append(tuple(value for value in unit_record.values()))

    with open('match_info.csv', 'w', encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(csv_rows)
