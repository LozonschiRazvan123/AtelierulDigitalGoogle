lista_produse = ["ciocolata", 'suc', 'paine', 'mere', "apa"]
lista_noua = []
# for x in lista_produse:
#    if "a" in x:
#         lista_noua.append(x)
# lista_noua = [x for x in lista_produse if "a" in x]
lista_noua = [x if "a" in x else "b" for x in lista_produse]
print(lista_noua)