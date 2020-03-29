from csv import DictReader
import matplotlib.pyplot as plt
import numpy as np

reader = DictReader(open('../Data/prebivalstvo-SLO.csv', 'rt', encoding='utf-8'))
slovar = {}
for row in reader:
    slovar[row["MUNICIPALITIES"]] = row

"""
for key in slovar:
    print(key)
    for i in range(0, len(slovar[key])):
        print(slovar[key].get("MUNICIPALITIES"))
"""

tabelaNaravniPrirastZaSlovenijo = []
tabelaNaravniPrirastZaSlovenijoString = []
tabelaPriseljevanje = []
tabelaPriseljevanjeString = []

#Naravno prirast za celo Slovenijo spravimo v slovar
for value in slovar["SLOVENIA"]:
    if "Natural increase" in value:
        tabelaNaravniPrirastZaSlovenijo.append(int(slovar["SLOVENIA"].get(value)))
        tabelaNaravniPrirastZaSlovenijoString.append(slovar["SLOVENIA"].get(value))
    elif "Net migration from abroad" in value:
        tabelaPriseljevanje.append(int(slovar["SLOVENIA"].get(value)))
        tabelaPriseljevanjeString.append(slovar["SLOVENIA"].get(value))

plt.figure(figsize=(15, 7))
plt.title("Primerjava naravna prirasta/priseljevanja")
plt.ylabel("Število ljudi")
plt.xticks([])
plt.plot(np.arange(1995, 2019, 1), tabelaNaravniPrirastZaSlovenijo, label='Naravna prirast')
plt.plot(np.arange(1995, 2019, 1), tabelaPriseljevanje, label='Priselitve')

columns = []
for x in range(1995, 2019):
    columns.append(str(x))
the_table = plt.table(cellText=[tabelaPriseljevanjeString, tabelaNaravniPrirastZaSlovenijoString],
                      rowLabels=["Priseliteve", "Naravna prirast"],
                      colLabels=columns,
                      loc='bottom')
plt.legend()
plt.show()
