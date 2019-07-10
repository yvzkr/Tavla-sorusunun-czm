
def find_moves(checkers, dice1, dice2):

    #bütün taşları konumsal olarak taslar listesine atar
    taslar=[konum for konum,tasSayisi in checkers.items() for i in range(tasSayisi) ]

    print("Taşlar:",taslar)
    print("cherkers: ", checkers)




checkers = {1: 3, 6: 1, 10: 2, 12: 1, 19: 1}
print(find_moves(checkers, 6, 1))