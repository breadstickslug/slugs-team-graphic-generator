from viz.models import Move
import csv


def find_move_name(move_id):
    with open("csv/move_names.csv", encoding="utf8") as names:
        names_reader = csv.reader(names)
        next(names_reader)
        print(move_id)
        for row in names_reader:
            if int(row[0]) == move_id and int(row[1]) == 9:
                return row[2]
    return None

def find_move_desc(move_id):
    with open("csv/move_flavor_text.csv", encoding="utf8") as desc:
        desc_reader = csv.reader(desc)
        next(desc_reader)
        for row in desc_reader:
            if int(row[0]) == move_id and int(row[1]) == 20 and int(row[2]) == 9:
                return row[3]
    return None

def fix_bp_acc(row, idx):
    if row[idx] == '':
        return 0
    return int(row[idx])

with open("csv/moves.csv", encoding="utf8") as moves:
    moves_reader = csv.reader(moves)
    next(moves_reader)
    for row in moves_reader:
        _, created = Move.objects.get_or_create(
                move_id = int(row[0]),
                move_name = find_move_name(int(row[0])),
                move_type_id = int(row[3]),
                move_base_power = fix_bp_acc(row, 4),
                move_pp = int(row[5]),
                move_accuracy = fix_bp_acc(row, 6),
                move_priority = int(row[7]),
                move_damage_class = int(row[9]),
                move_description = find_move_desc(int(row[0])),
            )
