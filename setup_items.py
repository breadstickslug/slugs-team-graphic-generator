from viz.models import Item
import csv


def find_item_name(item_id):
    with open("csv/item_names.csv", encoding="utf8") as names:
        names_reader = csv.reader(names)
        next(names_reader)
        print(item_id)
        for row in names_reader:
            if int(row[0]) == item_id and int(row[1]) == 9:
                return row[2]
    return None

def find_item_desc(item_id):
    with open("csv/item_flavor_text.csv", encoding="utf8") as desc:
        desc_reader = csv.reader(desc)
        next(desc_reader)
        for row in desc_reader:
            if int(row[0]) == item_id and int(row[1]) == 20 and int(row[2]) == 9:
                return row[3]
    return ""

with open("csv/items.csv", encoding="utf8") as items:
    items_reader = csv.reader(items)
    next(items_reader)
    for row in items_reader:
        _, created = Item.objects.get_or_create(
                item_id = int(row[0]),
                item_name = find_item_name(int(row[0])),
                item_description = find_item_desc(int(row[0])),
            )
