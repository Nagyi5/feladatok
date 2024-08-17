import random
import pandas as pd
import matplotlib.pyplot as plt

def otoslotto_huzas():
    return random.randint(1, 90)

def szimulacio(huzasok_szama):
    eredmenyek = []
    for _ in range(huzasok_szama):
        szamok = set()
        while len(szamok) < 5:
            szamok.add(otoslotto_huzas())
        eredmenyek.extend(szamok)  # Hozzáadjuk az összes számot a listához
    return eredmenyek

def grafikon_keszites(eredmenyek):
    df = pd.DataFrame(eredmenyek, columns=['Eredmények'])
    osszesites = df['Eredmények'].value_counts().sort_index()

    osszesites.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Ötöslottó számok előfordulása')
    plt.xlabel('Számok')
    plt.ylabel('Előfordulás')
    plt.xticks(range(0, 90))  # 1-től 90-ig tartó tengely
    plt.grid(axis='y')
    plt.show()
def main():
    huzasok_szama = int(input("Add meg a húzások számát: "))
    eredmenyek = szimulacio(huzasok_szama)
    grafikon_keszites(eredmenyek)

if __name__ == "__main__":
    main()