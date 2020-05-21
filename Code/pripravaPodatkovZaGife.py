from csv import DictReader

reader = DictReader(open('../Data/indexDelavcev.csv', 'rt', encoding='utf-8'))
slovar = {}
for row in reader:
    slovar[row['MUNICIPALITIES']] = row['2003 Labour migration index']

tabelaNaravniPrirastZaSlovenijo = []
tabelaNaravniPrirastZaSlovenijoString = []
tabelaPriseljevanje = []
tabelaPriseljevanjeString = []

for value in slovar:
    if value != "SLOVENIA":
        if slovar[value] != "-":
            prikazValue = value;
            if prikazValue == "Solčava":
                prikazValue = "Solcava"
            if prikazValue == "Luče":
                prikazValue = "Luce"
            if prikazValue == "Apače":
                prikazValue = "Apace"
            if prikazValue == "Apače":
                prikazValue = "Apace"
            if prikazValue == "Zavrč":
                prikazValue = "Zavrc"
            if prikazValue == "Sveti Jurij ob Ščavnici":
                prikazValue = "Sveti Jurij"
            if prikazValue == "Rače - Fram":
                prikazValue = "Race-Fram"
            if prikazValue == "Kidričevo":
                prikazValue = "Kidricevo"
            if prikazValue == "Hoče - Slivnica":
                prikazValue = "Hoce-Slivnica"
            if prikazValue == "Zreče":
                prikazValue = "Zrece"
            if prikazValue == "Podčetrtek":
                prikazValue = "Podcetrtek"
            if prikazValue == "Radeče":
                prikazValue = "Radece"
            if prikazValue == "Braslovče":
                prikazValue = "Braslovce"
            if prikazValue == "Zagorje ob Savi":
                prikazValue = "Zasavska"
            if prikazValue == "Moravče":
                prikazValue = "Moravce"
            if prikazValue == "Divača":
                prikazValue = "Divaca"
            if prikazValue == "Mirna Peč":
                prikazValue = "Mirna Pec"
            if prikazValue == "Novo mesto":
                prikazValue = "Novo Mesto"
            if prikazValue == "Ivančna Gorica":
                prikazValue = "Ivancna_Gorica"
            if prikazValue == "Kočevje":
                prikazValue = "Kocevje"
            if prikazValue == "Semič":
                prikazValue = "Semic"
            if prikazValue == "Črnomelj":
                prikazValue = "Crnomelj"
            prikazValue = prikazValue.replace(" - ", "-")
            prikazValue = prikazValue.replace(" ", "_")
            prikazValue = prikazValue.replace("Slov.", "Slovenskih")
            if prikazValue == "Šempeter-Vrtojba":
                prikazValue = "Šempeter_-_Vrtojba"
            print(prikazValue + " " + str(round(float(slovar[value]))))


