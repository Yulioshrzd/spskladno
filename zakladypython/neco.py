cisla = [5, 2, 8, 1, 9, 2, 5]
print(f"Původní: {cisla}")
print(f"Délka:   len() = {len(cisla)}")
print(f"Počet 2: .count(2) = {cisla.count(2)}")
print(f"Index 8: .index(8) = {cisla.index(8)}")

# sorted() - NOVÝ list (původní se nezmění!)
serazeny = sorted(cisla)
print(f"\nsorted(cisla) = {serazeny}")
print(f"Původní cisla = {cisla}")  # nezměněn!

cisla.sort()
print(f"\nPo cisla.sort(): {cisla}")

# .reverse() - obrátí pořadí
cisla.reverse()
print(f"Po .reverse():   {cisla}")

# in - kontrola přítomnosti
print(f"\n5 in cisla: {5 in cisla}", end="\t")
print(f"3 in cisla: {3 in cisla}")

