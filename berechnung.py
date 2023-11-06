from itertools import combinations

if __name__ == "__main__":
    print("Executed")
else:
    aspekt = {'Konjunktion': 0, 'Sextil': 60, 'Quadrat': 90,
              'Trigon': 120, 'Opposition': 180}
# input: dictionary
    # create list of combinations from dict of 2 pairs
    def combis(dict):
        return list(combinations(dict.items(), 2))

# input: 2x tupel, return str, float
# create first combination Halfsum
    def create_pairs(keyvalue_one, keyvalue_two):
        key_one, value_one = keyvalue_one
        key_two, value_two = keyvalue_two
        key_one = str(key_one)
        value_one = float(value_one)
        key_two = str(key_two)
        value_two = float(value_two)
        key_sum = 'HS(' + key_one + '/' + key_two + ')'
        # print(key_sum)
        value_sum = (value_one + value_two) / 2
        if value_sum < 180:
            value_sum = value_sum + 180
        value_sum = round(value_sum, 4)
        # print(value_sum)
        return key_sum, value_sum

# input: 2x tupel, return str, list
    # create final key-value-pair
    def create_finalpairs(tupelone, tupeltwo):
        key_one, value_one = tupelone
        key_two, value_two = tupeltwo
        key_one = str(key_one)
        key_two = str(key_two)
        value_one = float(value_one)
        value_two = float(value_two)
        actual_winkel = min(abs(value_one - value_two), 360 - abs(value_one-value_two))
        actual_winkel = round(actual_winkel, 2) # tatsächlicher winkel
        #kon = str(kon)
        final_key = key_one + '-' + key_two
        if final_key.count('HS') == 1:
            orbis = 3.5
        else:
            orbis = 4.0
        aspekt_winkel = spielraum(actual_winkel, orbis) # aspekt winkel
        aspect = lookup_aspekt(aspekt_winkel)
        for key, value in aspekt.items():
            if aspekt_winkel == value:
                guete = ((orbis - abs(aspekt_winkel - actual_winkel)) / orbis) * 100
                guete = round(guete)
                break
            else:
                guete = 0
        valuelist_ofkey = [aspect, actual_winkel, orbis, guete]
        return final_key, valuelist_ofkey

# input: int
    # find key compared to value
    def lookup_aspekt(winkel):
        for key, value in aspekt.items():
            if winkel == value:
                return key

# input: int
# check int in orbis range
# later, compared with aspect-dict to get Key
    def spielraum(winkel, orbis):
        if winkel <= orbis:
            winkel = aspekt['Konjunktion']
        elif winkel >= (aspekt['Sextil'] - orbis) and winkel <= (aspekt['Sextil'] + orbis):
            winkel = aspekt['Sextil']
        elif winkel >= (aspekt['Quadrat'] - orbis) and winkel <= (aspekt['Quadrat'] + orbis):
            winkel = aspekt['Quadrat']
        elif winkel >= (aspekt['Trigon'] - orbis) and winkel <= (aspekt['Trigon'] + orbis):
            winkel = aspekt['Trigon']
        elif winkel >= (aspekt['Opposition'] - orbis) and winkel <= (aspekt['Opposition'] + orbis):
            winkel = aspekt['Opposition']
        return winkel

# no use yet
"""
    def tierzeichen(halfsum):
        zeichen = ['ar', 'pi', 'aq', 'cp', 'sa', 'sc', 'li', 'vi', 'le', 'cn', 'ge', 'ta']
        posi = halfsum / 30
        posi = int(posi)
        return zeichen[posi]
"""