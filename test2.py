import unittest
import run
import sys

class exampleTest(unittest.TestCase):
    damaTahtası={1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
    zar1=6
    zar2=1
    konum1=1
    konum2=6


    def testRunCevap(self):
        sonuc = run.find_moves(self.damaTahtası, self.zar1,self.zar2)
        print("Gönderilen Taş pozisyonları =>",self.damaTahtası,"\nGelen Zarlar=>",self.zar1,self.zar2,"\nTaşları Oynatma Olasılıklarımız ve Puanlama=>",sonuc)
        print("--------------------")

    #Konumları gönderilen taşların puanlarını ve puanını öğrenme
    def testKonumPuan(self):
        print("Sonuçlarını Merak ettiğimiz konumlar=>",self.konum1,self.konum2)
        sonuc=run.konumlamaVePuanlama(self.konum1,self.konum2,self.zar1,self.zar2,self.damaTahtası)
        print("Haraketin Sonucu=>",sonuc)
        print("--------------------")

    def testKonumlandırmaKontrol(self):
        print("Seçilen,",self.konum1,"deki taş",self.konum1+self.zar1," konumuna koyulabiliyor mu?")
        sonuc=run.konumlandırmaKontrol(self.damaTahtası, self.konum1, self.zar1)
        if sonuc:
            print("Koyulabilir")
        print("---------------------")

    def testTasYerlestir(self):
        print("Konumlar=>" , self.damaTahtası)
        print(self.konum1," konumundaki taşın ", self.zar1," zarıyla haraket ettirme")
        run.TasYerlestir(self.damaTahtası, self.konum1, self.zar1)
        print(self.damaTahtası)
        print("--------------------")

    def testBolgeKontrol(self):
        print("Oynanacak bölgenin önemli olup olmadığını kontrol ediyor")
        print(run.kritik_puan_katsayisi(self.konum1))
        print("---------------------")

    def testTaslarıYerlestir(self):
        print("Atılan Zarlar ile taşların konumlarından alınıp oynanması \nDamaTahtasının eski hali=>",self.damaTahtası)
        print("Oynanan konumlar=>",self.konum1,self.konum2,"Zarla=>",self.zar1,self.zar2)
        run.taslarıYerlestir(self.konum1,self.konum2,self.zar1,self.zar2,self.damaTahtası)
        print("Dama Tahtasının yeni hali=>",self.damaTahtası)
        print("-----------------------")

    def testPuanaAyrıntıları(self):
        print("Dama Tahtasına Taşlar koyulduktan sonra gelen puanlama")
        yeniDamaTahtası=self.damaTahtası.copy()
        run.taslarıYerlestir(self.konum1,self.konum2,self.zar1,self.zar2,yeniDamaTahtası)
        print("Yeni Dama Tahtası ",yeniDamaTahtası,"Taşların Eski konumu=>", self.damaTahtası)
        puan=run.TaslarKoyulduktanSonraPuanlama(self.konum1,self.konum2,self.zar1,self.zar2,self.damaTahtası,yeniDamaTahtası)
        print("1. Konum ve 1. zar=>",self.konum1,self.zar1,"2. konum ve 2. zar",self.konum2,self.zar2,"Alınan Puan=>",puan)
        print("------------------------")


if __name__ == "__main__":
    unittest.main()