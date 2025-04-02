import random


cisla = [1,5,10,15,20,25,30]

cislo1 = int(input("zadejte první číslo: "))
cislo2 = int(input("zadejte první číslo: "))
znamenko = (input("zadejte znaménko: "))

if znamenko == "+":
    vysledek = cislo1+cislo2
    print(vysledek)
elif znamenko == "-":
    vysledek = cislo1-cislo2
    print(vysledek)
elif znamenko == "*":
vysledek = cislo1*cislo2
    print(vysledek)
elif znamenko == "/":
    vysledek = cislo1/cislo2
    print(vysledek)
else:
    input("zadejte správné znaménko: ")
    
cisla.append(vysledek)
print(cisla)

random.choice(cisla)