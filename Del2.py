import csv
import Del1 as a  # Detta underlättar eftersom man ej behöver importera in varje funktion för sig
import matplotlib.pyplot as plt


# Lista över alla församlingar i kommunen
def lista(kommun):
    församlingar = []  # placerar alla församlingar i just den kommunen i denna lista

    with open('skattetabell.csv', mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')

        # Kollar om kommunen är hittad och lägger till församlingar
        for row in reader:
            kommun_namn = row['Kommun']
            if kommun_namn == kommun:
                församlingar.append(row['Församling'])

    # Skriver ut församlingar
    if församlingar:
        print(f"Församlingar i {kommun}:")
        for församling in församlingar:
            print(f"=> {församling}")
    else:
        print(f"Inga församlingar hittades för kommunen {kommun}.")


# Skatter
def kommun():
    kommun = input("Ange din kommun: ").upper().strip()
    lista(kommun)

    församling = input("Ange din församling: ").upper().strip()

    with open('skattetabell.csv', mode='r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=';')

        # Startvärden
        skatteprocent = 0
        kommunal_skatt = 0
        begravnings_avgift = 0
        kyrkoavgift = 0

        # Hämtar skatteinformation
        for row in reader:
            if (
                row['Kommun'].strip() == kommun
                and row['Församling'].strip() == församling
            ):
                kommunal_skatt = float(row['Kommunal-skatt'])
                begravnings_avgift = float(row['Begravnings-avgift'])
                kyrkoavgift = float(row['Kyrkoavgift'])
                skatteprocent = float(row["Summa, inkl. kyrkoavgift"])
                break

    print(f"\nSkattesatser för {kommun} - {församling}:")
    print(f"Kommunalskatt: {kommunal_skatt:.2f}%")
    print(f"Begravningsavgift: {begravnings_avgift:.2f}%")
    print(f"Kyrkoavgift: {kyrkoavgift:.2f}%")
    print(f"Totalt skatteprocent: {skatteprocent:.2f}%")

    return skatteprocent


# Prognos och diagram
def prognos():
    arbetstimmar_per_månad = []
    månader = []

    with open('Arbetstimmar.csv', mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row['Månad'] != 'Total årsarbetstid':
                månader.append(row['Månad'])
                arbetstimmar_per_månad.append(float(row['Arbetstimmar']))

    total_arsinkomst_100 = 0
    total_arsinkomst_80 = 0

    resultat_lista = []
    fakturerat_100 = []
    fakturerat_80 = []

    tim_pris = float(input("Ange timpris för alla månader: "))

    for i, timmar in enumerate(arbetstimmar_per_månad):
        if i >= 12:
            break

        inkomst_100 = timmar * tim_pris
        inkomst_80 = inkomst_100 * 0.8

        fakturerat_100.append(inkomst_100)
        fakturerat_80.append(inkomst_80)

        total_arsinkomst_100 += inkomst_100
        total_arsinkomst_80 += inkomst_80

        semesterdagar_per_manad = (12 / 100) * (inkomst_100 / tim_pris) / 8

        resultat_lista.append(
            (månader[i], inkomst_100, inkomst_80, semesterdagar_per_manad)
        )

    print("\nMånad | Inkomst vid 100% | Inkomst vid 80% | Intjänade semesterdagar")
    for rad in resultat_lista:
        print(
            f"{rad[0]:<10} | {rad[1]:.2f} kr | {rad[2]:.2f} kr | {rad[3]:.2f} dagar"
        )

    print(f"\nTotal årsinkomst vid 100% beläggning: {total_arsinkomst_100:.2f} kr")
    print(f"Total årsinkomst vid 80% beläggning: {total_arsinkomst_80:.2f} kr")

    plt.figure(figsize=(11, 6))
    plt.bar(månader[:12], fakturerat_100, label='Fakturerat 100%')
    plt.plot(
        månader[:12],
        fakturerat_80,
        linestyle='dashed',
        color='green',
        label='80% nivå'
    )
    plt.xlabel("Månad")
    plt.ylabel("Fakturerat belopp per månad (kr)")
    plt.title("Prognos för 2025")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


# Meny
def meny():
    skatteprocent = kommun()

    while True:
        print("\n-----Meny-----")
        print("1. Skapa faktura")
        print("2. Beräkna företagets kostnader")
        print("3. Beräkna nettolön")
        print("4. Beräkna kvarvarande pengar i bolaget")
        print("5. Skriv ut prognos, tabell och diagram")
        print("6. Avsluta programmet")

        val = input("Välj ett nummer du vill köra: ").strip()

        if val == "1":
            a.skapa_faktura()

        elif val == "2":
            a.beräkna_företagets_kostnander()

        elif val == "3":
            brutto_utan_print = a.brutto_utan_print()
            a.beräkna_nettolön(brutto_utan_print, skatteprocent)

        elif val == "4":
            total_exklusive_moms_v2 = a.totalexklusive_moms()
            brutto_utan_print = a.brutto_utan_print()
            tot_lone_kostnad_v2 = a.tot_lone_kostnad(brutto_utan_print)
            a.kvar_i_bolaget(tot_lone_kostnad_v2, total_exklusive_moms_v2)

        elif val == "5":
            prognos()

        elif val == "6":
            break

        else:
            print("Vänligen välj en siffra mellan 1-6 tack :)")


meny()
