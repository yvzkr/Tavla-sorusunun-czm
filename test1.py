import unittest
import run

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




if __name__ == "__main__":
    unittest.main()