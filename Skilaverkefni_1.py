import random
#Elmar Ólafsson
#23.1.2017
#valmynd
valmynd = 1#byrja á að gera valmynd fyrir notandann
while valmynd == 1:
    print("\n1.Verkefni, Listi yfir tölur")
    print("2.Verlefni, Random tölur")
    print("3.Verkefni, Strengjalisti")
    print("4.Verkefni, Fjöldi teningakasta ákveðinn af notanda")
    print("5.Verkefni, Skráning í áfanga")
    print("6.Hætta")
    valkostur = int(input("\nVinsamlegast veldu verkefni: "))#hann velur 1-5

    #Liður1
    if valkostur == 1:#Númer 1 er valið
        talnalisti = []#tómur listi
        tala_1 = int(input("\nSláðu inn 1 tölu af 7: "))
        tala_2 = int(input("Sláðu inn 2 tölu af 7: "))
        tala_3 = int(input("Sláðu inn 3 tölu af 7: "))
        tala_4 = int(input("Sláðu inn 4 tölu af 7: "))
        tala_5 = int(input("Sláðu inn 5 tölu af 7: "))
        tala_6 = int(input("Sláðu inn 6 tölu af 7: "))
        tala_7 = int(input("Sláðu inn 7 tölu af 7: "))#bið um 7 tölur

        for i in range(1):
            talnalisti.append(tala_1)
            talnalisti.append(tala_2)
            talnalisti.append(tala_3)
            talnalisti.append(tala_4)
            talnalisti.append(tala_5)
            talnalisti.append(tala_6)
            talnalisti.append(tala_7)#set eina tölu í einu inn í listann

        print("\nHæsta tala listans er: %s" % (max(talnalisti)))#prenta hæstu töluna í listanum
        print("Lægsta tala listans er: %s" % (min(talnalisti)))#prenta lægstu töluna í listanum
        medaltal = (talnalisti[0] + talnalisti[1] + talnalisti[2] + talnalisti[3] + talnalisti[4] + talnalisti[5] + talnalisti[6]) / 7#reikna meðaltal
        print("Meðaltal talnana er: %s" % (medaltal))#prenta meðaltal
        summa = talnalisti[0] + talnalisti[1] + talnalisti[2] + talnalisti[3] + talnalisti[4] + talnalisti[5] + talnalisti[6]#reikna summu
        print("Summa talnana er: %s" % (summa))#prenta summu
        talnalisti.sort()#sortera listann
        print("\nTölurnar raðaðar eftir stærð: %s" % talnalisti)#prenta sorteraðann listann
        print("\nTölurnar prentaðar með for lykkju:")
        for number in talnalisti:
            print(number, end="; ")#prenta með forlykkju og ;
        print("\n")
        count = 0#bý til teljara
        for number in talnalisti:
            if number <= 50.5:
                print(number, "er lægri eða jafn há 50,5")
                count += 1#bætist 1 í teljarann ef tala er lægri en 50,5
        print("\nÞað eru %s tölur lægri eða jafn og 50,5" % count)

    #liður2
    if valkostur == 2:#liður 2 er valinn
        randtolur = []#bý til tómann lista
        for i in range(70):
            tala = random.randrange(1,500)#70 tölur 1-500
            randtolur.append(tala)#set í listann
        print(randtolur[0:4])
        print(randtolur[4:8])
        print(randtolur[8:12])
        print(randtolur[12:16])
        print(randtolur[16:20])
        print(randtolur[20:24])
        print(randtolur[24:28])
        print(randtolur[28:32])
        print(randtolur[32:36])
        print(randtolur[36:40])
        print(randtolur[40:44])
        print(randtolur[44:48])
        print(randtolur[48:52])
        print(randtolur[52:56])
        print(randtolur[56:60])
        print(randtolur[60:64])
        print(randtolur[64:68])
        print(randtolur[68:70])#prenta 4 í dalk allar tölurnar
        print("\nHæsta talan: %s" % (max(randtolur)))#prenta hæstu töluna
        print("Lægsta talan: %s" % (min(randtolur)))#prenta lægstu töluna
        print("\n")

        randtolur.reverse()#listanum snúinn við
        print(randtolur[0:6])
        print(randtolur[6:12])
        print(randtolur[12:18])
        print(randtolur[18:24])
        print(randtolur[24:30])
        print(randtolur[30:36])
        print(randtolur[36:42])
        print(randtolur[42:48])
        print(randtolur[48:54])
        print(randtolur[54:60])
        print(randtolur[60:66])
        print(randtolur[66:70])#prenta 6 i dalki allan listann

        undircount = 0#teljari fyrir undir 250
        for number in randtolur:
            if number <= 250:
                undircount += 1#+1 hvert skipti sem for lykkjan finnur tölu undir 250
        yfircount = 0#teljari fyrir yfir 250
        for number in randtolur:
            if number >= 251:
                yfircount += 1#+1 hvert skipti sem for lykkjan finnur tölu yfir 250
        print("\nTölur á bilinu 1-250: %s" % undircount)
        print("Tölur á bilinu 251-500: %s" % yfircount)#prenta niðurstöður
    #Liður3
    if valkostur == 3:#verkefni 3 valið
        nafnalisti = []#tómur listi búinn til
        nafn_1 = input("Sláðu inn fyrsta nafnið: ")
        nafn_2 = input("Sláðu inn annað nafnið: ")
        nafn_3 = input("Sláðu inn þriðja nafnið: ")
        nafn_4 = input("Sláðu inn fjórða nafnið: ")
        nafn_5 = input("Sláðu inn fimmta nafnið: ")#bið um 5 nöfn
        for i in range(1):
            nafnalisti.append(nafn_1)
            nafnalisti.append(nafn_2)
            nafnalisti.append(nafn_3)
            nafnalisti.append(nafn_4)
            nafnalisti.append(nafn_5)#bæti i listann ritt í einu
    #valmynd í lið 3

        svar = 1
        while svar == 1:
            print("\n1.Birta nöfn óraðað")
            print("2.Raða nöfnunum í stafrósröð")
            print("3.Raða nöfnum í öfugða stafróstöð röð")
            print("4.Birta eitt nafn eftir því hvaða númer 1-5 er valið")
            print("5.Hætta")
            val_1 = int(input("Velu lið: "))#valmynd
            #1
            if val_1 == 1:
                print("Listinn óraðaður: %s" % nafnalisti)#óraðaður listi

            #2
            if val_1 == 2:
                nafnalisti.sort()
                print("Listinn í stafrósröð: %s" % nafnalisti)#sorteraður listi

            #3
            if val_1 == 3:
                nafnalisti.sort()
                nafnalisti.reverse()
                print("Listinn í öfugði stafsósröð: %s" % nafnalisti)#öfugður sorteraður listi

            #4
            if val_1 == 4:
                val_3 = int(input("Veldu nafn eftir númeri 1-5: "))
                if val_3 == 1:
                    print("Nafn 1: %s" % nafnalisti[0])
                if val_3 == 2:
                    print("Nafn 2: %s" % nafnalisti[1])
                if val_3 == 3:
                    print("Nafn 3: %s" % nafnalisti[2])
                if val_3 == 4:
                    print("Nafn 4: %s" % nafnalisti[3])
                if val_3 == 5:
                    print("Nafn 5: %s" % nafnalisti(4))#notandi velur nafn sem hann vil sjá
            #5
            if val_1 == 5:
                break#hættir í 3

    #liður4
    if valkostur == 4:#4 er valið
        teningalisti = []#Tómur listi
        tala1 = 0
        tala2 = 0
        tala3 = 0
        tala4 = 0
        tala5 = 0
        tala6 = 0#sex teljarar
        oft = int(input("Hversu oft viltu kasta teningnum? "))#bið um teningakast
        for i in range(oft):#for lykkja keyrir jafn oft og notandinn slær inn hér að ofan
            teningakast = random.randrange(1,7)#random tölur fra 1-6
            teningalisti.append(teningakast)#bæti í lista
        for number in teningalisti:
            if number == 1:
                tala1 += 1
            if number == 2:
                tala2 += 1
            if number == 3:
                tala3 += 1
            if number == 4:
                tala4 += 1
            if number == 5:
                tala5 += 1
            if number == 6:
                tala6 += 1#counterarnir fá tölurnar
        print("Talan 1 kom: %s sinnum" % tala1)
        print("Talan 2 kom: %s sinnum" % tala2)
        print("Talan 3 kom: %s sinnum" % tala3)
        print("Talan 4 kom: %s sinnum" % tala4)
        print("Talan 5 kom: %s sinnum" % tala5)
        print("Talan 6 kom: %s sinnum" % tala6)#prenta hversu oft hver tala kom fyrir

        if tala1 > tala2 and tala1 > tala3 and tala1 > tala4 and tala1 > tala5 and tala1 > tala6:
            print("\nTalan 1 Kom oftast fyrir")
        if tala2 > tala1 and tala2 > tala3 and tala2 > tala4 and tala2 > tala5 and tala2 > tala6:
            print("\nTalan 2 kom oftast fyrir")
        if tala3 > tala1 and tala3 > tala2 and tala3 > tala4 and tala3 > tala5 and tala3 > tala6:
            print("\nTalan 3 kom oftast fyrir")
        if tala4 > tala2 and tala4 > tala3 and tala4 > tala1 and tala4 > tala5 and tala4 > tala6:
            print("\nTalan 4 kom oftast fyrir")
        if tala5 > tala2 and tala5 > tala3 and tala5 > tala4 and tala5 > tala1 and tala5 > tala6:
            print("\nTalan 5 kom oftast fyrir")
        if tala6 > tala2 and tala6 > tala3 and tala6 > tala4 and tala6 > tala5 and tala6 > tala1:#finnur hvaða tala kemur oftast fyrir
            print("\nTalan 6 kom oftast fyrir")
        #pása fyrir heilann----------------------------------------------------------------------
        if tala1 < tala2 and tala1 < tala3 and tala1 < tala4 and tala1 < tala5 and tala1 < tala6:
            print("\nTalan 1 kom sjaldnast fyrir")
        if tala2 < tala1 and tala2 < tala3 and tala2 < tala4 and tala2 < tala5 and tala2 < tala6:
            print("\nTalan 2 kom sjaldnast fyrir")
        if tala3 < tala2 and tala3 < tala1 and tala3 < tala4 and tala3 < tala5 and tala3 < tala6:
            print("\nTalan 3 kom sjaldnast fyrir")
        if tala4 < tala2 and tala4 < tala3 and tala4 < tala1 and tala4 < tala5 and tala4 < tala6:
            print("\nTalan 4 kom sjaldnast fyrir")
        if tala5 < tala2 and tala5 < tala3 and tala5 < tala4 and tala5 < tala1 and tala5 < tala6:
            print("\nTalan 5 kom sjaldnast fyrir")
        if tala6 < tala2 and tala6 < tala3 and tala6 < tala4 and tala6 < tala5 and tala6 < tala1:#finnur hvaða tala kemur sjaldnast fyrir
            print("\nTalan 6 kom sjaldnast fyrir")

    #liður5
    if valkostur == 5:#liður 5 valinn
        strengjalisti = []#tómur listi
        forritun = int(input("Hversu margir eru skráðir í FOR1TÖ05BU? "))#hversu margir eru skraðir
        for i in range(forritun):#for lykkja eftir því hversu margir eru skraðir
            nafn = input("Nafn nemanda: ")#bið um jafn mörg nöfn og talan er sem eru skraðir
            strengjalisti.append(nafn)#set i listann
        strengjalisti.sort()#sortera listann
        for strengjalisti in strengjalisti:#nota forlykkju til að prenta
            print("\nnafn: %s" % strengjalisti)
    #valkostur 6
    if valkostur == 6:
        break#forrit hættir
