x=int(input())
y=int(input())
my_function=lambda x,y:x+y
print(my_function(x,y))
print(id(my_function))
players=[ {"nume":"Popescu","prenume":"Ion","rank":1}, {"nume":"Ionescu","prenume":"Mihai","rank":3}, {"nume":"Popa","prenume":"Ana","rank":2}]
sort_players=sorted(players, key=lambda players:players["nume"])
print(sort_players)
# problema leetcode
s=str(input())
nr=0
roman={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
for i in range(len(s)):
    if i>0 and roman[s[i]]>roman[s[i-1]]:
        nr+= roman[s[i]]-2*roman[s[i-1]]
     else:
        nr+=roman[s[i]]
print(nr)