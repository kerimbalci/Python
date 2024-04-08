
import math

def baslangic_ekrani():
    print("""
***** Hesap Makinesi *****
Toplama İşlemi > 1
Çıkarma İşlemi > 2
Çarpma İşlemi > 3
Bölme İşlemi > 4
Karekök alma İşlemi > 5
Kare alma İşlemi > 6 
Küp alma İşlemi > 7
Çıkmak için > 'q'          
  """)
def toplama_islemi():
    toplam = 0
    print("""
          *** Toplama İşlemi ***
          Çıkmak ve sonuç için 'q'""")
    while True:
        sayi = input("Sayı giriniz: ")
        if sayi.lower() == 'q':
            print("Toplam:", toplam)
            print("Programdan çıkılıyor...")
            break
        try:
            girdi = float(sayi)
            toplam += girdi
        except ValueError:
            print("Hatalı giriş. Lütfen bir sayı girin.")

def cikarma_islemi():
    print("""
          *** Çıkarma İşlemi ***
          Çıkmak ve sonuç için 'q'""")
    ilk_deger = None
    while True:
        sayi = input("Sayı giriniz: ")
        if sayi.lower() == 'q':
            if ilk_deger is None:
                print("Hiçbir değer girilmedi.")
            else:
                print("Sonuç:", ilk_deger)
                print("Programdan çıkılıyor...")
            break
        try:
            girdi = float(sayi)
            if ilk_deger is None:
                ilk_deger = girdi
            else:
                ilk_deger -= girdi
        except ValueError:
            print("Hatalı giriş. Lütfen bir sayı girin.")
def bolme_islemi():
    print("""
          *** Çarpma İşlemi ***
          Çıkmak ve sonuç için 'q''""")
    ilk_deger = None
    while True:
        sayi= input("Sayı giriniz: ")
        if sayi.lower() == 'q':
            if ilk_deger is None:
                print("Hiçbir değer girilmedi.")
            else:
                print("Sonuç:", ilk_deger)
                print("Programdan çıkılıyor...")
            break
        try:
            girdi = float(sayi)
            if ilk_deger is None:
                ilk_deger = girdi
                     
            else:
                if girdi != 0:
                    ilk_deger /= girdi
                else:
                    print("Hatalı giriş. Sıfıra bölme hatası!")    

                
        except ValueError:
            print("Hatalı giriş. Lütfen bir sayı girin.")

def carpma_islemi():
    print("""
          *** Çarpma İşlemi ***
          Çıkmak ve sonuç için 'q'""")
    ilk_deger=1

    while True:
        sayi = input("Sayı giriniz: ")
        if sayi.lower() =='q':
            print("Sonuç:", ilk_deger)
            print("Programdan çıkılıyor...")
            break
        try:
            girdi = float(sayi)
            ilk_deger *= girdi
        except ValueError:
            print("Hatalı giriş. Lütfen bir sayı girin.")

def karekok():
    print("""
          *** Karekök Alma İşlemi ***
          Çıkmak için 'q'""")
    try:
        while True:
            sayi = float(input("Sayı giriniz: "))
            if sayi=='q':
                break
        
            if sayi<0:
             print("Negatif bir sayının karekökü olmaz.")
         
            else:
             karekok = math.sqrt(sayi)
             print("Girdiğiniz sayının karekökü: ",karekok)
    except ValueError:
        print("Hatalı giriş. Lütfen bir sayı girin.")

def kare_alma():
    print("""
          *** Kare Alma İşlemi ***
          Çıkmak için 'q'""")
    try:
        while True:
            sayi = float(input("Sayı giriniz: "))
            if sayi=='q':
                break
            kare = sayi**2
            print("Girdiğiniz sayının karesi: ",kare)
    except ValueError:
        print("Hatalı giriş. Lütfen bir sayı girin.")
def kup_alma():
    print("""
          *** Küp Alma İşlemi ***
          Çıkmak için 'q'""")
    try:
        while True:
            
            sayi = float(input("Sayı giriniz: "))
            if sayi=='q':
                break
            kup = sayi**3
            print("Girdiğiniz sayının küpü: ",kup)
    except ValueError:
        print("Hatalı giriş. Lütfen bir sayı girin.")
    
    

while True:
    baslangic_ekrani()
    islem = input("İşlem seçiniz: ")
    if islem == "1":
       
        toplama_islemi()
    elif islem == "2":
       
        cikarma_islemi()
    elif islem == "3":
        
        carpma_islemi()    
    elif islem == "4":
       
        bolme_islemi()     
    elif islem == "5":
       
        karekok()
    elif islem == "6":
       
        kare_alma()
    elif islem == "7":
       
        kup_alma()
    elif islem == "q":  
        break          
    else:
        print("Geçersiz işlem seçimi.")

    
