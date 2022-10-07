print("Bankomat")
parolumuz=321654
parol=(input("Parolu dahil edin\n"))
if (parol==parolumuz):
    print("Parol duzdur")
balans=1000
while True:
    process=input("""
    Balans uchun 1
    Artirmaq uchun 2
    Cixartmaq uchun 3
    Programmi bitirmek uchun q
            """)
    if (process=="q"):
        print ("Programm bitdi")
        break
    elif (process=="1"):
        print("Balansiniz:",balans)
    elif (process=="2"):
        artim=int(input ("Meblegi daxil edin: "))
        balans=balans+artim
        print("Balansiniz:",balans)
    
    elif(process=="3"):
        
        chix_mebleg=int (input("Chixartmaq istediyiniz meblegi daxil edin "))
        balans=balans-chix_mebleg
        print("Balansiniz:",balans)
    else:
        print("Kecherli process secin")

