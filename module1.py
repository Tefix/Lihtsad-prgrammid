from def import *
palgad=[1200,2500,750,395,1200]
inimesed=["a","B","C","D","E"]

while 1:
    try:
        print(
            "1. Lisage kasutajaid\n"
            "2. Kustutage kasutaja\n"
            "3. Leidke k�rgeima tasuga kasutaja\n"
            "4. Leidke madalaima tasuga kasutaja\n"
            "5. Sorteeri kasutajad palga j�rgi\n"
            "6. Leidke sama palgaga kasutajad\n"
            "7. Leidke kasutaja palga j�rgi\n"
            "8. Leidke kasutaja, kelle palk on suurem kui antud palk\n"
            "9. V�lju"
        )
        answer=input("??????? ????????: ")

        if answer == "1":
            kolv=int(input("??????? ??????? ????????????? ?? ?????? ????????: "))
            for i in range(kolv):
                LisaAndmed(palgad, inimesed)
        elif answer=="2":
            KasutaAndmed(palgad, inimesed)
        elif answer=="3":
            SuurPalk(palgad, inimesed)
        elif answer=="4":
            MaadalimPalk(palgad, inimesed)
        elif answer=="5":
            JarjestaPalgad(palgad, inimesed)
        elif answer=="6":
            SamaPalk(palgad, inimesed)
        elif answer=="7":
            foundsalary(palgad, inimesed)
        elif answer=="8":
            inpsalarythan(palgad, inimesed)
        elif answer=="9":
            sortid(palgad, inimesed)
        elif answer=="10":
            break

    except:
        print("Error")
