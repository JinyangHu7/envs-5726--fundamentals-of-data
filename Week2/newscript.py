import sys
from math import remainder

sys.path.insert(1, r'/Users/admin/PycharmProjects/envs-5726--fundamentals-of-data/Week2')

import organizations

american_water = organizations.Company(
    name='American Water',
    market_cap=28940000000,
    share_value=148.4
)

american_water_shares = american_water.get_number_of_shares()
print(american_water_shares)

partnership_of_delaware_estuary = organizations.NonProfit(
    name='Partnership of the Delaware Estuary',
    assets=3140000,
    designation='501c3'
)

print(partnership_of_delaware_estuary.name)
print(partnership_of_delaware_estuary.assets)
print(partnership_of_delaware_estuary.designation)

remainder = 10%3
print(remainder)

import math
print(dir(math))

Q = 131400
CODd = 0.000918
B0 = 0.3
GWPch4 = 85.34
L = 0.1
EG = 198.5
EF = 0.581
PE = Q * CODd * B0 * GWPch4 * L - EG * EF
print (PE)


