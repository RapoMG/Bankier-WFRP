# Rozmienianie nominału
def rozmien(w_nom, m_nom, nom):
    # Większy nominał (rozmieniany), mniejszy nominał (docelowy), nom ('ss' lub 'bp') definiuje przelicznik
    if nom == 'ss':
        przel = 20
    elif nom == 'bp':
        przel = 12
    else:
        przel = -9999  # Wyraźne wskazanie błędu w przeliczaniu

    if w_nom > 0:
        w_nom -= 1
        m_nom += przel

    return w_nom, m_nom


# Zamienianie nominału
'''def zamien(w_nom, m_nom, nom):
    # Większy nominał (docelowy), mniejszy nominał (zamieniany), nom ('ss' lub 'bp') definiuje przelicznik
    if nom == 'ss':
        przel = 20
    elif nom == 'bp':
        przel = 12
    else:
        przel = -9999  # Wyraźne wskazanie błędu w przeliczaniu

    if m_nom >= przel:
        m_nom -= przel
        w_nom += 1
    return w_nom, m_nom
'''
def zamien(ile, w_nom, m_nom, nom):

    if nom == 'ss':
        przel = 20
    elif nom == 'bp':
        przel = 12
    else:
        przel = -9999  # Wyraźne wskazanie błędu w przeliczaniu

    while ile > (m_nom/przel):
        czysc()
        #tabela('jeden', pocz_zk, pocz_ss, pocz_bp)
        tabela('brak')
        zadania()
        print(' Przy tej liczbie monet można uzyskać tylko', (m_nom//przel), 'z', ile, 'oczekiwanych.')
        try:
            malo = str(input(' Zamienić mimo tego? [T/N]\n '))
        except ValueError:
            continue
        if malo == 'N' or malo == 'n':
            return w_nom, m_nom
        elif malo == 'T' or malo == 't':
            break
        else:
            continue
        print('pętla')
    print('drugi etap')
    while ile > 0:
        print('ile:',ile)
        if m_nom >= przel:
            m_nom -= przel
            w_nom += 1
            ile -= 1
        else:
            ile = 0
    print('koniec')
    return w_nom, m_nom

##########################
# Funkcje zadań głównych #
##########################

# Zadanie określenia zasobów


def zasoby():
    def_zk = def_ss = def_bp = 0
    linie = ''
    ktory_nominal = ['Koron', 'Szylingów', 'Pensów']
    koment = ['', ' Liczbowo poproszę!', ' Z długiem przychodzisz? Kredyty są piętro wyżej!',
              ' Nie ma tylu monet w całym Altdorfie! ']
    k = przebieg = 0  # k - operator komentarza
    while True:
        try:
            czysc()
            tabela(linie, def_zk, def_ss, def_bp, 'Będzie')
            zadania()
            print(koment[k])
            wartosc = int(input(' Ile ' + ktory_nominal[przebieg] + '?\n '))  # Ile masz koron?
            k = 0
        except ValueError:
            k = 1
            continue
        if wartosc > 10000:  # ogranicznik ilości monet
            k = 3
            continue
        if wartosc >= 0 and przebieg == 0:
            def_zk = wartosc
            linie = 'deklarowanie'
        elif wartosc >= 0 and przebieg == 1:
            def_ss = wartosc
        elif wartosc >= 0 and przebieg == 2:
            def_bp = wartosc
            break
        else:
            k = 2
            continue
        przebieg += 1
    return def_zk, def_ss, def_bp


# Zadanie zwiększenia zasobów
def dodaj(dod_zk, dod_ss, dod_bp):
    linie = 'jeden'
    tresc = 'Dodane'
    sum_zk = sum_ss = sum_bp = 0
    koment = ['', ' Liczbowo poproszę!', ' Z długiem przychodzisz? Kredyty są piętro wyżej!',
              ' Nie byłoby tylu monet w całym Altdorfie! ']
    k = 0
    while True:
        czysc()
        tabela(linie, sum_zk, sum_ss, sum_bp, tresc, dod_zk, dod_ss, dod_bp)
        opcje(7)
        print(koment[k])
        print(' Jaki nominał dodać?')
        try:
            wybor = int(input(' '))
        except ValueError:
            continue
        if wybor == 1:  # Wybór złota
            czysc()
            tabela(linie, sum_zk, sum_ss, sum_bp, tresc, dod_zk, dod_ss, dod_bp)  # te zmienne to wynik
            zadania()
            try:
                wart = int(input('\n O ile marek powiększamy rachunek? \n '))
            except ValueError:
                k = 1
                continue
            if (wart + dod_zk) > 10000:  # ogranicznik ilości monet
                k = 3
                wart -= wart
                continue
            linie = 'trzy'
            k = 0
            sum_zk += wart
            wart -= wart
            dod_zk += sum_zk
        elif wybor == 2:  # Wybór srebra
            czysc()
            tabela(linie, sum_zk, sum_ss, sum_bp, tresc, dod_zk, dod_ss, dod_bp)

            zadania()
            try:
                wart = int(input('\n Ile szylingów dodać do sakiewki? \n '))
            except ValueError:
                k = 1
                continue
            if (wart + sum_ss) > 10000:  # ogranicznik ilości monet
                k = 3
                wart -= wart
                continue
            linie = 'trzy'
            k = 0
            sum_ss += wart
            wart -= wart
            dod_ss += sum_ss
        elif wybor == 3:  # Wybór brązu
            czysc()
            tabela(linie, sum_zk, sum_ss, sum_bp, tresc, dod_zk, dod_ss, dod_bp)
            zadania()
            try:
                wart = int(input('\n Fenigi? Ile? \n '))
            except ValueError:
                k = 1
                continue
            if (wart + sum_bp) > 10000:  # ogranicznik ilości monet
                k = 3
                wart -= wart
                continue
            linie = 'trzy'
            k = 0
            sum_bp += wart
            dod_bp += sum_bp
        elif wybor == 0:
            return dod_zk, dod_ss, dod_bp
        else:
            continue


# Zadanie zmniejszania zasobów
def odejmij(od_zk, od_ss, od_bp):
    wyd_zk = wyd_ss = wyd_bp = 0
    wydaj_zk = wydaj_ss = wydaj_bp = False
    linie = 'jeden'
    tresc = 'Odjęte'
    koment = ['', ' Liczbowo poproszę!', ' Cyfry! Nie litery, cyfry!',
              ' Chyba będę pobierać opłatę od złożonego zlecenia...']
    k = przebieg = 0  # k - operator komentarza
    ktory_nominal = ['Koron', 'Szylingów', 'Pensów']

    # Pytanie o wydatki
    while True:
        czysc()
        tabela(linie, wyd_zk, wyd_ss, wyd_bp, tresc, od_zk, od_ss, od_bp)
        zadania()
        print(koment[k])
        try:
            wartosc = int(input(' Ile ' + ktory_nominal[przebieg] + ' chcesz wydać?\n '))
            k = 0
        except ValueError:
            if k == 3:
                k = 0
            else:
                k += 1
            continue
        if wartosc >= 0 and przebieg == 0:
            wyd_zk = wartosc
        elif wartosc >= 0 and przebieg == 1:
            wyd_ss = wartosc
        elif wartosc >= 0 and przebieg == 2:
            wyd_bp = wartosc
            break
        else:
            continue
        przebieg += 1

    # Kontrola czy zasob nie przekroczy wydatków
    zasob = od_zk * 240 + od_ss * 12 + od_bp
    wydatek = wyd_zk * 240 + wyd_ss * 12 + wyd_bp
    if zasob >= wydatek:
        if wyd_zk > 0:
            wydaj_zk = True
        if wyd_ss > 0:
            wydaj_ss = True
        if wyd_bp > 0:
            wydaj_bp = True
    else:
        czysc()
        tabela(linie, wyd_zk, wyd_ss, wyd_bp, tresc, od_zk, od_ss, od_bp)
        zadania()
        print(' Nie stać Cię na ten wydatek.')
        pauza()

    # Wydatki
    while wydaj_zk:
        if od_zk >= wyd_zk:
            od_zk -= wyd_zk
            break
        if od_ss > 0:
            od_zk, od_ss = zamien(od_zk, od_ss, 'ss')
        if od_bp > 0:
            od_ss, od_bp = zamien(od_ss, od_bp, 'bp')

    while wydaj_ss:
        if od_ss >= wyd_ss:
            od_ss -= wyd_ss
            break
        if od_zk > 0:
            od_zk, od_ss = rozmien(od_zk, od_ss, 'ss')
            continue
        elif od_bp > 0:
            od_ss, od_bp = zamien(od_ss, od_bp, 'bp')

    while wydaj_bp:
        if od_bp >= wyd_bp:
            od_bp -= wyd_bp
            break
        if od_ss > 0:
            od_ss, od_bp = rozmien(od_ss, od_bp, 'bp')
        elif od_zk > 0:
            od_zk, od_ss, = rozmien(od_zk, od_ss, 'ss')

    if zasob >= wydatek:
        czysc()
        tabela('trzy', wyd_zk, wyd_ss, wyd_bp, tresc, od_zk, od_ss, od_bp)
        zadania()
        pauza()
    return od_zk, od_ss, od_bp


# Zadanie rozmiany monet
def rozmiana(rozm_zk, rozm_ss, rozm_bp):
    pocz_zk, pocz_ss, pocz_bp = rozm_zk, rozm_ss, rozm_bp
    zle = k = 0
    linie = 'jeden'
    koment = ['', ' Przemyśl, co robisz.',
              ' Niby jak? Nie ma dość monet. Masz tylko ' + str(rozm_zk) + '. Rachujesz niby elf!',
              ' Z czego mam rozmienić? Masz jeno ' + str(rozm_ss) + '. Jesteś jak mewy!',
              ' Popiło się? Bo masz ' + str(rozm_ss) + ', a ' + str(zle) + ' mówisz.']
    while True:
        # Wartości dla opcji wyświetlanych opcji: zk - 1, ss - 2, bp - 4
        opc = 0
        if rozm_zk > 0:
            opc += 1
        if rozm_ss > 0:
            opc += 2

        czysc()
        tabela(linie, pocz_zk, pocz_ss, pocz_bp, 'Było', rozm_zk, rozm_ss, rozm_bp, 'Jest')
        opcje(opc)
        print(koment[k])
        wybor = input(' Co chcesz rozmienić?\n ')
        k = 0

        # Dwa warianty pod 1
        if wybor == '1':
            # Wybór złotych koron
            if opc == 1 or opc == 3:
                try:
                    czysc()
                    tabela(linie, pocz_zk, pocz_ss, pocz_bp, 'Było', rozm_zk, rozm_ss, rozm_bp, 'Jest')
                    zadania()
                    ile = int(input('\n Ile rozmienić?\n '))
                    pocz_zk, pocz_ss, pocz_bp = rozm_zk, rozm_ss, rozm_bp
                except ValueError:
                    k = 1
                    continue
                if ile > rozm_zk:  # Wybór większy od zasobu
                    k = 2
                    continue
                while ile > 0:
                    rozm_zk, rozm_ss = rozmien(rozm_zk, rozm_ss, 'ss')
                    ile -= 1
                    linie = 'oba_zmienne'

            # Wybór szylingów, jeśli tylko one są dostępne
            elif opc == 2:
                try:
                    czysc()
                    tabela(linie, pocz_zk, pocz_ss, rozm_bp, 'Było', rozm_zk, rozm_ss, rozm_bp, 'Jest')
                    zadania()
                    ile = int(input('\n Ile rozmienić?\n '))
                    pocz_zk, pocz_ss, pocz_bp = rozm_zk, rozm_ss, rozm_bp
                except ValueError:
                    k = 1
                    continue
                if ile > rozm_ss:
                    k = 3
                    continue
                while ile > 0:
                    rozm_ss, rozm_bp = rozmien(rozm_ss, rozm_bp, 'bp')
                    ile -= 1
                    linie = 'oba_zmienne'

        # Wybór szylingów, jeśli są dostępne wraz z koronami
        elif wybor == '2' and opc == 3:  # Wybór wyłącznie srebra
            try:
                czysc()
                tabela(linie, pocz_zk, pocz_ss, rozm_bp, 'Było', rozm_zk, rozm_ss, rozm_bp, 'Jest')
                zadania()
                ile = int(input('\n Ile rozmienić?\n '))
                pocz_zk, pocz_ss, pocz_bp = rozm_zk, rozm_ss, rozm_bp
            except ValueError:
                k = 1
                continue
            if ile > rozm_ss:
                k = 4
                zle = ile  # Wartość do komunikatu
                continue
            while ile > 0:
                rozm_ss, rozm_bp = rozmien(rozm_ss, rozm_bp, 'bp')
                ile -= 1
                linie = 'oba_zmienne'
        elif wybor == '0':
            break
        else:
            continue
    return rozm_zk, rozm_ss, rozm_bp


# Zadanie zamiany monet
def zamiana(zam_zk, zam_ss, zam_bp):
    pocz_zk, pocz_ss, pocz_bp = zam_zk, zam_ss, zam_bp
    linie = 'jeden'
    while True:
        # Wartości dla opcji wyświetlanych opcji: zk - 1, ss - 2, bp - 4
        opc = 0
        if zam_ss >= 20:  # Wartości na sztywno, żeby sobie nie utrudniać
            opc += 2
        if zam_bp >= 12:
            opc += 4

        czysc()
        tabela(linie, pocz_zk, pocz_ss, pocz_bp, 'Było', zam_zk, zam_ss, zam_bp, 'Jest')
        opcje(opc)
        wybor = input('\n Co chcesz zamienić?\n ')

        # Dwa warianty pod 1
        if wybor == '1':
            # Wybór szylingów
            if opc == 2 or opc == 6:
                try:
                    czysc()
                    tabela(linie, pocz_zk, pocz_ss, pocz_bp, 'Było', zam_zk, zam_ss, zam_bp, 'Jest')
                    zadania()
                    ile = int(input(' Na ile Koron maksymalnie zamienić?\n '))
                    pocz_zk, pocz_ss, pocz_bp = zam_zk, zam_ss, zam_bp
                except ValueError:
                    continue
                #while ile > 0:
                zam_zk, zam_ss = zamien(ile, zam_zk, zam_ss, 'ss') #wcięcie
                    #ile -= 1
                linie = 'oba_zmienne' #wcięcie
            # Wybór pensów
            elif opc == 4:
                try:
                    czysc()
                    tabela(linie, pocz_zk, pocz_ss, pocz_bp, 'Było', zam_zk, zam_ss, zam_bp, 'Jest')
                    zadania()
                    ile = int(input(' Ile Szylingów chcesz uzyskać?\n '))
                    pocz_zk, pocz_ss, pocz_bp = zam_zk, zam_ss, zam_bp
                except ValueError:
                    continue
                zam_ss, zam_bp = zamien(ile, zam_ss, zam_bp, 'bp')
                linie = 'oba_zmienne'
        elif wybor == '2' and opc == 6:
            try:
                czysc()
                tabela(linie, pocz_zk, pocz_ss, pocz_bp, 'Było', zam_zk, zam_ss, zam_bp, 'Jest')
                zadania()
                ile = int(input(' Ile srebrników chcesz dostać?\n '))
                pocz_zk, pocz_ss, pocz_bp = zam_zk, zam_ss, zam_bp
            except ValueError:
                continue
            zam_ss, zam_bp = zamien(ile, zam_ss, zam_bp, 'bp')
            linie = 'oba_zmienne'
        elif wybor == '0':
            break
        else:
            continue
    return zam_zk, zam_ss, zam_bp


# Zadanie obliczenia odsetka oszczędności
def inwestycja(baz_zk, baz_ss, baz_bp):
    # 1. wyświetla posiadaną kwotę w tabeli
    # a. do wyboru są opcje: okeśl kwotę i odsetki
    # b. po wypełnieniu wyświetli się opcja 3. oblicz
    # c. obliczenie daje dwie kolejne: dodaj zyski i odejmij stratę
    # D. zmiana w A. usuwa C.
    #
    # 2. Określ kwotę prowadzi przez wybór nominałów jak w dodawaniu.
    # A. Deklaracje wyświetlane w 2. rzędzie
    #
    # 3. Odsetki pyta o przedział 1-10, nazwa wiersza 2. wyświetlana jako Zysk 4%
    #
    # 4. Oblicz wyświetli 3. rząd ze spodziewanym zyskiem
    #
    # 5. Dodaj zyski dodaje 3. rząd, bez przeliczania. Wraca do menu gł.
    #
    # 6. Odejmij stratę odejmuje deklarację (2. wiersz) od podstawy. Wraca do menu gł.
    # # # # # # # # # # # # # # # # # # # # # # # # # #

    # wyświetla opcje dla inwestycji
    def opc_inwest():  # kopia z zadań do przebudowy
        zad_a = ' 1. Kwota inwestycji'
        zad_b = ' 2. Określ odsetki'
        zad_c = ''
        zad_d = ''
        koniec = '0. Zakończ'
        if jeden and dwa:
            zad_c = '3. Oblicz zysk'
        if trzy:
            zad_d = '4. Dodaj zyski'

        print(zad_a.ljust(22) + zad_c.ljust(22) + koniec)
        print(zad_b.ljust(22) + zad_d.ljust(22))
        print('\n')
        print(' ' + '─' * 70)  # pokarze zakres "widoku" i "pytania"

    # Zadanie deklarowania zakresu inwestycji
    def kwota_inwest(wyb_zk, wyb_ss, wyb_bp, lini, tresc):
        while True:
            czysc()
            tabela(lini, wyb_zk, wyb_ss, wyb_bp, tresc, ods_zk, ods_ss, ods_bp, 'Zysk')
            opcje(7)
            try:
                wybor_inw = int(input('\n Jaki nominał dodać?\n '))
            except ValueError:
                continue
            if wybor_inw == 1:  # Wybór złota
                czysc()
                lini = 'dwa'
                tabela(lini, wyb_zk, wyb_ss, wyb_bp, tresc)
                zadania()
                wyb_zk = int(input('\n O ile marek powiększamy rachunek? \n '))
            elif wybor_inw == 2:  # Wybór srebra
                czysc()
                lini = 'dwa'
                tabela(lini, wyb_zk, wyb_ss, wyb_bp, tresc)
                zadania()
                wyb_ss = int(input('\n Ile szylingów dodać do inwestycji? \n '))
            elif wybor_inw == 3:  # Wybór brązu
                czysc()
                lini = 'dwa'
                tabela(lini, wyb_zk, wyb_ss, wyb_bp, tresc)
                zadania()
                wyb_bp = int(input('\n Fenigi teź? Ile? \n '))
            elif wybor_inw == 0:
                return wyb_zk, wyb_ss, wyb_bp, lini
            else:
                continue

    inw_zk = inw_ss = inw_bp = ods_zk = ods_ss = ods_bp = proc = 0
    jeden = dwa = trzy = False
    linie = 'jeden'
    procent = ''
    # 1:
    while True:
        czysc()
        tabela(linie, inw_zk, inw_ss, inw_bp, procent, ods_zk, ods_ss, ods_bp, 'Zysk')
        opc_inwest()
        # alternatywne opcje
        try:
            wybor = int(input('\n Czym się zająć?\n '))
        except ValueError:
            continue
        if wybor == 1:
            inw_zk, inw_ss, inw_bp, linie = kwota_inwest(inw_zk, inw_ss, inw_bp, linie, procent)
            jeden = True  # reguluje dostęp do opcji
            trzy = False  # wymusza ponowne użycie przeliczenia
        elif wybor == 2:
            while True:
                czysc()
                tabela(linie, inw_zk, inw_ss, inw_bp, procent, ods_zk, ods_ss, ods_bp, 'Zysk')
                opc_inwest()
                try:
                    proc = int(input('\n Jakiego procenta zysku oczekujesz? Od 1 do 10.\n '))
                    if proc not in range(1, 11):  # Zasięg musi się kończyć o punkt dalej niż oczekiwany koniec
                        raise ValueError
                    procent = str(proc) + ' % z'
                    linie = 'dwa'
                    dwa = True  # reguluje dostęp do opcji
                    trzy = False  # wymusza ponowne użycie przeliczenia
                    break
                except ValueError:
                    continue
        elif wybor == 3 and jeden and dwa:
            zysk = (240 * inw_zk + 12 * inw_ss + inw_bp) * (proc / 100)
            while True:
                if zysk >= 240:
                    zysk -= 240
                    ods_zk += 1
                elif zysk >= 12:
                    zysk -= 12
                    ods_ss += 1
                else:
                    ods_bp = int(round(zysk))
                    linie = 'trzy'
                    trzy = True
                    break
        elif wybor == 4 and trzy:
            baz_zk += ods_zk
            baz_ss += ods_ss
            baz_bp += ods_bp
            '''ods_zk = ods_ss = ods_bp = 0  # Zbędne przy powrocie do menu gł.
            linie = 'deklarowanie'
            jeden = dwa = trzy = False  # przywraca opcje do początku
            continue'''
            return baz_zk, baz_ss, baz_bp  # powrót do menu gł., bo nie aktualizuje głównej wartości monet
        elif wybor == 0:
            return baz_zk, baz_ss, baz_bp
        else:
            continue


# Obliczanie rabatów i wartości sprzedaży
def targowanie():
    def opc_targow():  # kopia z zadań do przebudowy
        zad_1 = ' 1. Wartość bazowa'
        zad_2 = zad_3 = zad_4 = ''
        koniec = '0. Zakończ'
        if cena:
            zad_2 = ' 3. Upust 10%'
            zad_3 = ' 4. Upust 20%'
            zad_4 = ' 2. Oblicz procent'

        print(zad_1.ljust(20) + zad_2.ljust(20) + koniec)
        print(zad_4.ljust(20) + zad_3.ljust(20))
        print('')
        print(' ' + '─' * 70)  # pokarze zakres "widoku" i "pytania"

    def upust(zloto, srebro, braz, procent):
        wynik = (240 * zloto + 12 * srebro + braz) * (procent / 100)
        zloto = srebro = braz = 0
        while True:
            if wynik >= 240:
                wynik -= 240
                zloto += 1
            elif wynik >= 12:
                wynik -= 12
                srebro += 1
            else:
                braz = int(round(wynik))
                return zloto, srebro, braz
    cena = False
    linie = 'pusta'
    rab_zk = rab_ss = rab_bp = cena_zk = cena_ss = cena_bp = 0
    wycena = ''
    # 1:
    while True:
        czysc()
        tabela(linie, cena_zk, cena_ss, cena_bp, 'Wartość', rab_zk, rab_ss, rab_bp, wycena)
        opc_targow()
        # alternatywne opcje
        try:
            wybor = int(input('\n Czym się zająć?\n '))
        except ValueError:
            continue
        if wybor == 1:  # deklaracja ceny wyjściowej
            cena_zk, cena_ss, cena_bp = zasoby()
            cena = True  # reguluje dostęp do opcji
            linie = 'deklarowanie'

        elif wybor == 3 and cena:  # Upust 10%
            rab_zk, rab_ss, rab_bp = upust(cena_zk, cena_ss, cena_bp, 90)
            linie = 'oba_zmienne'
            wycena = 'Upust 10%'  # Opis tabeli
        elif wybor == 4 and cena:  # Upust 20%
            rab_zk, rab_ss, rab_bp = upust(cena_zk, cena_ss, cena_bp, 80)
            linie = 'oba_zmienne'
            wycena = 'Upust 20%'  # Opis tabeli

        elif wybor == 2 and cena:  # wart. procentowa podana przez użytkownika
            while True:
                czysc()
                tabela(linie, cena_zk, cena_ss, cena_bp, 'Wartość', rab_zk, rab_ss, rab_bp, wycena)
                opc_targow()
                try:
                    proc_tekst = input('\n Jaki procent wartości rozpatrzyć? (maks. 5 cyfr)\n ')#
                    proc = float(proc_tekst.replace(",", "."))  # Zamienia , na . na potrzeby py
                    if proc - int(proc) > 0:  # Zaokrągla do 2 miejsc, jeśli jest ułamek
                        proc = round(proc, 2)
                    else:  # Ucina zera dziesiętne jeśli jest całkowita
                        proc = int(proc)
                    if len(str(proc)) > 6:  # Testuje długość
                        raise ValueError
                    wycena = 'Cena ' + str(proc_tekst) + '%'
                    linie = 'oba_zmienne'
                    rab_zk, rab_ss, rab_bp = upust(cena_zk, cena_ss, cena_bp, proc)
                    break
                except ValueError:
                    continue
        elif wybor == 0:
            break
        else:
            continue

#########################################################
        #############################################
########################################################
# Zapisywanie i odczytywanie danych w pliku
def depozyt(zl, sr, br):
    # Czyta wskazany wiersz w pliku i określa możliwość wczytania wartości zasobów
    def czyt_linii(linia):
        zawartosc = linecache.getline('sakwa', linia)  # Liczy od 1!
        zawartosc = zawartosc[:-1]
        zaw = True
        if zawartosc == '':
            zawartosc = '<puste>'
            zaw = False
        return zawartosc, zaw

    def nadanie_nazwy():
        while True:
            czysc()
            tabela('brak')  # Pusta przestrzeń
            zadania()  # Pusta przestrzeń
            try:
                tresc = input('\n Podaj nazwę dla konta (maks. 15 znaków):\n ')
                if len(tresc) > 15:
                    raise ValueError
                return tresc
            except ValueError:
                continue

    def lista_kont():
        # określanie zapisanych gniazd
        koniec = '0. Zakończ'
        konto1, kon1 = czyt_linii(1)
        konto2, kon2 = czyt_linii(5)
        konto3, kon3 = czyt_linii(9)
        konto4, kon4 = czyt_linii(13)
        konto5, kon5 = czyt_linii(17)
        konto6, kon6 = czyt_linii(21)
        konto7, kon7 = czyt_linii(25)
        konto8, kon8 = czyt_linii(29)
        konto9, kon9 = czyt_linii(33)
        # Wyświetlanie dostępnych zapisów
        print(' 1. ' + konto1.ljust(17) + '4. ' + konto4.ljust(17) + '7. ' + konto7.ljust(17) + koniec)
        print(' 2. ' + konto2.ljust(17) + '5. ' + konto5.ljust(17) + '8. ' + konto8.ljust(17))
        print(' 3. ' + konto3.ljust(17) + '6. ' + konto6.ljust(17) + '9. ' + konto9.ljust(17))
        print('')
        print(' ' + '─' * 70)  # pokarze zakres "widoku" i "pytania"
        return kon1, kon2, kon3, kon4, kon5, kon6, kon7, kon8, kon9

    def konto(n, z, s, b, dost):
        # wiersze w pliku (liczone od 0): Nazwy, Złota, Srebra, Brązu; określenie dostępu do opcji
        oper1 = ''
        oper2 = '2. Wczytaj'
        oper3 = ' 3. Zmień nazwę '
        oper4 = '4. Usuń'
        koniec = '0. Zakończ'
        # Ukrywanie opcji
        if not plik or not dost:
            oper2 = oper3 = oper4 = ''
        if zl != '':  # Zl ma wartość jeśli deklarowano lub wczytano
            oper1 = ' 1. Zapisz'
        # ODCZYTYWANIE WARTOŚCI
        czysc()
        # Warunki wyświetlania tabeli na kontach
        if plik:
            nazwa, nic = czyt_linii(n)  # nic to pojemnik na niepotrzebne tu dane
            if nazwa != '<puste>':  # Konto już istnieje...
                zloto, nic = czyt_linii(z)
                srebro, nic = czyt_linii(s)
                braz, nic = czyt_linii(b)
                if zl != '':  # ...i wcześniej zdeklarowano kwoty.
                    tabela('oba_zmienne', zloto, srebro, braz, nazwa, zl, sr, br, 'Masz')
                else:  # ...ale nie zdeklarowano kwoty.
                    tabela('deklarowanie', zloto, srebro, braz, nazwa)
            else:
                tabela('brak')
        else:
            tabela('brak')
        #tabela(tabelka)  # tablica będzie się zmieniać zależnie od obecn. pliku
        print(oper1.ljust(20) + oper2.ljust(20) + koniec)
        print(oper3.ljust(20) + oper4.ljust(20))
        print('\n')
        print(' ' + '─' * 70)  # pokarze zakres "widoku" i "pytania"
        while True:
            try:
                operacja = int(input('\n Co zrobić?\n '))
            except ValueError:
                continue
            # ZAPIS
            if operacja == 1 and (deklaruj > 1 or wczytane > 1): # Deklaracja lub odczyt
                # Tworzy plik, jeśli nie istnieje
                if not plik:
                    try:
                        with open('sakwa', 'xt') as f:
                            for i in range(36):
                                f.write('\n')
                    except FileExistsError:
                        pass
                # Pobiera dane z pliku
                with open('sakwa', encoding="utf8") as p:
                    dane = p.readlines()
                # Podmienia treść w odpowiednich pozycjach i zapisuje całość
                with open('sakwa', 'w', encoding="utf8") as p:
                    # Pyta o nazwę jeśli jej jeszcze nie ma
                    if not dost:
                        nazwa = nadanie_nazwy()
                        dane[n - 1] = (nazwa + '\n')
                    # Waruek sprawdzający czy wart. pochodzą z deklaracji, czy z odczytu.
                    if zk != '' and zk == zl:  # Dane deklarowane
                        dane[z - 1] = (str(zk) + '\n')
                        dane[s - 1] = (str(ss) + '\n')
                        dane[b - 1] = (str(bp) + '\n')
                    else:  #Dane z odczytu
                        dane[z - 1] = (str(zl) + '\n')
                        dane[s - 1] = (str(sr) + '\n')
                        dane[b - 1] = (str(br) + '\n')
                    p.writelines(dane)
                linecache.checkcache()  # Aktualizuje pam. podr. po zmianach w pliku
                return zk, ss, bp, 1  # Obejście niewczytania danych
            # ODCZYT
            elif operacja == 2 and dost:  # wczytanie
                return int(zloto), int(srebro), int(braz), 2
            # ZMIANA NAZWY
            elif operacja == 3 and dost:  # zmiana nazwy
                nazwa = nadanie_nazwy()
                with open('sakwa', encoding="utf8") as p:
                    dane = p.readlines()
                with open('sakwa', 'w', encoding="utf8") as p:
                    dane[n - 1] = (nazwa + '\n')
                    p.writelines(dane)
                linecache.checkcache()  # Aktualizuje pam. podr. po zmianach w pliku
                return zl, sr, br, 1  # Obejście niewczytania danych
            # USUŃ
            elif operacja == 4 and dost:  # Usuń
                with open('sakwa', encoding="utf8") as p:
                    dane = p.readlines()
                with open('sakwa', 'w', encoding="utf8") as p:
                    dane[n-1] = '\n'  # Bez nazwy będzie traktowało jak usunięte
                    p.writelines(dane)
                linecache.checkcache()
                return zl, sr, br, 1  # Obejście niewczytania danych
            # KONIEC
            elif operacja == 0:
                return zl, sr, br, 1  # Obejście niewczytania danych
            else:
                continue

    # ### Główna część Depozytu – ekran zapisanych kont ### #
    wczytane = 0  # potrzebne do ominięcia błędu nadpisania wartości przy otwarciu innego konta po wczytaniu.
    while True:
        czysc()
        # wyświetlanie tabeli zależnie od zadeklarowania kwoty
        if zl != '':
            tabela('deklarowanie', zl, sr, br, 'Masz')
        else:
            tabela('brak')
        # Zmienne k opisują dostęp do operacji na kontach
        k1, k2, k3, k4, k5, k6, k7, k8, k9 = lista_kont()
        try:
            wybor = int(input('\n Które konto?\n '))
        except ValueError:
            continue
        if wybor == 1:
            zl, sr, br, wczytane = konto(1, 2, 3, 4, k1)  # kolejne zmienne które porównają zk ze zwrotem
        elif wybor == 2:
            zl, sr, br, wczytane = konto(5, 6, 7, 8, k2)
        elif wybor == 3:
            zl, sr, br, wczytane = konto(9, 10, 11, 12, k3)
        elif wybor == 4:
            zl, sr, br, wczytane = konto(13, 14, 15, 16, k4)
        elif wybor == 5:
            zl, sr, br, wczytane = konto(17, 18, 19, 20, k5)
        elif wybor == 6:
            zl, sr, br, wczytane = konto(21, 22, 23, 24, k6)
        elif wybor == 7:
            zl, sr, br, wczytane = konto(25, 26, 27, 28, k7)
        elif wybor == 8:
            zl, sr, br, wczytane = konto(29, 30, 31, 32, k8)
        elif wybor == 9:
            zl, sr, br, wczytane = konto(33, 34, 35, 36, k9)
        elif wybor == 0:
            return zl, sr, br, wczytane  # Obejście niewczytania danych
        else:
            continue


#########################
# Główna część programu #
#########################


while True:
    # Test potrzebny uwzględniając, że deklaracja wynika też z wczytania zapisu.
    if deklaruj > 1:
        tab = 'jeden'
    czysc()
    tabela(tab)
    zadania(deklaruj)
    try:
        zadanie = input('\n Wpisz numer zadania: \n ')
        zadanie = int(zadanie)
    except ValueError:
        continue
    if zadanie == 1:
        zk, ss, bp = zasoby()
        deklaruj = 2
    elif zadanie == 2 and deklaruj > 1:
        zk, ss, bp = dodaj(zk, ss, bp)
    elif zadanie == 3 and deklaruj > 1:
        zk, ss, bp = odejmij(zk, ss, bp)
    elif zadanie == 4 and deklaruj > 1:
        zk, ss, bp = rozmiana(zk, ss, bp)
    elif zadanie == 5 and deklaruj > 1:
        zk, ss, bp = zamiana(zk, ss, bp)
    elif zadanie == 6 and deklaruj > 1:
        zk, ss, bp = inwestycja(zk, ss, bp)
    elif zadanie == 7 and deklaruj > 1:
        targowanie()
    elif zadanie == 8 and (plik or deklaruj > 1):
        zk, ss, bp, odczyt = depozyt(zk, ss, bp)

        deklaruj += odczyt
    elif zadanie == 9:
        continue
    elif zadanie == 0:
        break
    else:
        continue
