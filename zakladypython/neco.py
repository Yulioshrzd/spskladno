oblibene_filmy = ["Matrix", "Logan"]

film1 = input("Zadej 1. nazev filmu: ")
film2 = input("Zadej 2. nazev filmu: ")
film3 = input("Zadej 3. nazev filmu: ")

oblibene_filmy.append(film1)
oblibene_filmy.append(film2)
oblibene_filmy.append(film3)

print("Tvoje nejoblibenejsi filmy jsou: ")
for film in oblibene_filmy:
    print(film)

print()
print(f"Tvoje oblibene filmy je {len(oblibene_filmy)}")

