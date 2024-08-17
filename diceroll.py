import random
import pandas as pd
import matplotlib.pyplot as plt

def dobokocka_dobas():
    return random.randint(1, 6)

def szimulacio(dobasok_szama):
    eredmenyek = []
    for _ in range(dobasok_szama):
        dobas1 = dobokocka_dobas()
        dobas2 = dobokocka_dobas()
        eredmenyek.append(dobas1 + dobas2)
    return eredmenyek

def grafikon_keszites(eredmenyek):
    df = pd.DataFrame(eredmenyek, columns=['Eredmények'])
    osszesites = df['Eredmények'].value_counts().sort_index()

    osszesites.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Dobókocka dobások előfordulása')
    plt.xlabel('Dobások összege')
    plt.ylabel('Előfordulás')
    plt.xticks(range(0, 11))
    plt.grid(axis='y')
    plt.show()

def main():
    dobasok_szama = int(input("Add meg a dobások számát: "))
    eredmenyek = szimulacio(dobasok_szama)
    grafikon_keszites(eredmenyek)

if __name__ == "__main__":
    main()
