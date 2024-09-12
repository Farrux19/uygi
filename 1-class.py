import os
os.system("cls")

class Mashina:
    def __init__(self, narxi, rangi, ot_kuchi):
        self.narxi = narxi
        self.rangi = rangi
        self.ot_kuchi = ot_kuchi

a = int(input("Nechta mashina kiritmoqchisiz: "))

mashinalar = []
b = 0
#dastur eng arzon mashinani chiqaradi
for _ in range(a):
    b += 1
    print(f"\t{b}-mashina\n")
    narxi = float(input("Mashinaning narxini kiriting: "))
    rangi = input("Mashinaning rangini kiriting: ")
    ot_kuchi = int(input("Mashinaning ot kuchini kiriting: "))
    
    mashina = Mashina(narxi, rangi, ot_kuchi)
    mashinalar.append(mashina)

kichik = min(mashinalar, key=lambda mashina: mashina.narxi)

print("\n\tEng arzon mashina:")
print(f"Narxi: {kichik.narxi}\nRangi: {kichik.rangi}\nOt kuchi: {kichik.ot_kuchi}")