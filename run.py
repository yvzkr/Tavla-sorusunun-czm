

def find_moves(checkers, dice1, dice2):
    #checkers={1: 3, 6: 1, 10: 2, 12: 1, 19: 1}
    #bütün taşları konumsal olarak taslar listesine atar.
    #buradki maksat artık elimizde 8 tane taşın konumları var
    #bu konumları (1,1,1,6,7,12,13)sırasıyla elde etmiş oldu
    taslar=[konum for konum,tasSayisi in checkers.items() for i in range(tasSayisi) ]

    print("Taşlar:",taslar)
    print("cherkers: ", checkers)

    # Göndereceğimiz konumlardan, zarlardan dönen ve yeni konumları ve puanları tutacak eleman
    puanTablosuListesi=[]
    # burada ilk i ye sıfrıncı index i atıyoruz.
    for i in taslar:
        #sonra j ye de  sırasıyla
        for j in taslar:
            print(i,j)



checkers = {1: 3, 6: 1, 10: 2, 12: 1, 19: 1}
print(find_moves(checkers, 6, 1))