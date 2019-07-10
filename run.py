def konumlamaVePuanlama(konum1,konum2,zar1,zar2,checkers):

    pass

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
            #bütün taşların birbirleriyle ikişer ikişer eşleşerek konumlama ve Puanlama için
            #konumlama ve puanlama fonksiyonuna gönderildi.
            #fonksiyonda False Dönme olasılıkları var bunlar taşların haraket edemez olduğunu gösterir
            #örnegin 24. üçgendeki taş hiç haraket edemez. Çünkü gelebileceği en uç noktaya gelmiştir
            sonuc=konumlamaVePuanlama(i,j,dice1,dice2,checkers)
            #sonuc eğer False değilse puanTablosuListesine eklenir
            if sonuc:
                puanTablosuListesi.append(sonuc)

    #puan tablosu listesi ilk set yapılıyor çünkü burada bazı aynı konumdaki taşlarda çalıştığı için
    #bunları burada eledik. Örneğin 1 . yuvada 3 tane var tavlada sadece en üstteki taş haraket ettiriliyordu
    #3 defa oynattığımız için aynı taşı iki 3 defa oynatmış oluyoruz. aynı saonuçtan 3 tane olmuş oluyor
    #3 tane sonuçtan bir tanesi bize yeterli olduğu için sadece bir tanesini alsakk bize yeterli olur.
    return list(set(puanTablosuListesi))



checkers = {1: 3, 6: 1, 10: 2, 12: 1, 19: 1}
print(find_moves(checkers, 6, 1))