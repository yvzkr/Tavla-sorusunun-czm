# Tavla-sorusunun-czm
Tavla sorusunun çözümü

Pulların pozisyonlarını, ve atılan iki zarın değerini girdi olarak alan ve bulabildiği hamleleri bulup puanlayarak 0 dan büyük puanı olan hamleleri geri döndüren find_moves adında bir fonksiyonunun yazılması

#Problem:
Elimizde bir tavla tahtası var. Bu tahta üzerindeki her üçgen saat yönüne doğru numaralandırılmış ve üzerinde rastgele yerleştirilmiş pullarımız var. Hangi üçgende kaç tane pul olduğunu aşağıdaki gibi bir sözlük içerisinde anlayabiliyoruz:

checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
Bu sözlük aşağıdaki resimdeki gibi bir dağılımı gösteriyor:

Sizden istediğimiz pulların pozisyonlarını, ve atılan iki zarın değerini girdi olarak alan ve bulabildiği hamleleri bulup puanlayarak 0 dan büyük puanı olan hamleleri geri döndüren find_moves adında bir fonksiyon yazmanız.
Örnek Girdi
def find_moves(checkers, dice1, dice2)
    ...
    ...
    ...

print(find_moves(checkers, 6, 1))

Örnek Çıktı
Üçlü tüplerden oluşan bir liste çıkmasını bekliyoruz. İlk hamleyi gösteren bir tuple, ikinci hamleyi gösteren bir tuple, iki hamlenin yarattığı puanı gösteren bir integer.

 (((1, 7), (6, 7), 3), ..., ..., ...)

      +       +      +
      |       |      +--> Bu hamlenin kaç puan ettiği.
      |       +---------> 6 numaralı üçgendeki pulu 7 ye
      +-----------------> 1 numaralı üçgendeki pulu 7 ye                

Hamlenin Puanlanması

    • Önemli kapılar: 5, 6, 7, 8, 17, 18, 19, 20
    • Bir kapı kapatmak +1 puan, eğer önemli kapı ise ise +2
    • Bir kapı açmak -1 puan, eğer önemli kapı ise -2
    • Bir taş açığa çıkarmak -1 puan.
    • Bir taşı açıktan kurtarmak +1 puan
    
  
    
#Ek AÇıklamalar

Puanlanırken Soruda bazı açıklamalarda boşlukları kendim değerlendirdiğim kısımlar.

Puan Verilirken kriterler:

Taşları Çektiğimiz yerlerdeki puanlama

    #Taşı Çektiğim yerdeki puanlama
    def EskiKonumPuanlama(konum1,konum2,yeniDamaTahtahsi,damaTahtası):

        tasiAyirmadaAlinanPuan = []
    
    # eski konum listesi en içerden başlasak ilk iki taşta aynı konumdan ayrılıyorsa buna bir defa bakmak için
    # teke düşürdükki bir daha puan vermeyelim
        eskiKonumListesi = list(set([konum1, konum2]))
        onemi = 1
    
    # Burada konumları eski konumları kontrol ediyoruz.
    # Olasılıklar hesaplanarak TasiAyirmadaAlinanPuana Ekliyoruz
    
        for konum in eskiKonumListesi:
           # eğer belirtilen kritik bölgelerde ise bunun değerini göderir
            # değilse geri 1 döndürür
          onemi = onemi * kritik_puan_katsayisi(konum, 1)
            # 1-)eskiden 1 tane taş vardı ve artık o taşı oradan aldın +1 puan
            if yeniDamaTahtahsi[konum] == 0 and damaTahtası[konum] == 1:
                tasiAyirmadaAlinanPuan.append(1)
            # 2-)eskiden bu konumda bir kapı vardı ama sen onu bozdun -1 puan
            elif yeniDamaTahtahsi[konum] < 2 and damaTahtası[konum] > 1:
                tasiAyirmadaAlinanPuan.append(-1 * onemi)  # eğer önemli ise 2 ile çarpar
                # 2a-) Hatta sonra bu kapıyı bozmayı bırak birde açık verdin -1 puan daha
                if yeniDamaTahtahsi[konum] == 1:
                    tasiAyirmadaAlinanPuan.append(-1)
            # 3-)eskiden buradaydım ve 1 tane taş vardı onu çektim ama hala 1 tane var o zman 1 puan alırsın
            # çünkü bir tane olanı kurtardım
            elif yeniDamaTahtahsi[konum] == 1 and damaTahtası[konum] == 1:
                tasiAyirmadaAlinanPuan.append(1)
            # print("çekilen taş:", konum, "kaç puan değerinde:", sum(tasiAyirmadaAlinanPuan))
        return sum(tasiAyirmadaAlinanPuan)
    
    
Taşları Koyduğumuz yerdeki puanlama

    #Taşı koyduğum yerdeki puanlama
    def yeniKonumPuanlama(konum1,konum2,yeniDamaTahtahsi,zar1,zar2,damaTahtası):
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
            #1-) eğer eski yuvada taş yoksa ve buraya sadece bir tane taş koyduysan -1 puan alırın yani açık verdin
            if eskiTasSayisi==0 and yeniDamaTahtahsi[yenikonum]==1:
                tasiKoymadaAlinanPuan.append(-1)
            #2-) eski taş sayın 0 dı ve sonra buraya bir kapı yaptın
            # eğer önemli ise çarpı iki katı
            elif eskiTasSayisi==0 and yeniDamaTahtahsi[yenikonum]>1:
                tasiKoymadaAlinanPuan.append(1*onemi)
            # 3-)eskiden burada tek açık vardı şimdi burada bir kapı var
            # eğer önemli ise çarpı 2 katı
            elif eskiTasSayisi==1 and yeniDamaTahtahsi[yenikonum]>1:
                tasiKoymadaAlinanPuan.append(1*onemi)
            #4-) eskiden burada bir taş olabilir eğer sayı sabit ise bi kotrol edelim
            elif eskiTasSayisi == 1 and yeniDamaTahtahsi[yenikonum] == 1:
                tasiKoymadaAlinanPuan.append(-1)
    
        return sum(tasiKoymadaAlinanPuan)