
def cevirici(deger):
    
    if(deger == 'a'):
        deger = "97"
    elif(deger == "b"):
        deger = "98"
    elif(deger == "c"):
        deger = "99"
    elif(deger == "d"):
        deger = "100"
    elif(deger == "e"):
        deger = "101"
    elif(deger == "f"):
        deger = "102"
    elif(deger == "g"):
        cıktı = "103"
    elif(deger == "h"):
        cıktı = "104"
    elif(deger == "i"):
        cıktı = "105"
    elif(deger == "j"):
        cıktı = "106"
    elif(deger == "k"):
        cıktı = "107"
    elif(deger == "l"):
        cıktı = "108"
    elif(deger == "m"):
        cıktı = "109"
    elif(deger == "n"):
        cıktı = "110"
    elif(deger == "o"):
        cıktı = "111"
    elif(deger == "p"):
        cıktı = "112"
    elif(deger == "r"):
        cıktı = "113"
    elif(deger == "s"):
        cıktı = "114"
    elif(deger == "t"):
        cıktı = "115"
    elif(deger == "u"):
        cıktı = "116"
    elif(deger == "v"):
        cıktı = "117"
    elif(deger == "w"):
        cıktı = "118"
    elif(deger == "x"):
        cıktı = "120"
    elif(deger == "y"):
        cıktı = "121"
    elif(deger == "z"):
        cıktı = "122"
    elif(deger == "0"):
        cıktı = "48"
    elif(deger == "1"):
        cıktı = "49"
    elif(deger == "2"):
        cıktı = "50"
    elif(deger == "3"):
        cıktı = "51"
    elif(deger == "4"):
        cıktı = "52"
    elif(deger == "5"):
        cıktı = "53"
    elif(deger == "6"):
        cıktı = "54"
    elif(deger == "7"):
        cıktı = "55"
    elif(deger == "8"):
        cıktı = "56"
    elif(deger == "9"):
        cıktı = "57"
    return deger

print("------------------------\nASCII Dec-Char converter\n------------------------\nSonuçlar bilgiler.txt ye kaydedilecek\n------------------------")
print("chardan - dece çevirmek için : 1\ndecden - chara çevirmek için : 2")
secim = input("Seçim : ")
if(secim == "1"):
    ilk_deger = input("1.değeri giriniz : ")
    ikinci_deger = input("2.değeri giriniz, çevirmek için x : ")
    if(ikinci_deger == "x"):
        cevirici(ilk_deger)
        print("Çıktı = {}".format(cevirici(ilk_deger)))
        dosya = open("bilgiler.txt","w",encoding="utf-8")
        dosya.write("{}".format(cevirici(ilk_deger)))
        dosya.close()
    else:
        ucuncu_deger = input("3.değeri giriniz, çevirmek için x : ")
        if(ucuncu_deger == "x"):
            cevirici(ilk_deger)
            A = ("{}".format(cevirici(cıktı)))
            cevirici(ikinci_deger)
            B = ("{}".format(cevirici(cıktı)))
            print("Çıktı = " + A + B)
            dosya = open("bilgiler.txt","w",encoding="utf-8")
            dosya.write("Çıktı" + A + B)
            dosya.close()
        else:
            dorduncu_deger = input("4.değeri giriniz, çevirmek için x : ")
            if(dorduncu_deger == "x"):
                cevirici(ilk_deger)
                A = ("{}".format(cevirici(cıktı)))
                cevirici(ikinci_deger)
                B = ("{}".format(cevirici(cıktı)))
                cevirici(ucuncu_deger)
                C = ("{}".format(cevirici(cıktı)))
                print("Çıktı = " + A + B + C)
                dosya = open("bilgiler.txt","w",encoding="utf-8")
                dosya.write("Çıktı" + A + B + C)
                dosya.close()
            else:
                besinci_deger = input("5.değeri giriniz, çevirmek için x : ")
                if(besinci_deger == "x"):
                    cevirici(ilk_deger)
                    A = ("{}".format(cevirici(cıktı)))
                    cevirici(ikinci_deger)
                    B = ("{}".format(cevirici(cıktı)))
                    cevirici(ucuncu_deger)
                    C = ("{}".format(cevirici(cıktı)))
                    cevirici(dorduncu_deger)
                    D = ("{}".format(cevirici(cıktı)))                
                    print("Çıktı = " + A + B + C + D)
                    dosya = open("bilgiler.txt","w",encoding="utf-8")
                    dosya.write("Çıktı" + A + B + C + D)
                    dosya.close()
                else:
                    altinci_deger = input("6.değeri giriniz, çevirmek için x : ")
                    if(altinci_deger == "x"):
                        cevirici(ilk_deger)
                        A = ("{}".format(cevirici(cıktı)))
                        cevirici(ikinci_deger)
                        B = ("{}".format(cevirici(cıktı)))
                        cevirici(ucuncu_deger)
                        C = ("{}".format(cevirici(cıktı)))
                        cevirici(dorduncu_deger)
                        D = ("{}".format(cevirici(cıktı)))
                        cevirici(besinci_deger)
                        E = ("{}".format(cevirici(cıktı)))
                        print("Çıktı = " + A + B + C + D + E)
                        dosya = open("bilgiler.txt","w",encoding="utf-8")
                        dosya.write("Çıktı = " + A + B + C + D + E)
                        dosya.close()
                    else:
                        yedinci_deger = input("çevirmek için x : ")
                        if(yedinci_deger == "x"):
                            cevirici(ilk_deger)
                            A = ("{}".format(cevirici(cıktı)))
                            cevirici(ikinci_deger)
                            B = ("{}".format(cevirici(cıktı)))
                            cevirici(ucuncu_deger)
                            C = ("{}".format(cevirici(cıktı)))
                            cevirici(dorduncu_deger)
                            D = ("{}".format(cevirici(cıktı)))
                            cevirici(besinci_deger)
                            E = ("{}".format(cevirici(cıktı)))
                            cevirici(altinci_deger)
                            F = ("{}".format(cevirici(cıktı)))
                            print("Çıktı = " + A + B + C + D + E + F)
                            dosya = open("bilgiler.txt","w",encoding="utf-8")
                            dosya.write("Çıktı" + A + B + C + D + E + F)
                            dosya.close()
