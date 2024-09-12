import os
os.system("cls")

#dastur parollarni saqlaydi
class ParolManager:
    def __init__(self):
        self.ilova = []
        self.parol = []

    def parol2(self):
        nom = input("Nimani parolini kiritmoqchi siz: ")
        parollar = input("Parolni kiriting: ")
        self.ilova.append(nom)
        self.parol.append(parollar)

    def parol3(self):
        kor = input("\nNimani parolini ko'rmoqchisiz: ")
        if kor in self.ilova:
            index = self.ilova.index(kor)
            print("Parol:", self.parol[index])
        else:
            print("Buni parolini saqlamagan siz")

n = int(input("Nechta parol saqlamoqchisiz: "))
saqla = ParolManager()

for i in range(n):
    saqla.parol2()

saqla.parol3()