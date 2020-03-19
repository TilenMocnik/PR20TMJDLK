import csv
from csv import DictReader

reader = DictReader(open('../Data/prostovoljnaDrustva(ZA EKSTRAKCIJO MESTA-REGIJA).csv', 'rt', encoding='utf-8'))
slovar = {}
for row in reader:
   kraj = row["PodatkiObjave/PodatekObjave/2/__text"]
   postnaSt = row["PodatkiObjave/PodatekObjave/12/__text"]
   if 0 < int(postnaSt) < 2000:
       slovar[kraj] = "Osrednjeslovenska"
   elif 2000 < int(postnaSt) < 3000:
       slovar[kraj] = "Štajerska"
   elif 3000 < int(postnaSt) < 4000:
       slovar[kraj] = "Savinjska"
   elif 4000 < int(postnaSt) < 5000:
       slovar[kraj] = "Gorenjska"
   elif 5000 < int(postnaSt) < 6000:
       slovar[kraj] = "Primorska"
   elif 6000 < int(postnaSt) < 7000:
       slovar[kraj] = "Primorska"
   elif 6000 < int(postnaSt) < 7000:
       slovar[kraj] = "Primorska"
   elif 7000 < int(postnaSt) < 8000:
       slovar[kraj] = "Dolenjska"
   elif 8000 < int(postnaSt) < 9000:
        slovar[kraj] = "Prekmurje"
file = open("../Data/Kraj-Regija2.csv", "w")
print(slovar)
file.write("Kraj,Regija\n")
for key in slovar:
    file.write(key + "," +slovar.get(key) + "\n")
file.close()
