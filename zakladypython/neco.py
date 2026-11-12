vek = int(input("Kolik ti je let?: "))
student = input("Jseš student školy? (ano/ne): ")
doprovod = input("Máš doprovod dospělého? (ano/ne): ")
zakaz_vstupu = input("Máš zakaz vstupu? (ano/ne): ")

if vek >= 15 and student == "ano" and doprovod == "ano" and zakaz_vstupu == "ne":
    print("Vstup povolen.")
else:
    print("Vstup neni povolen")