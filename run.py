
def tasiKoyKontrol(damaTahtası,konum):
    #tsaşı koyduğunda 24. üçgeni geçerse bu uygun bir hamle olmaz
    if konum > 24:
        return False
    return True

def tasiCekKontrol(checkers, konum):
    #taşın bu konumda olmaması durumunda
    if checkers[konum]!=0:
        return True
    else:
        return False

def konumlandırmaKontrol(damaTahtası, konum, zar):
    #Taşı çektiğimizde bir kontrol yapıyor
    if not tasiCekKontrol(damaTahtası,konum):
        return False
    #Taşı koyarken bir kontrol yappıyor bir problem olup olmaması için
    if not tasiKoyKontrol(damaTahtası,konum + zar):
        return False
    #bir problem çıkmaması halinde True
    return True

#tahtanın yuvasına taşı yerleştir
def tasiKoy(damaTahtasi, konum):
    #tabiki yeni konumumuz damaTahtası sözllüğünde olmayacağından
    #onu eklememiz lazım bunuda try except ile hallediyoruz
    try:
        damaTahtasi[konum] += 1
    except KeyError:
        damaTahtasi[konum]=1

#tahtanın konumundan yuvayı 1 eksiltir
def tasiCek(damaTahtasi, konum):
    damaTahtasi[konum]-=1

def TasYerlestir(damaTahtasi,konum,zar):
    tasiCek(damaTahtasi,konum)
    tasiKoy(damaTahtasi,konum+zar)

def kritik_puan_katsayisi(konum,puan,kritik_bolgeler = [5, 6, 7, 8, 17, 18, 19, 20]):

    if konum in kritik_bolgeler:
        puan*=2
    return puan


# konum1: birinci taşın konumu
#konum2: ikinci taşın konumu
#zar1: gelen 1. zarın konumu
#zar2: gelen ikinci zarın konumu
def PUANLAMA(konum1,konum2,zar1, zar2,damaTahtası):
    #yeni dama tahtası  tanımlıyoruz bunun nedeni taşları
    yeniDamaTahtahsi=damaTahtası.copy()

    #birinci zar için tahtayı kontrol ediyoruz.
    #taş 24. kareyi aşıp aşmadığı yada taşın bu konumda olup olmadığı kontrol ediyor
    #eğer durumları karşılamıyor ise False döndürecek ve puanda alamayacağız
    if not konumlandırmaKontrol(yeniDamaTahtahsi, konum1, zar1):
        return False

    #dama tahtasında kontrolümüzü yaptıktan sonra şimdi taşımızı çekip yeni konumuza
    #koymaya geldi.

    #birinci zar ve birincikonum için yerleştiriyoruz
    #print("Birinci Taş=>",konum1,"Birinci Zar=>",zar1,"Birinci Taş yerleşmeden önce damaTahtası:", yeniDamaTahtahsi)

    TasYerlestir(yeniDamaTahtahsi,konum1,zar1)

    #print("Birinci Taş yerleştikten sonra damaTahtası:", yeniDamaTahtahsi, "\n")
    #ikinci taşın konumuna yerleşmesi

    if not konumlandırmaKontrol(yeniDamaTahtahsi, konum2, zar2):
        return False

    TasYerlestir(yeniDamaTahtahsi, konum2, zar2)

    #print("Taşlar yerleşti konumlar=> {", konum1, konum2, "} yeni konumlar=>{",konum1+zar1,konum2+zar2,"}")
    #print("Eski tahta=>", damaTahtası, "\nYeni tahta=>", yeniDamaTahtahsi,"\n")

    tasiAyirmadaAlinanPuan=[]

    #eski konum listesi en içerden başlasak ilk iki taşta aynı konumdan ayrılıyorsa buna bir defa bakmak için
    #teke düşürdükki bir daha puan vermeyelim
    eskiKonumListesi=list(set([konum1,konum2]))
    onemi=1

    #Burada konumları eski konumları kontrol ediyoruz.
    #Olasılıklar hesaplanarak TasiAyirmadaAlinanPuana Ekliyoruz

    for konum in eskiKonumListesi:
        #eğer belirtilen kritik bölgelerde ise bunun değerini göderir
        #değilse geri 1 döndürür
        onemi=onemi*kritik_puan_katsayisi(konum,1)
        #1-)eskiden 1 tane taş vardı ve artık o taşı oradan aldın +1 puan
        if yeniDamaTahtahsi[konum]==0 and damaTahtası[konum]==1:
            tasiAyirmadaAlinanPuan.append(1)
        #2-)eskiden bu konumda bir kapı vardı ama sen onu bozdun -1 puan
        elif yeniDamaTahtahsi[konum]<2 and damaTahtası[konum]>1:
            tasiAyirmadaAlinanPuan.append(-1*onemi)#eğer önemli ise 2 ile çarpar
            #2a-) Hatta sonra bu kapıyı bozmayı bırak birde açık verdin -1 puan daha
            if yeniDamaTahtahsi[konum]==1:
                tasiAyirmadaAlinanPuan.append(-1)
        # 3-)eskiden buradaydım ve 1 tane taş vardı onu çektim ama hala 1 tane var o zman 1 puan alırsın
        # çünkü bir tane olanı kurtardım
        elif yeniDamaTahtahsi[konum]==1 and damaTahtası[konum]==1:
            tasiAyirmadaAlinanPuan.append(1)
        #print("çekilen taş:", konum, "kaç puan değerinde:", sum(tasiAyirmadaAlinanPuan))




    yeniKonumListesi=list(set([konum1+zar1,konum2+zar2]))
    tasiKoymadaAlinanPuan=[]

    onemi=1

    for yenikonum in yeniKonumListesi:
        onemi = onemi * kritik_puan_katsayisi(yenikonum, 1)
        eskiTasSayisi=0
        if not yenikonum in damaTahtası:
            eskiTasSayisi=0
        else:
            eskiTasSayisi=damaTahtası[yenikonum]
        # eğer eski yuvada taş yoksa ve buraya sadece bir tane taş koyduysan -1 puan alırın yani açık verdin
        if eskiTasSayisi==0 and yeniDamaTahtahsi[yenikonum]==1:
            tasiKoymadaAlinanPuan.append(-1)
        # eski taş sayın 0 dı ve sonra buraya bir kapı yaptın
        # eğer önemli ise çarpı iki katı
        elif eskiTasSayisi==0 and yeniDamaTahtahsi[yenikonum]>1:
            tasiKoymadaAlinanPuan.append(1*onemi)
        # eskiden burada tek açık vardı şimdi burada bir kapı var
        # eğer önemli ise çarpı 2 katı
        elif eskiTasSayisi==1 and yeniDamaTahtahsi[yenikonum]>1:
            tasiKoymadaAlinanPuan.append(1*onemi)
        # eskiden burada bir taş olabilir eğer sayı sabit ise bi kotrol edelim
        elif eskiTasSayisi == 1 and yeniDamaTahtahsi[yenikonum] == 1:
            tasiKoymadaAlinanPuan.append(-1)



    return sum(tasiAyirmadaAlinanPuan)+sum(tasiKoymadaAlinanPuan)



def konumlamaVePuanlama(konum1,konum2,zar1,zar2,checkers):
    puan=PUANLAMA(konum1,konum2,zar1,zar2,checkers)
    if puan and puan>0:
        return ((konum1, konum1+zar1),(konum2,konum2+zar2), puan)
    else:
        return False

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



checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
print(find_moves(checkers, 6, 1))