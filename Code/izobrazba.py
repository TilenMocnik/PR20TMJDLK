from csv import DictReader
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num
import datetime

reader = DictReader(open('../Data/izobrazba.csv', 'rt', encoding='utf-8'))
slovar = {}
for row in reader:
    slovar[row["OBČINE"]] = row


def normalization(tabela):
    skupaj = 0
    for x in tabela:
        skupaj = skupaj + int(x)

    novaTab = []
    for x in tabela:
        novaTab.append(round(int(x)/skupaj, 2) *100)
    return novaTab


def kreirajTab(imeKraja, leto):
    tab = [slovar[imeKraja].get(str(leto) + " Brez izobrazbe, nepopolna osnovnošolska"),
           slovar[imeKraja].get(str(leto) + " Srednješolska - Skupaj"),
           slovar[imeKraja].get(str(leto) + " Višješolska, visokošolska - Skupaj")]
    return normalization(tab)


tabStore = kreirajTab("Štore", 2019)
tabZavrc = kreirajTab("Zavrč", 2019)
tabLjubljana = kreirajTab("Ljubljana", 2019)

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars


fig = plt.figure()
ax = fig.add_subplot(111)
yvals = tabStore
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = tabZavrc
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = tabLjubljana
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('Prebivalstvo v %')
ax.set_xlabel('Stopnja izobrazbe')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Nizka', 'Srednja', 'Visoka'))
ax.legend((rects1[0], rects2[0], rects3[0]), ('Štore', 'Zavrč', 'Ljubljana'))

plt.title("Stopnja izobrazbe za Štore, Zavrč in Ljubljano")
plt.show()

print(tabStore)
print(tabZavrc)
print(tabLjubljana)
