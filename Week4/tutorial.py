tree_list = ['Hedge Maple', 'Honey Locust', 'Sweetgum']
for tree in tree_list:
    print(tree)

for index, tree in enumerate(tree_list):
    print(f'{index}: {tree}')

natural_disasters_2024_table = [
    ['Natural Disasters by Type', 'Occurrences in Global South', 'Occurrences in Global North'],
    ['Storms', 108, 36],
    ['Floods', 132, 8],
    ['Mass Movement', 33, 0],
    ['Earthquake', 33, 0],
    ['Droughts', 11, 1]
]

headers = natural_disasters_2024_table[0]
for row in natural_disasters_2024_table[1:]:
     print(row[headers.index('Occurrences in Global South')])

from pathlib import Path
folder_path = Path('/Users/admin/Downloads/MyPythonFile.py')
print(folder_path.exists())