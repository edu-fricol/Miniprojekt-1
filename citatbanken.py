"""
Projekt 1: Personlig citatbank
Ett menybaserat program för att hantera citat med filhantering.
"""
import random

def ladda_citat_fran_fil(filnamn):
    try:
        with open(filnamn, "r") as fil:        
              citatlista = fil.readlines()
        return citatlista
    except FileNotFoundError:
        return []

def spara_citat_till_fil(citatlista, filnamn):

    with open(filnamn, "w") as fil:
        for citat in citatlista:
            fil.write(citat + "\n")


def visa_alla_citat(citatlista):
    if not citatlista:
        print("Inget citat finns.")
        return

    print("\n--- Alla Citat ---")
    for index, citat in enumerate(citatlista, start=1):
        print(f"{index}. {citat}")
        print("-------------------\n")

def lagg_till_citat(citatlista):
 
    while True:
        citat = input("Ange citatet: ").strip()
        forfattare = input("Ange författaren: ").strip()


        if citat == "" or forfattare == "":
                print("Citatet och/eller författaren kan inte vara tomma.")
                print("Vänligen försök igen.")
                continue

        nytt_citat = f"{citat} - {forfattare}"
        citatlista.append(nytt_citat)
        print("Citatet har lagts till!")
        return True

def slumpa_citat(citatlista):

    if not citatlista:
        print("Inget citat finns att visa.")
        return

    slumpat_citat = random.choice(citatlista)
    print("\nSlumpmässigt Citat:")
    print(slumpat_citat.strip())
    print()

def huvudprogram():

    filnamn = "citat.txt"
    citatlista = ladda_citat_fran_fil(filnamn)
   
    while True:
        print("1. Visa alla citat")
        print("2. Lägg till ett nytt citat")
        print("3. Slumpa citat")
        print("4. Avsluta")

        val = input("Välj ett alternativ (1-4): ").strip()

        if val == "1":
            visa_alla_citat(citatlista)
        elif val == "2":
            if lagg_till_citat(citatlista):
                spara_citat_till_fil(citatlista, filnamn)
        elif val == "3":
            slumpa_citat(citatlista)
        elif val == "4":
            print("Avslutar programmet. Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    huvudprogram()