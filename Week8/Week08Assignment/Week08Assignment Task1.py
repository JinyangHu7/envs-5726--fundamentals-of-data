from pathlib import Path
from collections import namedtuple
from typing import List, Type
import csv

##Task 1
csv_path = Path('/Users/admin/Downloads/IOM_Rohingya_WASH_Survey.csv')

wash_table: List[tuple] = []

with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
    reader = csv.reader(csv_file)
    headers: List[str] = next(reader)

    g_indices: List[int] = [
        index
        for index, header in enumerate(headers)
        if header.startswith('G')
    ]

    g_headers: List[str] = [
        headers[index]
        for index in g_indices
    ]

    WASHRow: Type[tuple] = namedtuple(
        typename='WASHRow',
        field_names=g_headers
    )

    for row in reader:
        g_values: List[str] = [
            row[index]
            for index in g_indices
        ]

        wash_row = WASHRow(*g_values)
        wash_table.append(wash_row)


print(wash_table[0])


##Task 2
import sys

sys.path.insert(
    1,
    '/Users/admin/PycharmProjects/envs-5726--fundamentals-of-data/Week8/Week08Assignment'
)

from Week08Assignment_Datalib import convert_yesno_to_binary


converted_wash_table = convert_yesno_to_binary(wash_table)

print(converted_wash_table[0])