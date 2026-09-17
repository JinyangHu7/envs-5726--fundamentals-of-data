#task1
def is_min_ratio_toilets_to_people_met(ratio):
    ratio_parts = ratio.split("/")
    toilets_text = ratio_parts[0]
    people_text = ratio_parts[1]

    toilets = int(toilets_text.split("t")[0])
    people = int(people_text.split("p")[0])

    toilet_people_ratio = toilets / people

    if toilet_people_ratio < 1 / 20:
        return False
    else:
        return True

print(is_min_ratio_toilets_to_people_met('1t/37p'))
print(is_min_ratio_toilets_to_people_met('1t/12p'))

#task2
def is_population_disabled(disabled, total_population):
    disabled_ratio = disabled / total_population

    if disabled_ratio < 0.10:
        return False
    else:
        return True

print(is_population_disabled(disabled=0, total_population=32))
print(is_population_disabled(disabled=52, total_population=392))

#task3
def is_gp_religious_or_academic(gp):
    keywords = {'Mosque', 'Church', 'School', 'Institute', 'Education', 'Faculty'}
    gp_words = set(gp.split())
    matching_words = keywords.intersection(gp_words)

    if matching_words:
        return True
    else:
        return False

print(is_gp_religious_or_academic('Faculty Of Earth Sciences and Mining'))
print(is_gp_religious_or_academic('Almorada Church'))
print(is_gp_religious_or_academic('Health Insulation Building'))

#task4
def get_sanitation_priority(ratio, disabled, pop, gp):
    ratio_met = is_min_ratio_toilets_to_people_met(ratio)
    disabled_population = is_population_disabled(disabled, pop)
    religious_or_academic = is_gp_religious_or_academic(gp)

    if (ratio_met == False and disabled_population == True and religious_or_academic == True):
        return "High Priority"

    elif (ratio_met == True and disabled_population == False and religious_or_academic == False):
        return "Low Priority"

    else:
        return "Medium Priority"

print(get_sanitation_priority(ratio='1t/49p', disabled=52, pop=392, gp='Faculty - Students Dwelling'))
print(get_sanitation_priority(ratio='1t/29p', disabled=0, pop=178, gp='Mohamed Ali Abbas Secondary School For Girls'))
print(get_sanitation_priority(ratio='1t/17p', disabled=0, pop=52, gp='Alsalam Old Mosque'))
print(get_sanitation_priority(ratio='1t/6p', disabled=0, pop=12, gp='Nile Club'))