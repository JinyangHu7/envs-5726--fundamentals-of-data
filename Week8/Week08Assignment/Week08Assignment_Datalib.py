from typing import List, Any


def convert_yesno_to_binary(table: List[tuple]) -> List[tuple]:

    converted_table: List[tuple] = []
    row_class = type(table[0])

    conversion_dictionary = {
        '': 0,
        'Do not know': 0,
        'No': 0,
        'Yes': 1
    }

    for row in table:
        row_values: List[Any] = list(row)

        for index, value in enumerate(row_values):
            if value in conversion_dictionary:
                row_values[index] = conversion_dictionary[value]

        converted_row = row_class(*row_values)
        converted_table.append(converted_row)

    return converted_table