import berechnung
import collections

astrodata = {}
astrodata_combinations = []
astro_combi = {}
new_astro = {}
sort_astro = {}
i = 0
j = 0
k = 1
with open('astrodata.txt') as file:
    for line in file:
        (key, value) = line.replace('24.12.2020', ' ').strip().split(None, 1)
        value = value[:6]  # kürzen der länge
        astrodata[key] = value
file.close()
# print(astrodata)

astrodata_combinations = berechnung.combis(astrodata)  # erstellt combinationen aus den ersten 10 // len() 45
# print(astrodata_combinations)

# erstellt dictionary aus den combinationen
for x in astrodata_combinations:
    key, value = berechnung.create_pairs(*astrodata_combinations[i])
    astro_combi[key] = value
    i += 1

astro_combi.update(astrodata.items())  # fügt die ersten 10 zu den combinationen hinzu // len() 55
# print(astro_combi)
astro_combi = berechnung.combis(astro_combi)  # erstellt alle möglichen combinationen aus den 55 vorherigen //len() 1485
# print(astro_combi)


for x in astro_combi:
    key, value = berechnung.create_finalpairs(*astro_combi[j])
    new_astro[key] = value
    j += 1

new_astro = {k:v for k,v in new_astro.items() if k.count('HS') < 2}
new_astro = {k:v for k,v in new_astro.items() if v[0] != None}

# print(len(new_astro))
sort_astro = collections.OrderedDict(sorted(new_astro.items(), key=lambda x: x[1][3], reverse=True))
# key = lambda x : x[1][3], x = Key-Value-Paar in Dict, x[0] = Key in Dict, x[1] = Value (List) in Dict, x[1][3] = Element an Speicherstelle 3 in List
# print(sort_astro)
# print(len(sort_astro))
with open('astrodataOut.txt', 'w') as output:
    for key, value in sort_astro.items():
        if key.count('HS') == 0:
            print("{:2d}. *{:<29}: {:<12} {:<7} {:<3} {:<2}%".format(k, key, value[0], value[1],
                                                                         value[2], value[3]),
                  file=output)
            k += 1
        else:
            print("{:2d}. {:<30}: {:<12} {:<7} {:<3} {:<2}%".format(k, key, value[0], value[1], value[2],
                                                                       value[3]), file=output)
            k += 1
    output.close()
