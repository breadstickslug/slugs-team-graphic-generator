from viz.models import Species
import csv

#with open("csv/pokemon_species.csv", encoding="utf8") as species:
#        species_reader = csv.reader(species)
#        next(species_reader)
#        for r in species_reader:
#            curr_species = Species.objects.filter(species_id = int(r[0]))
#            for s in curr_species:
#                s.species_gender_ratio = int(r[8])
#                s.save()

# 0: all male
# 8: all female
# 4: both
# -1: genderless

grid = [
    -1, # deoxys
    -1,
    -1,
    8, # wormadam
    8,
    -1, # shaymin
    -1, # giratina
    -1, # rotom
    -1,
    -1,
    -1,
    -1,
    4, # castform sun
    4, # castform rain
    4, # castform snow
    4, # basculin
    4, # darmanitan
    -1, # meloetta
    0, # tornadus
    0, # thundurus
    0, # landorus
    -1, # kyurem
    -1,
    -1, # keldeo resolute
    8, # meowstic female
    4, # aegislash
    4, # pumpkaboo
    4,
    4,
    4, # gourgeist
    4,
    4,
    4, # venusaur mega
    4,
    4,
    4,
    4,
    4,
    8, # kangaskhan mega
    4,
    4,
    4,
    -1, # mewtwo x
    -1, # mewtwo y
    4,
    4,
    4, # heracross mega
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4, # abomasnow mega
    8, # floette eternal
    8, # latias mega
    0, # latios mega
    4, # swampert mega
    4,
    4,
    4,
    0, # gallade mega
    4,
    4,
    4,
    4,
    4,
    4,
    -1, # diancie mega
    4,
    -1, # kyogre
    -1, # groudon
    -1, # rayquaza mega
    8, # cosplay pikachu rockstar
    8,
    8,
    8,
    8,
    8,
    -1, # hoopa
    4, # camerupt mega
    4,
    4,
    4,
    4, # rattata alola
    4,
    4, # rat totem alola
    0, # original cap pikachu
    0,
    0,
    0,
    0,
    0,
    4, # raichu alola
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    0, # battle bond greninja
    0,
    -1, # zygarde 10 pc
    -1, # zygarde 50 pc
    -1, # zygarde complete
    4, # gumshoos totem
    4,
    4, # oricorio
    4,
    4,
    4, # lycanroc midnight
    4, # wishiwashi totem
    4, # lurantis totem
    8, # salazzle totem
    -1, # minior orange meteor
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    4, # mimikyu
    4,
    4,
    4, # kommo totem
    -1, # magearna
    0, # pikachu partner cap
    4, # marowak totem
    4, # ribombee totem
    4, # rockruff OT
    4, # lycanroc dusk
    4, # araquanid totem
    4,
    -1, # necrozma
    -1,
    -1,
    4, # pika starter
    4,
    0, # pikachu world cap
    4, # meowth galar
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    -1,
    -1,
    -1,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    -1, # zygarde 10
    4, # cramorant
    4,
    4, # tox lowkey
    4, # eiscue noice
    8,
    4,
    -1,
    -1,
    -1,
    4,
    -1,
    -1,
    -1
    ]
print(len(grid))
print(len(grid)+10000)
for i in range(10001, 10195):
    curr_species = Species.objects.filter(species_id = i)
    for s in curr_species:
        print(i)
        s.species_gender_ratio = grid[i-10001]
        s.save()
