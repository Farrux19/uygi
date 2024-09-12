import os
os.system("cls")

class ism:
    def __init__(self, ismmi, familyasi, otasini_ismi):
        self.ismmi =ismmi
        self.familyasi = familyasi
        self.otasini_ismi = otasini_ismi

#dastur ismda a harifi bolsa pasport bermaydi
ismmi = input("ism kiriting:  ")
familyasi = input("familya kiriting:  ")
otasini_ismi = input("otasini ismini kiriting:  ")

if 'A' in ismmi:
    print("\nKechirasiz sizni ismingizda a harifi bor bolgani uchun sizga pasport berilmaydi ")
else:
    print("\nSizni ismingizda a harifi yoq ekan sizga pasport beramiz ") 