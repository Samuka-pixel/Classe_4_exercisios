m = float(input("Quantos metros?: "))
med = str(input("qual é a medida que queres?: "))
if med == "km":
    medEmKm = m/1000
    print(medEmKm, "km")
else:
    print(m * 3.281, "pés")