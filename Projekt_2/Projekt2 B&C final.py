import random
from time import time as tt
from time import sleep as sleep

def dupe(seq):
    """
    Kontroluje, zda se v sekvenci nenachází duplicitní znak
    :param seq:
    :return:
    """
    for p in seq:
      pocet = seq.count(p)
      if pocet > 1:
        return True
#trochu zbytečnost
def cislo(text):
    if text.isdigit() != True:
        return True
#nastavení a statistiky
sep = 50 * "-"
stats = {"Hry": 0, "Průměr pokusů": 0, "Pokusy celkově": 0, "Nejrychlejší": ""}
settings = {"dif_delka": 4, "dif_pokusy": 100, "pokusy_kolo": 0, "menu_volba": 0, "chall": False, }
menu_stats = list()
#menu
while settings.get("menu_volba") != 1:
    print(f"""{sep}\n---------- Vítejte ve hře Bulls & Cows -----------\n{sep}\nAktuální obtížnost: Délka čísla: {settings.get("dif_delka")} Pokusy: {settings.get("dif_pokusy")}\n{sep}\n\t1. Hrát\n\t2. Nastavení obtížnosti\n\t3. Pravidla\n\t4. Statistiky\n\t5. Konec\n{sep}""")
    settings["menu_volba"] = input("Zvolte číselnou volbu z menu: ")
    volba = settings.get("menu_volba")
    while cislo(volba) == True or int(volba) > 5 or int(volba) <= 0:
        settings["menu_volba"] = input("Zvolte číselnou volbu z menu: ")
        volba = settings.get("menu_volba")
    if int(settings.get("menu_volba")) == 5:
        print(f"{sep}\n--------------- Aplikace ukončena ----------------\n{sep}\n{stats}")
        for tisk in menu_stats:
            print(tisk)
        break
    while int(settings.get("menu_volba")) == 2:
        settings["dif_delka"] = "wait"
        while cislo(settings.get("dif_delka")) == True or int(settings.get("dif_delka")) < 4 or int(settings.get("dif_delka")) > 6:
            settings["dif_delka"] = input("Zvolte obtiznost delky cisla 4 - 6: ")
        settings["dif_pokusy"] = "wait"
        while cislo(settings.get("dif_pokusy")) == True or int(settings.get("dif_pokusy")) <= 0:
            settings["dif_pokusy"] = input("Zvolte limit pokusu: ")
        break
    if int(settings.get("menu_volba")) == 3:
        print(f"{sep}\nNávrat za 15 sekund, případně rolujte nahoru")
        print(f"{sep}\nPodle obtížnosti je vygenerováno číslo o délce 4 - 6 číslic\nČísla se nemohou opakovat a první nikdy nemůže být 0\nTipujete číslo:\nPokud trefíte umístění a číslo, dostanete počet bulls\nPokud trefíte pouze číslo, dostanete počet cows")
        sleep(15)
    if int(settings.get("menu_volba")) == 4:
        print(stats)
        for tisk in menu_stats:
            print(tisk)
        print("Návrat do menu za 10 sekund")
        sleep(10)
        settings["menu_volba"] = 0
    while int(settings.get("menu_volba")) == 1:
        idif = int(settings.get("dif_delka"))
        idif1 = int(settings.get("dif_pokusy"))
#generátor čísla
        n = range(0, 10)
        while n[0] == 0:
            n = list(random.sample(n, k=idif))
#tělo hry
        print(f"{sep}\nVygeneroval jsem číslo o délce {idif}, příjemnou zábavu\nZbývá pokusů {idif1}\nPro ukončení kdykoli napiš exit\n{sep}")
        t_start = tt() #timer
        pokus = True
        while pokus:
            nguess = input(f"Tipněte si číslo o délce {idif}: ")
            if nguess == "exit":
                print("Kolo ukončeno")
                settings["pokusy_kolo"] = 0
                pokus = False
                break
            else:
                while len(nguess) != idif or nguess.isdigit() != True or nguess[0] == "0" or dupe(nguess) == True:
                    print(f"Chybný vstup, zadej číslo o délce {idif}")
                    nguess = input(f"Tipněte si číslo o délce {idif}: ")
            bull, poradi, cow = 0, 0, 0
            settings["pokusy_kolo"] += 1
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
            zbyva = idif1 - settings.get('pokusy_kolo')
            print(f"{rescow} : {cow} || {resbull} : {bull} || Zbývá pokusů {zbyva} || Aktuální čas: {str(tt() - t_start)[0:5]} sekund")
#vyhodnocení úspěšnosti a tvorba statistiky
            if bull == idif or zbyva == 0:
                t_stop = tt()
                t_final = t_stop - t_start
                t_str_final = str(t_final)[0:5]
                stats["Pokusy celkově"] = stats.get("Pokusy celkově") + settings.get("pokusy_kolo")
                stats["Hry"] = stats.get("Hry") + 1
                stats["Průměr pokusů"] = (stats.get("Pokusy celkově") / stats.get("Hry"))
                if bull == idif:
                    menu_stats.append(f"Hra {stats.get('Hry')}: Pokusy: {settings.get('pokusy_kolo')} Čas: {t_str_final}")
                    if stats.get("Nejrychlejší") == "" or t_final < float(stats.get("Nejrychlejší")):
                        stats["Nejrychlejší"] = t_str_final
                    print(f"{sep}\nVyhrál jsi! Číslo je opravdu {nguess}\nPočet pokusů: {settings.get('pokusy_kolo')}\nČas: {t_str_final} sekund\nStatistiky: {stats}\n{sep}")
                    settings["pokusy_kolo"] = 0
                    pokus = False
                elif zbyva == 0:
                    menu_stats.append(f"Hra {stats.get('Hry')}: Pokusy: {settings.get('pokusy_kolo')} PROHRA")
                    print(f"\nProhrál jsi, číslo bylo {n}")
                    settings["pokusy_kolo"] = 0
                    pokus = False
#dotaz na restart hry či návrat do menu
        while "ano" not in str(settings.get("menu_volba")) or "ne" not in str(settings.get("menu_volba")) or str(settings.get("menu_volba").isdigit()) == True or str(settings.get("menu_volba").isalnum()) == True:
            settings["menu_volba"] = input("""Chcete hrát znovu?\nANO - NE: """).lower()
            if "ano" in settings.get("menu_volba"):
                settings["menu_volba"] = 1
                break
            elif "ne" in settings.get("menu_volba"):
                settings["menu_volba"] = 0
                break





