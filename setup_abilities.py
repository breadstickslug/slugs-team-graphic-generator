from viz.models import Ability
import csv

with open("csv/ability_names.csv", encoding="utf8") as abilities:
    ability_reader = csv.reader(abilities)
    next(ability_reader)
    curr_a_id = 0
    for r in ability_reader:
        if curr_a_id != int(r[0]):
            curr_a_id = int(r[0])
        else:
            if int(r[1]) == 9 and int(r[0]) < 300:
                _, created = Ability.objects.get_or_create(
                        ability_id = int(r[0]),
                        ability_name = r[2],
                    )
