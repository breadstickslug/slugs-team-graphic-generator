from viz.models import Species, Move
import csv

with open("csv/pokemon_moves.csv", encoding="utf8") as moves:
    learnset_reader = csv.reader(moves)
    next(learnset_reader)
    curr_mon_id = 0
    curr_species = Species.objects.filter(species_id = curr_mon_id)
    learn_set = set()
    moves_set = set()
    for r in learnset_reader:
        if curr_mon_id != int(r[0]) and int(r[0]) == 10194:
            if curr_mon_id != 0:
                #print(learn_set)
                for mon in curr_species:
                    mon.learnset.clear()
                    for mv in moves_set:
                        #print("adding "+str(mv)+" to "+mon.species_name+"-"+mon.species_form_name)
                        mon.learnset.add(mv)
            learn_set = set()
            moves_set = set()
            curr_mon_id = int(r[0])
            #print(curr_mon_id)
            curr_species = Species.objects.filter(species_id = curr_mon_id)
            print(curr_species)
        if int(r[0]) == 10194:
            move = Move.objects.filter(move_id = int(r[2]))[0]
            #print(move)
            if str(move) not in learn_set:
                learn_set.add(str(move))
                moves_set.add(move)
    for mon in curr_species:
        mon.learnset.clear()
        for mv in moves_set:
            #print("adding "+str(mv)+" to "+mon.species_name+"-"+mon.species_form_name)
            mon.learnset.add(mv)
