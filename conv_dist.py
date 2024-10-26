m = float(input("Quantos metros?: "))
med = str(input("qual é a medida que queres?: "))
if med == "km":
    medEmKm = m/1000
    print(medEmKm, "km")
if med == "hm":
    medEmKm = m/100
    print(medEmKm, "hm")
if med == "dam":
    medEmKm = m / 10
    print(medEmKm, "dam")
if med == "m":
    medEmKm = m
    print(medEmKm, "m")
if med == "dm":
    medEmKm = m * 10
    print(medEmKm, "dm")
if med == "cm":
    medEmKm = m * 100
    print(medEmKm, "cm")
if med == "mm":
    medEmKm = m * 1000
    print(medEmKm, "mm")
