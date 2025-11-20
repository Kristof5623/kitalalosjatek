import random
print("")
print("Egy kitalálos játékot játszunk ahol most neked ki kell találd a számot amire gondoltam!")
print("Elöször mond meg milyen modban szeretnél játszani??")
print("1. veryeasy (1,10)")
print("2. easy (1,100)")
print("3. normal (1,1.000)")
print("4. hard (1,10.000)")
print("5. veryhard (1,100.000)")
print("6. insane (1,1.000.000)")


mod=int(input("Add meg azt a számát ameik modban szeretnél játsazni!:"))
while (mod>6):
    print("helytelen nehézségi szint megadás")
    mod=int(input("Add meg azt a számát ameik modban szeretnél játsazni!:"))

while (mod<1):
    print("helytelen nehézségi szint megadás")
    mod=int(input("Add meg azt a számát ameik modban szeretnél játsazni!:"))
    
print("Rendben akkor",mod,"-es/as/ös/os nehézségi modban játzsól!")

if (mod==1):
    try:
        veryeasy=random.randint (1,10)

        vetipp=int(input("Írd be a tipped (1,10) közt:"))

        vedb=1

        while (veryeasy!=vetipp):
            if (vetipp<veryeasy):
                print("A(z)",vedb,". probád nem talát,",end="")
                vetipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",vedb,". probád nem talát,",end="")
                vetipp=int(input(" a számom kisebb:"))
            vedb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(vedb,". probára!")
    except ValueError:
        vetipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

        while (veryeasy!=vetipp):
            if (vetipp<veryeasy):
                print("A(z)",vedb,". probád nem talát,",end="")
                vetipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",vedb,". probád nem talát,",end="")
                vetipp=int(input(" a számom kisebb:"))
            vedb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(vedb,". probára!")




if (mod==2):
    try:
        easy=random.randint (1,100)

        etipp=int(input("Írd be a tipped (1,100) közt:"))

        edb=1

        while (easy!=etipp):
            if (etipp<easy):
                print("A(z)",edb,". probád nem talát,",end="")
                etipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",edb,". probád nem talát,",end="")
                etipp=int(input(" a számom kisebb:"))
            edb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(edb,". probára!")
    except ValueError:
        etipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

        while (easy!=etipp):
            if (etipp<easy):
                print("A(z)",edb,". probád nem talát,",end="")
                etipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",edb,". probád nem talát,",end="")
                etipp=int(input(" a számom kisebb:"))
            edb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(edb,". probára!")    




if (mod==3):
    try:
        normal=random.randint (1,1000)

        ntipp=int(input("Írd be a tipped (1,1.000) közt:"))

        ndb=1

        while (normal!=ntipp):
            if (ntipp<normal):
                print("A(z)",ndb,". probád nem talát,",end="")
                ntipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",ndb,". probád nem talát,",end="")
                ntipp=int(input(" a számom kisebb:"))
            ndb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(ndb,". probára!")
    except ValueError:
        ntipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

        while (normal!=ntipp):
            if (ntipp<normal):
                print("A(z)",ndb,". probád nem talát,",end="")
                ntipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",ndb,". probád nem talát,",end="")
                ntipp=int(input(" a számom kisebb:"))
            ndb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(ndb,". probára!")



if (mod==4):
    try:
        hard=random.randint (1,10000)

        htipp=int(input("Írd be a tipped (1,10.000) közt:"))

        hdb=1

        while (hard!=htipp):
            if (htipp<hard):
                print("A(z)",hdb,". probád nem talát,",end="")
                htipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",hdb,". probád nem talát,",end="")
                htipp=int(input(" a számom kisebb:"))
            hdb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(hdb,". probára!")
    except ValueError:
        htipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

        while (hard!=htipp):
            if (htipp<hard):
                print("A(z)",hdb,". probád nem talát,",end="")
                htipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",hdb,". probád nem talát,",end="")
                htipp=int(input(" a számom kisebb:"))
            hdb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(hdb,". probára!")



if (mod==5):
    try:
        veryhard=random.randint (1,100000)

        vhtipp=int(input("Írd be a tipped (1,100.000) közt:"))

        vhdb=1

        while (veryhard!=vhtipp):
            if (vhtipp<veryhard):
                print("A(z)",vhdb,". probád nem talát,",end="")
                vhtipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",vhdb,". probád nem talát,",end="")
                vhtipp=int(input(" a számom kisebb:"))
            vhdb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(vhdb,". probára!")
    except ValueError:
        vhtipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

        while (veryhard!=vhtipp):
            if (vhtipp<veryhard):
                print("A(z)",vhdb,". probád nem talát,",end="")
                vhtipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",vhdb,". probád nem talát,",end="")
                vhtipp=int(input(" a számom kisebb:"))
            vhdb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(vhdb,". probára!")



if (mod==6):
    try:
        insane=random.randint (1,1000000)

        itipp=int(input("Írd be a tipped (1,1.000.000) közt:"))

        idb=1

        while (insane!=itipp):
            if (itipp<insane):
                print("A(z)",idb,". probád nem talát,",end="")
                itipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",idb,". probád nem talát,",end="")
                itipp=int(input(" a számom kisebb:"))
            idb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(idb,". probára!")
    except ValueError:
        itipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

        while (insane!=itipp):
            if (itipp<insane):
                print("A(z)",idb,". probád nem talát,",end="")
                itipp=int(input(" a számom nagyobb:"))
            else:
                print("A(z)",idb,". probád nem talát,",end="")
                itipp=int(input(" a számom kisebb:"))
            idb+=1
        print("")
        print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
        print(idb,". probára!")



valasz=input("Szeretnél úrja játszani?? igen/nem:")

if valasz=="igen":

    print("")
    print("Köszöntelek úrja itt!")
    print("Elöször mond meg milyen modban szeretnél játszani??")
    print("1. veryeasy (1,10)")
    print("2. easy (1,100)")
    print("3. normal (1,1.000)")
    print("4. hard (1,10.000)")
    print("5. veryhard (1,100.000)")
    print("6. insane (1,1.000.000)")


    mod=int(input("Add meg azt a számát ameik modban szeretnél játsazni!:"))
    while (mod>6):
        print("helytelen nehézségi szint megadás")
        mod=int(input("Add meg azt a számát ameik modban szeretnél játsazni!:"))
        
    print("Rendben akkor",mod,"-es/as/ös/os nehézségi modban játzsól!")

    if (mod==1):
        try:
            veryeasy=random.randint (1,10)

            vetipp=int(input("Írd be a tipped (1,10) közt:"))

            vedb=1

            while (veryeasy!=vetipp):
                if (vetipp<veryeasy):
                    print("A(z)",vedb,". probád nem talát,",end="")
                    vetipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",vedb,". probád nem talát,",end="")
                    vetipp=int(input(" a számom kisebb:"))
                vedb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(vedb,". probára!")
        except ValueError:
            vetipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

            while (veryeasy!=vetipp):
                if (vetipp<veryeasy):
                    print("A(z)",vedb,". probád nem talát,",end="")
                    vetipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",vedb,". probád nem talát,",end="")
                    vetipp=int(input(" a számom kisebb:"))
                vedb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(vedb,". probára!")




    if (mod==2):
        try:
            easy=random.randint (1,100)

            etipp=int(input("Írd be a tipped (1,100) közt:"))

            edb=1

            while (easy!=etipp):
                if (etipp<easy):
                    print("A(z)",edb,". probád nem talát,",end="")
                    etipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",edb,". probád nem talát,",end="")
                    etipp=int(input(" a számom kisebb:"))
                edb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(edb,". probára!")
        except ValueError:
            etipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

            while (easy!=etipp):
                if (etipp<easy):
                    print("A(z)",edb,". probád nem talát,",end="")
                    etipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",edb,". probád nem talát,",end="")
                    etipp=int(input(" a számom kisebb:"))
                edb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(edb,". probára!")    




    if (mod==3):
        try:
            normal=random.randint (1,1000)

            ntipp=int(input("Írd be a tipped (1,1.000) közt:"))

            ndb=1

            while (normal!=ntipp):
                if (ntipp<normal):
                    print("A(z)",ndb,". probád nem talát,",end="")
                    ntipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",ndb,". probád nem talát,",end="")
                    ntipp=int(input(" a számom kisebb:"))
                ndb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(ndb,". probára!")
        except ValueError:
            ntipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

            while (normal!=ntipp):
                if (ntipp<normal):
                    print("A(z)",ndb,". probád nem talát,",end="")
                    ntipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",ndb,". probád nem talát,",end="")
                    ntipp=int(input(" a számom kisebb:"))
                ndb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(ndb,". probára!")



    if (mod==4):
        try:
            hard=random.randint (1,10000)

            htipp=int(input("Írd be a tipped (1,10.000) közt:"))

            hdb=1

            while (hard!=htipp):
                if (htipp<hard):
                    print("A(z)",hdb,". probád nem talát,",end="")
                    htipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",hdb,". probád nem talát,",end="")
                    htipp=int(input(" a számom kisebb:"))
                hdb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(hdb,". probára!")
        except ValueError:
            htipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

            while (hard!=htipp):
                if (htipp<hard):
                    print("A(z)",hdb,". probád nem talát,",end="")
                    htipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",hdb,". probád nem talát,",end="")
                    htipp=int(input(" a számom kisebb:"))
                hdb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(hdb,". probára!")



    if (mod==5):
        try:
            veryhard=random.randint (1,100000)

            vhtipp=int(input("Írd be a tipped (1,100.000) közt:"))

            vhdb=1

            while (veryhard!=vhtipp):
                if (vhtipp<veryhard):
                    print("A(z)",vhdb,". probád nem talát,",end="")
                    vhtipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",vhdb,". probád nem talát,",end="")
                    vhtipp=int(input(" a számom kisebb:"))
                vhdb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(vhdb,". probára!")
        except ValueError:
            vhtipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

            while (veryhard!=vhtipp):
                if (vhtipp<veryhard):
                    print("A(z)",vhdb,". probád nem talát,",end="")
                    vhtipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",vhdb,". probád nem talát,",end="")
                    vhtipp=int(input(" a számom kisebb:"))
                vhdb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(vhdb,". probára!")



    if (mod==6):
        try:
            insane=random.randint (1,1000000)

            itipp=int(input("Írd be a tipped (1,1.000.000) közt:"))

            idb=1

            while (insane!=itipp):
                if (itipp<insane):
                    print("A(z)",idb,". probád nem talát,",end="")
                    itipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",idb,". probád nem talát,",end="")
                    itipp=int(input(" a számom kisebb:"))
                idb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(idb,". probára!")
        except ValueError:
            itipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

            while (insane!=itipp):
                if (itipp<insane):
                    print("A(z)",idb,". probád nem talát,",end="")
                    itipp=int(input(" a számom nagyobb:"))
                else:
                    print("A(z)",idb,". probád nem talát,",end="")
                    itipp=int(input(" a számom kisebb:"))
                idb+=1
            print("")
            print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
            print(idb,". probára!")


elif valasz=="nem":
    print("Köszönöm hogy játszotál remmélem tetszet!:)")

else:
    print("Nem helyes a választod írj igen-t vagy nem-et!") 

    if valasz=="igen":

        print("")
        print("Köszöntelek úrja itt!")
        print("Elöször mond meg milyen modban szeretnél játszani??")
        print("1. veryeasy (1,10)")
        print("2. easy (1,100)")
        print("3. normal (1,1.000)")
        print("4. hard (1,10.000)")
        print("5. veryhard (1,100.000)")
        print("6. insane (1,1.000.000)")


        mod=int(input("Add meg azt a számát ameik modban szeretnél játsazni!:"))
        while (mod>6):
            print("helytelen nehézségi szint megadás")
            mod=int(input("Add meg azt a számát ameik modban szeretnél játsazni!:"))
            
        print("Rendben akkor",mod,"-es/as/ös/os nehézségi modban játzsól!")

        if (mod==1):
            try:
                veryeasy=random.randint (1,10)

                vetipp=int(input("Írd be a tipped (1,10) közt:"))

                vedb=1

                while (veryeasy!=vetipp):
                    if (vetipp<veryeasy):
                        print("A(z)",vedb,". probád nem talát,",end="")
                        vetipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",vedb,". probád nem talát,",end="")
                        vetipp=int(input(" a számom kisebb:"))
                    vedb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(vedb,". probára!")
            except ValueError:
                vetipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

                while (veryeasy!=vetipp):
                    if (vetipp<veryeasy):
                        print("A(z)",vedb,". probád nem talát,",end="")
                        vetipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",vedb,". probád nem talát,",end="")
                        vetipp=int(input(" a számom kisebb:"))
                    vedb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(vedb,". probára!")




        if (mod==2):
            try:
                easy=random.randint (1,100)

                etipp=int(input("Írd be a tipped (1,100) közt:"))

                edb=1

                while (easy!=etipp):
                    if (etipp<easy):
                        print("A(z)",edb,". probád nem talát,",end="")
                        etipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",edb,". probád nem talát,",end="")
                        etipp=int(input(" a számom kisebb:"))
                    edb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(edb,". probára!")
            except ValueError:
                etipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

                while (easy!=etipp):
                    if (etipp<easy):
                        print("A(z)",edb,". probád nem talát,",end="")
                        etipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",edb,". probád nem talát,",end="")
                        etipp=int(input(" a számom kisebb:"))
                    edb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(edb,". probára!")    




        if (mod==3):
            try:
                normal=random.randint (1,1000)

                ntipp=int(input("Írd be a tipped (1,1.000) közt:"))

                ndb=1

                while (normal!=ntipp):
                    if (ntipp<normal):
                        print("A(z)",ndb,". probád nem talát,",end="")
                        ntipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",ndb,". probád nem talát,",end="")
                        ntipp=int(input(" a számom kisebb:"))
                    ndb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(ndb,". probára!")
            except ValueError:
                ntipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

                while (normal!=ntipp):
                    if (ntipp<normal):
                        print("A(z)",ndb,". probád nem talát,",end="")
                        ntipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",ndb,". probád nem talát,",end="")
                        ntipp=int(input(" a számom kisebb:"))
                    ndb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(ndb,". probára!")



        if (mod==4):
            try:
                hard=random.randint (1,10000)

                htipp=int(input("Írd be a tipped (1,10.000) közt:"))

                hdb=1

                while (hard!=htipp):
                    if (htipp<hard):
                        print("A(z)",hdb,". probád nem talát,",end="")
                        htipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",hdb,". probád nem talát,",end="")
                        htipp=int(input(" a számom kisebb:"))
                    hdb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(hdb,". probára!")
            except ValueError:
                htipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

                while (hard!=htipp):
                    if (htipp<hard):
                        print("A(z)",hdb,". probád nem talát,",end="")
                        htipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",hdb,". probád nem talát,",end="")
                        htipp=int(input(" a számom kisebb:"))
                    hdb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(hdb,". probára!")



        if (mod==5):
            try:
                veryhard=random.randint (1,100000)

                vhtipp=int(input("Írd be a tipped (1,100.000) közt:"))

                vhdb=1

                while (veryhard!=vhtipp):
                    if (vhtipp<veryhard):
                        print("A(z)",vhdb,". probád nem talát,",end="")
                        vhtipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",vhdb,". probád nem talát,",end="")
                        vhtipp=int(input(" a számom kisebb:"))
                    vhdb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(vhdb,". probára!")
            except ValueError:
                vhtipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

                while (veryhard!=vhtipp):
                    if (vhtipp<veryhard):
                        print("A(z)",vhdb,". probád nem talát,",end="")
                        vhtipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",vhdb,". probád nem talát,",end="")
                        vhtipp=int(input(" a számom kisebb:"))
                    vhdb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(vhdb,". probára!")



        if (mod==6):
            try:
                insane=random.randint (1,1000000)

                itipp=int(input("Írd be a tipped (1,1.000.000) közt:"))

                idb=1

                while (insane!=itipp):
                    if (itipp<insane):
                        print("A(z)",idb,". probád nem talát,",end="")
                        itipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",idb,". probád nem talát,",end="")
                        itipp=int(input(" a számom kisebb:"))
                    idb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(idb,". probára!")
            except ValueError:
                itipp=int(input("Amit meg adtál az nem szám valoszinüleg, írd a tipped újra:"))

                while (insane!=itipp):
                    if (itipp<insane):
                        print("A(z)",idb,". probád nem talát,",end="")
                        itipp=int(input(" a számom nagyobb:"))
                    else:
                        print("A(z)",idb,". probád nem talát,",end="")
                        itipp=int(input(" a számom kisebb:"))
                    idb+=1
                print("")
                print("Gratulálok eltaáltad a számmom amire gondoltam ",end="")
                print(idb,". probára!")


    elif valasz=="nem":
        print("Köszönöm hogy játszotál remmélem tetszet!:)")

    else:
        print("Nem helyes a választod írj igen-t vagy nem-et!")

