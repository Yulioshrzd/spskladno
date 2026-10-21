def trikrat_plus_jedna(cislo):
    cislo = cislo * 3 + 1 
    return cislo

for i in range(0, 19, 3):
    print(f"Pro hodnotu {i} je výsledek {trikrat_plus_jedna(i)}")
