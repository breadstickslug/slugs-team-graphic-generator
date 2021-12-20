from viz.models import Species, Move
import csv

evo_dict = {}
with open("csv/pokemon_species.csv", encoding="utf8") as species:
    reader = csv.reader(species)
    next(reader)
    for mon in reader:
        if mon[3]:
            evo_dict[mon[0]] = [int(mon[3])]
for mon in evo_dict:
    if str(evo_dict[mon][0]) in evo_dict:
        evo_dict[mon] = [evo_dict[mon][0], evo_dict[str(evo_dict[mon][0])][0]]

evo_dict["10004"] = [412] # worm sand
evo_dict["10005"] = [412] # worm trash
evo_dict["10017"] = [554] # darm zen
evo_dict["10025"] = [677] # meowstic f
evo_dict["10026"] = [679, 680] # aegislash blade
evo_dict["10030"] = [10027] # gourg s
evo_dict["10031"] = [10028] # gourg l
evo_dict["10032"] = [10029] # gourg xl
evo_dict["10033"] = [1, 2] # venu mega
evo_dict["10034"] = [4, 5] # zard x
evo_dict["10035"] = [4, 5] # zard y
evo_dict["10036"] = [7, 8] # blastoise mega
evo_dict["10037"] = [63, 64] # zam mega
evo_dict["10038"] = [92, 93] # gengar mega
evo_dict["10041"] = [129] # gyara mega
evo_dict["10045"] = [179, 180] # ampharos mega
evo_dict["10046"] = [123] # scizor mega
evo_dict["10048"] = [228] # hound mega
evo_dict["10049"] = [246, 247] # ttar mega
evo_dict["10050"] = [255, 256] # blaziken mega
evo_dict["10051"] = [280, 281] # gardevoir mega
evo_dict["10053"] = [304, 305] # aggron mega
evo_dict["10054"] = [307] # cham mega
evo_dict["10055"] = [309] # manectric mega
evo_dict["10056"] = [353] # banette mega
evo_dict["10058"] = [443, 444] # chomp mega
evo_dict["10059"] = [447] # lucario mega
evo_dict["10060"] = [459] # aboma mega
evo_dict["10064"] = [258, 259] # swamp mega
evo_dict["10065"] = [252, 253] # scept mega
evo_dict["10067"] = [333] # altaria mega
evo_dict["10068"] = [280, 281] # gallade mega
evo_dict["10070"] = [318] # sharpedo mega
evo_dict["10071"] = [79] # slowbro mega
evo_dict["10072"] = [95] # steelix mega
evo_dict["10073"] = [16, 17] # pidgeot mega
evo_dict["10074"] = [361] # glalie mega
evo_dict["10076"] = [374, 375] # metagross mega
evo_dict["10087"] = [322] # camerupt mega
evo_dict["10088"] = [427] # lopunny mega
evo_dict["10089"] = [371, 372] # mence mega
evo_dict["10090"] = [13, 14] # beedrill mega
evo_dict["10092"] = [10091] # raticate alola
evo_dict["10100"] = [172, 25] # raichu alola
evo_dict["10102"] = [10101] # sandslash alola
evo_dict["10104"] = [10103] # ninetales alola
evo_dict["10106"] = [10105] # dugtrio alola
evo_dict["10108"] = [10107] # persian alola
evo_dict["10110"] = [10109] # graveler alola
evo_dict["10111"] = [10109, 10110] # golem alola
evo_dict["10113"] = [10112] # muk alola
evo_dict["10114"] = [102] # exegg alola
evo_dict["10115"] = [104] # wak alola
evo_dict["10126"] = [744] # lycanroc midnight
evo_dict["10152"] = [10151] # lycanroc dusk
evo_dict["10163"] = [10162] # rapidash galar
evo_dict["862"] = [10175] # obstagoon
evo_dict["863"] = [10161] # perrserker
evo_dict["864"] = [10173] # cursola
evo_dict["865"] = [10166] # sirfetchd
evo_dict["866"] = [10168] # mr rime
evo_dict["867"] = [10179] # runerigus
evo_dict["10165"] = [10164] # slowbro galar
evo_dict["10167"] = [109] # weezing galar
evo_dict["10168"] = [439] # mr mime galar
evo_dict["10172"] = [10164] # slowking galar
evo_dict["10175"] = [10174] # linoone galar
evo_dict["10177"] = [10176] # darm galar
evo_dict["10178"] = [10176] # darm galar zen
evo_dict["10184"] = [848] # tox low key
evo_dict["10191"] = [891] # urshifu R

#print(evo_dict)

ed2 = {}
for mon in evo_dict:
    for prevo in evo_dict[mon]:
        if str(prevo) not in ed2:
            ed2[str(prevo)] = [int(mon)]
        else:
            ed2[str(prevo)] = ed2[str(prevo)] + [int(mon)]

#print(ed2)

for mon in ed2:
    pokemon_data = Species.objects.filter(species_id = mon)[0]
    print(pokemon_data)
    for evo in ed2[mon]:
        evo_datas = Species.objects.filter(species_id = evo)
        for match in evo_datas:
            print("inheriting to "+match.species_name)
            for move in pokemon_data.learnset.all():
                match.learnset.add(move)
