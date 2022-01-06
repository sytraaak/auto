import random
from time import time as tt

def dupe(seq):
    for p in seq:
      pocet = seq.count(p)
      if pocet > 1:
        return True

sep = 50 * "-"
print(sep+"\nVítejte ve hře Bulls & Cows\n"+sep)
stats = {"hry": 0, "prumer": 0, "pokusy": 0, "Nejrychlejší": ""}
hra = "ano"
while hra == "ano":
    pokusy = 0
    obtiznost = input("Chcete si zvolit obtížnost?\nANO - NE: ").lower()
    if "a" in obtiznost:
        dif, dif1 = input("Zvolte delku cisla 4 - 6: "), input("Zvolte limit pokusu: ")
        while dif.isdigit() != True or int(dif) < 4 or int(dif) > 6:
            print("Chybná volba")
            dif = input("Zvolte obtiznost delky cisla 4 - 6: ")
        while dif1.isdigit() != True or int(dif1) <= 0:
            print("Chybná volba")
            dif1 = input("Zvolte limit pokusu: ")
        idif = int(dif)
        idif1 = int(dif1)
    else:
        idif = 4
        idif1 = 100
    #generátor čísla
    n = range(0, 10)
    while n[0] == 0:
        n = list(random.sample(n, k=idif))
    print(n) #todo tohle smazat - testovací číslo
    print(f"Vygeneroval jsem číslo o délce {idif}, tak hádej\nZbývá pokusů {idif1}\n{sep}")
    t_start = tt()
    while hra == "ano":
        nguess = input(f"Tipněte si číslo o délce {idif}: ")
        while len(nguess) != idif or nguess.isdigit() != True or nguess[0] == "0" or dupe(nguess) == True:
            print(f"Chybný vstup, zadej číslo o délce {idif}")
            nguess = input(f"Tipněte si číslo o délce {idif}: ")
        bull, poradi, cow = 0, 0, 0
        pokusy += 1
        idif1 -= 1
        for n1 in nguess:
            for cykl in range(idif):
                if int(n1) == n[poradi]:
                    poradi += 1
                    bull += 1
                    break
                elif int(n1) in n:
                    poradi += 1
                    cow += 1
                    break
                else:
                    poradi += 1
                    break
        rescow, resbull = "cows", "bulls"
        if cow == 1:
            rescow = "cow"
        if bull == 1:
            resbull = "bull"
        print(f"{rescow} : {cow} || {resbull} : {bull} || Zbývá pokusů {idif1}")
        if bull == idif:
            t_stop = tt()
            t_final = t_stop - t_start
            stats["pokusy"] = stats.get("pokusy") + pokusy
            stats["hry"] = stats.get("hry") + 1
            stats["prumer"] = (stats.get("pokusy") / stats.get("hry"))
            if stats.get("Nejrychlejší") == "" or t_final < float(stats.get("Nejrychlejší")):
                stats["Nejrychlejší"] = str(t_final)[0:5]
            print(f"{sep}\nVyhrál jsi! Číslo je opravdu {nguess}\nPočet pokusů: {pokusy}\nČas: {str(t_final)[0:5]} sekund\nStatistiky: {stats}\n{sep}")
            break
        if idif1 == 0:
            print(f"Prohrál jsi, číslo bylo {n}")
            break
    hra = input("""Chcete hrát znovu?\nANO - NE: """).lower()
    if "a" not in hra:
        print("Díky za hru, aplikace ukončena")


















