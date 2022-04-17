# x=int(input())
# y=int(input())
# my_function=lambda x,y:x+y
# print(my_function(x,y))
# print(id(my_function))
# players=[{"nume":"Popescu","prenume":"Ion","rank":1}, {"nume":"Ionescu","prenume":"Mihai","rank":3},{ "nume":"Popa","prenume":"Ana","rank":2}, {"nume":"eu", "rank":4}]
# sort_players=sorted(players, key=lambda player:player["rank"])
# sort_players=players.sort(key=lambda player:player["rank"])
# print(players)
#  problema leetcode
# s=str(input())
# nr=0
# roman={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
# for i in range(len(s)):
#     if i>0 and roman[s[i]]>roman[s[i-1]]:
#         nr+= roman[s[i]]-2*roman[s[i-1]]
#      else:
#         nr+=roman[s[i]]
# print(nr)



# import copy
# a=[1,2,3,[4,4]]
# b=0
# b=copy.deepcopy(a)
# b[3][0]=1
# print(b)


players=[{"nume":"Popescu","prenume":"Ion","rank":1}, {"nume":"Ionescu","prenume":"Mihai","rank":3},{ "nume":"Popa","prenume":"Ana","rank":2}, {"nume":"eu", "rank":4}]

# def check_top_3_player(player):
#     #update_player=copy.deepcopy(player)
#     player["is_top_3"]=True if player["rank"]<=3 else False
#     return player
# players_with_top_3_value=map(check_top_3_player,players)
# print(tuple(players_with_top_3_value))

# players_with_top_3=map(lambda player: True if player["rank"]<=3 else False, players)
# all_name=filter(lambda player: True if player["nume"]=="Popa" else False, players)
# # print(list(players_with_top_3))
# print(tuple(all_name))

# a=[1,2,3]
# b=["one","two","three","four"]
# # c=zip(a,b)
# # print(list(c))
# for i in zip(a,b):
#     a,b=i
#     print(a,b,i)


# a=[1,2,3,4,5,6,7,8,9]
# list_a=[i+1 for i in a if i%2==0]
# print(list_a)

with open("data.txt","w") as file:
    file.write("hellor world")