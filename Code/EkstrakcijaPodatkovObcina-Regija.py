import csv
from csv import DictReader

reader = DictReader(open('../Data/prostovoljnaDrustva(ZA EKSTRAKCIJO MESTA-REGIJA).csv', 'rt', encoding='utf-8'))
naseljeRegija = []
for row in reader:
   arg2 = row["PodatkiObjave/PodatekObjave/2/__text"]
   arg3 = row["PodatkiObjave/PodatekObjave/12/__text"]
   if 0 < int(arg3) < 2000:
       naseljeRegija.append((arg2, "Osrednjeslovenska"))
   elif 2000 < int(arg3) < 3000:
       naseljeRegija.append((arg2, "Štajerska"))
   elif 3000 < int(arg3) < 4000:
       naseljeRegija.append((arg2, "Savinjska"))
   elif 4000 < int(arg3) < 5000:
       naseljeRegija.append((arg2, "Gorenjska"))
   elif 5000 < int(arg3) < 6000:
       naseljeRegija.append((arg2, "Primorska"))
   elif 6000 < int(arg3) < 7000:
       naseljeRegija.append((arg2, "Primorska"))
   elif 6000 < int(arg3) < 7000:
       naseljeRegija.append((arg2, "Primorska"))
   elif 7000 < int(arg3) < 8000:
       naseljeRegija.append((arg2, "Dolenjska"))
   elif 8000 < int(arg3) < 9000:
        naseljeRegija.append((arg2, "Prekmurje"))
print(naseljeRegija)
slovar = {}
file = open("../Data/Kraj-Regija.csv", "w")
for kraj, regija in naseljeRegija:
    slovar[kraj] = regija
print(slovar)
file.write("Kraj,Regija\n")
for key in slovar:
    file.write(key + "," +slovar.get(key) + "\n")
file.close()
