def liczba(tablica,szukanie):
    for inndeks, wartosc in enumerate(tablica):
        if wartosc == szukanie:
            return inndeks
    return 0

tablica = [9,7,1,5,9,4]
szukanie = 9
indeks = liczba(tablica,szukanie)
print(indeks)


def liczby_odkonca(tablica,szukanie):
    for inndeks in range(len(tablica) -1,-1,-1):
        if tablica[inndeks] ==szukanie:
            return inndeks
    return 0
tablica = [9,7,1,5,9,4]
szukanie = 9
indeks = liczby_odkonca(tablica,szukanie)
print(indeks)
