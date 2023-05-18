from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-prijs*korting:.2f} euro"
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {btw_bedrag} btw betaald moet worden"
    return uitvoer

inkomsten = [1000, 1500, 800, 1200, 900, 1100, 1300]
btw_percentage = 0.21
totaal_inkomsten = inkomsten_totaal(inkomsten, btw_percentage)
print(totaal_inkomsten)

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer = [laagste, hoogste]
    return uitvoer

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(mijn_lijst)
print(resultaat)

def gemiddelde(mijn_lijst):
    average = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten zijn {average} euro."
    return uitvoer

print(gemiddelde(mijn_lijst))

def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

invoer_lijst = [10,5,3,2,1,2,9]
resultaat = meervoudig(invoer_lijst)
print(resultaat)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer

invoer_lijst_2 = [10,5,3,2,1,2,9]
print(combinatie(invoer_lijst_2))