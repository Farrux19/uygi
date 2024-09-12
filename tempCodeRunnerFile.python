import os
os.system("cls")

class Telefon:
    def __init__(self):
        self.telefon_raqam = ""
        self.narx = 0

    def raqam_olish(self):
        self.telefon_raqam = input("Telefon raqamini kiriting: ")
        self.narx = self.narxni_hisoblash()

    def narxni_hisoblash(self):
        for raqam in set(self.telefon_raqam):
            if self.telefon_raqam.count(raqam) > 1:
                return 10
        return 5

    def raqamni_tekshirish(self):
        if len(self.telefon_raqam) == 9 and self.telefon_raqam.isdigit():
            print("Telefon raqami to'g'ri kiritildi:", self.telefon_raqam)
            print("Telefon raqami narxi: ", self.narx, "$")
            self.sotib_olish()
        else:
            print("Telefon raqami 9 ta sondan iborat bo'lishi kerak.")

    def sotib_olish(self):
        javob = input("Telefon raqamini sotib olasizmi (1 - Ha, 0 - Yo'q): ")
        if javob == "1":
            print("Telefon raqami berildi:", self.telefon_raqam)
        elif javob == "0":
            print("Telefon raqami bekor qilindi.")
        else:
            print("Noto'g'ri tanlov!")

telefon = Telefon()
telefon.raqam_olish()
telefon.raqamni_tekshirish()