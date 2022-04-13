lista_produse = ["ciocolata", 'suc', 'paine', 'mere', "apa"]
lista_noua = []
# for x in lista_produse:
#    if "a" in x:
#         lista_noua.append(x)
# lista_noua = [x for x in lista_produse if "a" in x]
# lista_noua = [x if "a" in x else "b" for x in lista_produse]
# print(lista_noua)


# l=[0,2,3,5,6,7,432,4324,10]
# listamea=[]
# for i in l:
#     if i%2==0:
#         listamea.append(i)
# print(listamea)


# def my_function(n):
#    if n==0:
#       return 0
#    elif n%2==1:
#       return n+my_function(n-1)
#    else:
#       return my_function(n-1)
# print(my_function(7))



try:
	a = 8
	b = 0
	c = a / b
except ZeroDivisionError:
	c = 0
print(c)
