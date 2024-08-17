def szovegfajl_elemzese(fajlnev):
    try:
        with open(fajlnev, 'r', encoding='utf-8') as fajl:
            tartalom = fajl.read()

            # Szavak számának meghatározása
            szavak = tartalom.split()
            szavak_szama = len(szavak)

            # Leghosszabb és legrövidebb szó meghatározása
            legrovidebb_szo = min(szavak, key=len)
            leghosszabb_szo = max(szavak, key=len)

            return szavak_szama, leghosszabb_szo, legrovidebb_szo

    except FileNotFoundError:
        return "A megadott fájl nem található."

# Példa használat:
fajlnev = "pelda.txt"
eredmeny = szovegfajl_elemzese(fajlnev)

if type(eredmeny) == tuple:
    szavak_szama, leghosszabb_szo, legrovidebb_szo = eredmeny
    print(f"Szavak száma: {szavak_szama}")
    print(f"Legrövidebb szó: {legrovidebb_szo}")
    print(f"Leghosszabb szó: {leghosszabb_szo}")
else:
    print(eredmeny)
