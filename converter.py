dosya = open("bilgiler.txt","w",encoding="utf-8")
values = []
çıktı = []
def Lister(Cdeger):
    for i in range(0,lenDeger):
        values.append(Cdeger[i])
def cevirici():
    for i in range(0,lenDeger):
        if(values[i] == 'a'):
            çıktı.append("97")
        elif(values[i] == "b"):
            çıktı.append("98")
        elif(values[i] == "c"):
            çıktı.append("99")
        elif(values[i] == "d"):
            çıktı.append("100")
        elif(values[i] == "e"):
            çıktı.append("101")
        elif(values[i] == "f"):
            çıktı.append("102")
        elif(values[i] == "g"):
            çıktı.append("103")
        elif(values[i] == "h"):
            çıktı.append("104")
        elif(values[i] == "i"):
            çıktı.append("105")
        elif(values[i] == "j"):
            çıktı.append("106")
        elif(values[i] == "k"):
            çıktı.append("107")
        elif(values[i] == "l"):
            çıktı.append("108")
        elif(values[i] == "m"):
            çıktı.append("109")
        elif(values[i] == "n"):
            çıktı.append("110")
        elif(values[i] == "o"):
            çıktı.append("111")
        elif(values[i] == "p"):
            çıktı.append("112")
        elif(values[i] == "q"):
            çıktı.append("113")
        elif(values[i] == "r"):
            çıktı.append("114")
        elif(values[i] == "s"):
            çıktı.append("115")
        elif(values[i] == "t"):
            çıktı.append("116")
        elif(values[i] == "u"):
            çıktı.append("117")
        elif(values[i] == "v"):
            çıktı.append("118")
        elif(values[i] == "w"):
            çıktı.append("119")
        elif(values[i] == "x"):
            çıktı.append("120")
        elif(values[i] == "y"):
            çıktı.append("121")
        elif(values[i] == "z"):
            çıktı.append("122")
        elif(values[i] == "0"):
            çıktı.append("48")
        elif(values[i] == "1"):
            çıktı.append("49")
        elif(values[i] == "2"):
            çıktı.append("50")
        elif(values[i] == "3"):
            çıktı.append("51")
        elif(values[i] == "4"):
            çıktı.append("52")
        elif(values[i] == "5"):
            çıktı.append("53")
        elif(values[i] == "6"):
            çıktı.append("54")
        elif(values[i] == "7"):
            çıktı.append("55")
        elif(values[i] == "8"):
            çıktı.append("56")
        elif(values[i] == "9"):
            çıktı.append("57")
        else:
            print("Lütfen geçerli bir değer seçiniz")
            i -= 1
MainScreen = 0
while MainScreen == 0: 
    print("------------------------\nASCII Dec-Char converter\n------------------------\nSonuçlar bilgiler.txt ye kaydedilecek\n------------------------")
    secim = input("1.Char - Dec :\nSeçim : ")
    if(secim == "1"):
        Cdeger = input("Çevirilecek değer:")
        lenDeger = len(Cdeger)
        Lister(Cdeger)
        cevirici()
        toDeger = çıktı[0]
        for i in range(1,lenDeger):
            toplam = toDeger + çıktı[i]
            toDeger = toplam
        print("Sonuç: " + toDeger)
        dosya.write(toDeger + "\n")
        a = input("Çıkmak için x\nDevam etmek için a\n")
        if a == "x":
            MainScreen = 1
    else:
        print("Lütfen bir seçenek seçiniz")
        input("")
dosya.close()
