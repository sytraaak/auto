texts = ['''
Situated about 10 miles west of Kemmerer, aaaaaaaaaaaaaaaaaaaaa 
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',
"""Situated about 10 miles west of Kemmerer, aaaaaaaaaaaaaaaaaaaaa 
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.""",
'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
#fix
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
predel = "*" * int((len(texts[1]) / (len(texts[2]) / 2) * (len(uzivatele) * 8)))
delka = str(len(texts))
#registrace
registrace = input("""Chcete regitrovat nového uživatele?
Vložte ANO nebo NE: """).lower()
while "a" in registrace:
    jmeno_registrace = input("Vložte nové uživatelské jméno: ")
    if jmeno_registrace not in uzivatele.keys():
        heslo_registrace = input("Vložte heslo: ")
        uzivatele[jmeno_registrace] = str(heslo_registrace)
        registrace = input("""Chcete registrovat dalšího uživatele?:
        Vložte ANO nebo NE: """).lower()
    else:
        print("Uživatelské heslo již existuje")
# login
jmeno = input("Vložte uživatelské jméno: ")
if jmeno not in uzivatele.keys():
    print("Neplatné uživatelské jméno, aplikace ukončena")
else:
    heslo = input("Vložte heslo: ")
    if uzivatele.get(jmeno) != heslo:
        print("Chybné heslo, aplikace ukončena")
    else:
        print(predel)
        print("Byli jste úspěšně přihlášeni")
        print(predel)
        print("Vítejte v aplikaci analýzy textu, " + jmeno)
        print("Můžete si vybrat analýzu " + delka + " textů")
        # volba textu
        volba = input("Zadejte číslo od 1 do " + delka + ": ")
        if volba.isalpha() or volba.isalnum() or volba == "" or int(volba) > int(delka) or int(volba) <= 0:
            print("Zadali jeste chybné číslo, aplikace ukončena")
        else:
            zvoleny = texts[(int(volba) - 1)]
            print("Vámi zvolený text: " + volba)
            print(predel)
# analýza textu
            rozdelena = zvoleny.split()
            cista = []
            for slovo in rozdelena:
                cista.append(slovo.strip(".,!"))
            velka = []
            velke = []
            mala = []
            cisla = []
            for slova in cista:
                if slova.islower():
                    mala.append(slova)
                if slova.isupper() and slova.isalpha():
                    velka.append(slova)
                if slova.isdigit():
                    cisla.append(int(slova))
                if slova.istitle():
                    velke.append(velke)
#spocitani podle delky
            podle_delky = dict()
            for slovo in cista:
                for rozmezi in range(30):
                    if len(slovo) == rozmezi:
                        podle_delky[str(rozmezi)] = podle_delky.setdefault(str(rozmezi), 0) + 1
#výpis rozdělení
            print("Počet slov v textu je: " + str(len(rozdelena)))
            print("Počet slov s velkým prvním písmenem: " + str((len(velke))))
            print("Počet slov psaných malým písmem: " + str((len(mala))))
            print("Počet slov psaných velkým písmem: " + str((len(velka))))
            print("Počet čísel: " + str((len(cisla))))
            print("Součet všech čísel: " + str(sum(cisla)))
            print(predel)
#klice na cisla
            klice = list(podle_delky.keys())
            for i in range(0, len(klice)):
                klice[i] = int(klice[i])
            klice.sort(reverse=True)
#tabulka
            vyskyt = "             Výskyt              "
            print("Délka|" + vyskyt + "|Počet")
            print(predel)
            for cislovani in range(1,(klice[0] + 1)):
                mezirka = int((4 - len(str(cislovani)))) * " "
                if cislovani in klice:
                    print(cislovani, mezirka + "|",podle_delky.get(str(cislovani)) * "*" ,((len(vyskyt) - 3) - podle_delky.get(str(cislovani))) * " " + " |", podle_delky.get(str(cislovani)))

