def convertor_valutar():
    cursuri = {
        "EUR": 0.20,
        "USD": 0.22,
        "GBP": 0.17
    }

    while True:
        try:
            valoare_ron = float(input("Introduceti suma RON: "))
            if valoare_ron < 0:
                print("eroare\n")
                continue

            moneda = input("Alege moneda (EUR, USD, GBP) sau 'q' pentru iesire: ").strip().upper()
            if moneda == "Q":
                print("La revedere!")
                break

            if moneda in cursuri:
                rata = cursuri[moneda]
                rezultat = valoare_ron * rata
                print(f"Rezultat: {valoare_ron:.2f} RON = {rezultat:.2f}{moneda}")
            else:
                print("Moneda invalida!\n")
                continue
        except ValueError:
            print("Eroare: introduceti o suma valida")

convertor_valutar()