felmedelande = "Ange tal inte bokstäver"  # Underlättar mycket vid många except ValueError
s = str("-" * 5)  # Design sträng


def skapa_faktura():
    # Välkomsttext
    ram = "*" * 74
    mellanrum = " " * 72
    meddelande = " Välkommen till det här programmet som hanterar ditt företags ekonomi!"
    prompt = " Vänligen skriv in följande uppgifter: "

    # Centrera texten
    centrerad_meddelande = meddelande.center(72)
    centrerad_prompt = prompt.center(72)

    # Skapa design
    print("\n" + ram)
    print(f"*{mellanrum}*")
    print(f"*{centrerad_meddelande}*")
    print(f"*{mellanrum}*")
    print(f"*{mellanrum}*")
    print(f"*{centrerad_prompt}*")
    print(ram + "\n")

    # Steg 1: Skapa en faktura
    namn_företag = "Wi-Fixar't"

    # Villkor för arbetstimmar
    while True:
        try:
            arbets_timmar = float(input("Ange antalet arbetade timmar: "))
            break
        except ValueError:
            print(felmedelande)

    # Villkor för timpris
    while True:
        try:
            tim_pris = float(input("Ange företagets timpris (exklusive moms): "))
            break
        except ValueError:
            print(felmedelande)

    # Beräkningar till fakturan
    total_exklusive_moms = tim_pris * arbets_timmar
    moms = total_exklusive_moms * 0.25
    tot_faktura_belopp = total_exklusive_moms + moms

    # Fakturans design
    print(f"\n {s} Faktura {s} ")
    print(f"Företagsnamn: {namn_företag}")
    print(f"Arbetade timmar: {arbets_timmar:.2f}")
    print(f"Timpriset är {tim_pris:.2f} kr")
    print(f"Totalt pris exklusive moms: {total_exklusive_moms:.2f} kr")
    print(f"Den totala kostnaden för fakturan: {tot_faktura_belopp:.2f} kr")

    return total_exklusive_moms


def beräkna_företagets_kostnander():
    while True:
        try:
            brutto = float(input("\nAnge din önskade bruttolön: "))
            break
        except ValueError:
            print(felmedelande)

    # Kalkyl för företagets kostnader
    arbets_avgift = brutto * 0.3142
    tjanstepension = brutto * 0.045
    semester = brutto * 0.12
    total_foretagskostnad = arbets_avgift + tjanstepension + semester
    tot_lone_kostnad = brutto + total_foretagskostnad

    # Design av företagets kostnader
    print(f"\n{s} Företagets Kostnader {s}")
    print(f"Bruttolönen är: {brutto:.2f} kr")
    print(f"arbetsgivaravgiften är: {arbets_avgift:.2f} kr")
    print(f"Tjänstepension är: {tjanstepension:.2f} kr")
    print(f"Semesterersättningen är: {semester:.2f} kr")
    print(f"Den totala lönekostnaden är: {tot_lone_kostnad:.2f} kr")

    return brutto, tot_lone_kostnad


def beräkna_nettolön(brutto_utan_print, skatteprocent):
    # Får information gällande skatt från skattetabellen
    while True:
        try:
            arbets_timmar = float(input("Ange antalet arbetade timmar: "))
            break
        except ValueError:
            print(felmedelande)

    skatt = brutto_utan_print * (skatteprocent / 100)
    nettolon = brutto_utan_print - skatt

    semesterdagar = brutto_utan_print * 0.12 / (
        (brutto_utan_print / arbets_timmar) * 8
    )

    print(f"\n {s} Nettolön {s}")
    print(f"Nettolönen är: {nettolon:.2f} kr")
    print(f"Den betalade skatten är: {skatt:.2f} kr")
    print(f"Intjänade semesterdagar: {semesterdagar} dagar")


def kvar_i_bolaget(total_exklusive_moms_v2, tot_lone_kostnad_v2):
    kvar_i_bolaget = float(tot_lone_kostnad_v2 - total_exklusive_moms_v2)
    print(f"Summan som finns kvar i bolaget är: {kvar_i_bolaget:.2f} kr")


def brutto_utan_print():
    while True:
        try:
            brutto_utan_print = float(input("\nAnge din önskade bruttolön: "))
            break
        except ValueError:
            print(felmedelande)

    return brutto_utan_print


def tot_lone_kostnad(brutto_utan_print):
    arbets_avgift_v2 = brutto_utan_print * 0.3142
    tjanstepension_v2 = brutto_utan_print * 0.045
    semester_v2 = brutto_utan_print * 0.12

    total_foretagskostnad_v2 = (
        arbets_avgift_v2 + tjanstepension_v2 + semester_v2
    )
    tot_lone_kostnad_v2 = brutto_utan_print + total_foretagskostnad_v2

    return float(tot_lone_kostnad_v2)


def totalexklusive_moms():
    while True:
        try:
            arbets_timmar_v2 = float(input("Ange antalet arbetade timmar: "))
            tim_pris_v2 = float(input("Ange företagets timpris: "))
            total_exklusive_moms_v2 = tim_pris_v2 * arbets_timmar_v2
            return total_exklusive_moms_v2
        except ValueError:
            print(felmedelande)
