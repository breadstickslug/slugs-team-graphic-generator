from viz.models import Species, Move
import csv

pokemon_data = Species.objects.filter(species_id = 1)[0]
for move in pokemon_data.learnset.all():
    print(move.move_id)
