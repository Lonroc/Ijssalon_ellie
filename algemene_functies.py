def mijn_functie_1(getal):
    return getal ** 2 

print(mijn_functie_1(4))

def mijn_functie_2(a, b):
    som = a + b
    verschil = a - b
    product = a * b
    quotient = a / b

    return som, verschil, product, quotient

resultaat = mijn_functie_2(12, 3)
print(resultaat)
