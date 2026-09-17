print(dir(bool))

green_bool = "greenfield".startswith("green")
print(green_bool)

equal_bool = 5 == 4
print(equal_bool)

general_motors_risk_rating = 27.6
general_motors_emissions_ambition = 'YES, MEETS ALL CRITERIA'

is_general_motors_risk = general_motors_risk_rating <= 25
print(is_general_motors_risk)


is_general_motors_sustainable = is_general_motors_risk and general_motors_emissions_ambition == 'YES, MEETS ALL CRITERIA'
print (is_general_motors_sustainable)

if True:
    print(11111)

if False:
    print(22222)

traffic_light = 'Red'
if traffic_light == 'Green':
    print('Go')
elif traffic_light == 'yellow':
    print('Stop')
else:
    print('Yield')