# Python-ohjelmoinnin perusteet-kurssin harjoitustyö.
# 2.12.2022 Kaisu Pietarinen.

# Ohjelma kysyy käyttäjältä verensokerin, jonka jälkeen käyttäjä saa tiedon onko verensokeri normaali,
# matala vai korkea ja kuinka käyttäjän tulee toimia. Mikäli verensokeri on liian korkea, ohjelma pyytää
# käyttäjää mittaamaan myös ketoaineet ja ilmoittaa miten käyttäjän tulee toimia.

# HUOM! Hiilihydraatti- sekä insuliinimäärät ovat suuntaa antavia ja todellisuudessa 
# diabeetikko itse tietää verensokerien korjaukseen tarvittavan hiilihydraattimäärän, ja 
# hoitotaho on ohjeistanut insuliiniannostukset. 
# Ohjelma on suuntaa antava, eikä ole tarkoitettu hoidolliseen tarkoitukseen!
# Oletuksena harjoitustyössä on, että diabeetikon hoitomuoto on monipistoshoito.



import csv
from datetime import datetime
import os

# Funktio pyytää käyttäjältä henkilötunnuksen, jonka tulee sisältää 11 merkkiä. 
# Merkit saavat olla kirjaimia, numeroita tai väliviivoja.
# Funktio palauttaa käyttäjän syöttämän henkilötunnuksen.
def hetu():
    pituus = 11
    try: 
        hloTunnus = input("Syötä henkilötunnus: ")
        while not hloTunnus.replace("-","").isalnum():
            print("Käytä vain kirjaimia, numeroita tai väliviivaa!")
            hloTunnus = input("Syötä henkilötunnus: ")
        while not len(hloTunnus) == pituus:
            print("Henkilötunnuksen tulee sisältää 11 merkkiä.")
            hloTunnus = input("Syötä henkilötunnus: ")
        return hloTunnus
    except:
        print("Tapahtui virhe henkilötunnusta syöttäessä.")

# Funktio pyytää käyttäjältä nimen, joka saa sisältää vain kirjaimia ja väliviivan 
# ja muuntaa etu- ja sukunimen ensimmäiset kirjaimet isoiksi kirjaimiksi.
# Funktio palauttaa käyttäjän syöttämän etu- ja sukunimen.
def nimi():
    try:
        etuNimi = input("Syötä etunimesi: ")
        while not etuNimi.replace("-","").isalpha():
            print("Käytä vain kirjaimia!")
            etuNimi = input("Syötä etunimesi: ")

        sukuNimi = input("Syötä sukunimesi: ")
        while not sukuNimi.replace("-","").isalpha():
            print("Käytä vain kirjaimia!")
            sukuNimi = input("Syötä sukunimesi: ")

        etunimiCap = etuNimi.title()
        sukunimiCap = sukuNimi.title()
        nimi = etunimiCap + " " + sukunimiCap

        return nimi
    except:
        print("Tapahtui virhe nimeä syöttäessä.")

# Funktio pyytää käyttäjää syöttämään ketoainearvon ja ilmoittaa käyttäjälle toimintaohjeet.
# Funktio palauttaa käyttäjän syöttämän ketoainearvon.
def ketoaineet():
    try:
        while True:
            try:
                keto = float(input("Syötä ketoarvosi (mmol/l):").replace(',','.'))
            except ValueError:
                print("Syötä vain kokonais- tai liukulukuja.")
                continue
            else:
                break
    
        print()

        if keto < 0.6:
            print("Ketoaineet ovat lievästi koholla.\n"
                "-> Pistä 1.5 yksikköä pikainsuliinia.\n" 
                "-> Mittaa verensokeri uudestaan 2 h kuluttua.")
        
        if keto >= 0.6 and keto < 1.6:
            print("Ketoaineet ovat hieman koholla.\n" 
                "-> Pistä 1.5-2 yksikköä pikainsuliinia ja juo nestettä.\n"
                "-> Mittaa verensokeri ja ketoaineet uudestaan 2 h kuluttua.")
        
        if keto >= 1.6 and keto < 3.1:
            print("Happomyrkytyksen riski on kasvanut.\n" 
                "-> Pistä 2 yksikköä pikainsuliinia.\n"
                "-> Mittaa verensokeri ja ketoaineet uudestaan 2 h kuluttua.")

        if keto >= 3.1:
            print("Happomyrkytyksen riski on korkea.\n" 
                "-> Hakeudu pikaisesti sairaalahoitoon!")

        print()
        return keto
    except:
        print("Tapahtui virhe ketoarvoa syöttäessä.")  

# Funktio pyytää käyttäjältä verensokeriarvon ja tulostaa käyttäjälle onko verensokeri normaali, matala vai korkea
# ja kuinka käyttäjän tulee toimia. Funktio pyytää käyttäjää myös tarvittaessa mittaamaan ketoaineet.
# Funktio palauttaa käyttäjän syöttämän verensokeriarvon.
def verensokeri():
    try:
        while True:
            try:
                vs = float(input("Syötä verensokeriarvosi (mmol/l): ").replace(',','.'))
            except ValueError:
                print("Syötä vain kokonais- tai liukulukuja.")
                continue
            else:
                break
        
        print()

        if vs < 2.0:
            print("Verensokerisi on hälyttävän matala!\n" 
                "-> Ota 20-30g hiilihydraattia (n. 2-3 dl mehua).\n"
                "-> Huolehdi, että joku on kanssasi siltä varalta, "
                "että menetät tajunnan.\n"
                "-> Mittaa verensokeri uudestaan 15 min. kuluttua.")

        if vs >= 2.0 and vs < 3.1:
            print("Verensokerisi on erittäin matala.\n" 
                "-> Ota 10-20g hiilihydraattia (noin 1-2 dl mehua).\n"
                "-> Mittaa verensokeri uudestaan 15 min. kuluttua.")

        if vs >= 3.1 and vs < 4.1:
            print("Verensokerisi on matala.\n" 
                "-> Ota 5-10g hiilihydraattia (noin 0.5-1 dl mehua).\n"
                "-> Mittaa verensokeri uudestaan 15 min. kuluttua.")

        if vs >= 4.1 and vs < 10.0:
            print("Verensokerisi on normaali.")

        if vs >= 10.0 and vs < 14.1:
            print("Verensokerisi on vähän korkea.\n" 
                "-> Pistä 0.5 yksikköä pikainsuliinia.\n"
                "-> Mittaa verensokeri uudestaan 2 h kuluttua")

        if vs >= 14.1 and vs < 17.1:
            print("Verensokerisi on korkea.\n" 
                "-> Pistä 1 yksikköä pikainsuliinia.\n"
                "-> Mittaa verensokeri uudestaan 2 h kuluttua")

        if vs >= 17.1 and vs < 20.0:
            print("Verensokerisi on hyvin korkea.\n" 
                "-> Mittaa ketoaineet!")

        if vs >= 20.0:
            print("Verensokerisi on todella korkea.\n" 
                "-> Mittaa ketoaineet!")
        
        print()
        return vs
    except:
        print("Tapahtui virhe verensokeria syöttäessä.")

# Funktio hetu-, nimi- ketoaineet-, ja verensokeri-funktioiden kutsumiseen ja 
# käyttäjän syöttämien sekä pvm ja aika tietojen kirjoittamiseen CSV-tiedostoon, 
# joka sisältää ennestään otsikot ja aiempien käyttäjien syöttämiä tietoja.
def kirjoitaCsv():
    pvmAika = datetime.now()
    kirjausPvm = pvmAika.strftime("%d.%m.%Y")
    kirjausAika = pvmAika.strftime("%H:%M")
    henkiloTunnus = hetu()
    henkilonNimi = nimi()
    henkilonVs = verensokeri()
    if henkilonVs >= 17.1:
        henkilonKeto = ketoaineet()
    else: henkilonKeto = 0.0

    otsikko = ['Pvm', 'Klo', 'Henkilötunnus','Nimi', 'Verensokeri', 'Ketoaineet']
    data = [kirjausPvm, kirjausAika, henkiloTunnus, henkilonNimi, henkilonVs, henkilonKeto]

    fileExists = os.path.isfile('Harjoitustyo.csv')

    with open('Harjoitustyo.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        if not fileExists:
            writer.writerow(otsikko)
        writer.writerow(data)
        f.close()


# Funktio harjtyo.csv-tiedoston lukemiseksi ja tulostamiseksi
def lueCsv():
    print("--------------------------------\n")
    print("'Harjoitustyo.csv'-tiedoston sisältö:\n")

    with open('Harjoitustyo.csv', encoding="utf8") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        for row in data:
            print('{:<12} {:<8} {:<15} {:<27} {:<12} {:<12}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

# Kutsutaan kirjoitaCsv- ja lueCsv-funktiota
kirjoitaCsv()
lueCsv()