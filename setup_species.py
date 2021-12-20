from viz.models import Species, Move
import csv

def find_mon_name(species_id):
    with open("csv/pokemon_species_names.csv", encoding="utf8") as names:
        names_reader = csv.reader(names)
        next(names_reader)
        print(species_id)
        for row in names_reader:
            if int(row[0]) == species_id and int(row[1]) == 9:
                return row[2]
    with open("csv/pokemon_form_names.csv", encoding="utf8") as names:
        names_reader = csv.reader(names)
        next(names_reader)
        for row in names_reader:
            if int(row[0]) == species_id and int(row[1]) == 9:
                return row[3]
    return ""

def find_form_name(form_id):
    with open("csv/pokemon_form_names.csv", encoding="utf8") as names:
        names_reader = csv.reader(names)
        next(names_reader)
        for row in names_reader:
            if int(row[0]) == form_id and int(row[1]) == 9:
                return row[2]
    return ""

def mon_type(mon_id, slot):
    with open("csv/pokemon_types.csv", encoding="utf8") as names:
        names_reader = csv.reader(names)
        next(names_reader)
        for row in names_reader:
            if int(row[0]) == mon_id and int(row[2]) == slot:
                return row[1]
    return None

def mon_ability(mon_id, slot):
    with open("csv/pokemon_abilities.csv", encoding="utf8") as names:
        names_reader = csv.reader(names)
        next(names_reader)
        for row in names_reader:
            if int(row[0]) == mon_id and int(row[3]) == slot:
                return row[1]
    return None

with open("csv/pokemon_forms.csv", encoding="utf8") as mons:
    species_reader = csv.reader(mons)
    next(species_reader)
    for row in species_reader:
        #_, created = Species.objects.get_or_create(
        print(int(row[0]))
        mon = Species.objects.create(
            species_id = int(row[3]),
            #species_name = find_mon_name(int(row[0])),
            species_name = row[1].title(),
            #species_form_name = find_form_name(int(row[0])) if row[2] else "",
            species_form_name = row[2].title() if row[2] else "",
            species_type_1 = mon_type(int(row[3]), 1),
            species_type_2 = mon_type(int(row[3]), 2),
            species_ability_1 = mon_ability(int(row[3]), 1),
            species_ability_2 = mon_ability(int(row[3]), 2),
            species_ability_3 = mon_ability(int(row[3]), 3)
        )
        mon.save()
