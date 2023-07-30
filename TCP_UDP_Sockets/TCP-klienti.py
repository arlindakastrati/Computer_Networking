#Programimi FIEK Klienti permes protokollit TCP

import socket #Importi i te gjitha moduleve nga libraria socket

serverName = '127.0.0.1' #IP Adresa e localhostit
serverPort = 14000 #NUMRI I PORTIT te serverit
print("Adresa e klientit eshte :",serverName)
print("NR i portit eshte:",serverPort)
print('----------------------------------------------------------------------')
pyetje=input("A deshironi ta nderroni NR e portit(PO ose JO):")
if(pyetje=='PO' or pyetje=='Po' or pyetje=='po' or pyetje=='pO'):
    serverName=input("Shkruaj IP adresen:")
    sP=input("Shkruaj NR e portit:")
    serverPort=int(sP)
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Ky rresht krijon soketin e klientit te quajtur soketi dhe permban dy parametra.
    #Parametri i pare AF_INET-tregon se rrjeti perdore IPv4
    #Parametri i dyte SOCK_STREAM-tregon se soketi eshte i tipit SOCK STREAM qe nenkupton qe oshte TCP soket

    soketi.connect((serverName,serverPort))#Komunikimi mes Klientit dhe Serverit
    #Parametri i metodes connect eshte adresa e anes se komunikimit te Serverit

    print('---------------------------SOKETI TCP_Klienti-------------------------')
    print('Kerkesat e mundshme:\nIP\nNRPORTIT\nNUMERO hapesire Teksti\nANASJELLTAS hapesire Teksti\nPALINDROM hapesire Teksti\nKOHA\nLOJA\nKONVERTO opcioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) hapesire Numri\nGCF hapesire Nr1 hapesire Nr2')
    print('----------------------------------------------------------------------')
    print('Kerkesat shtese:\nPRIM hapesire Numri\nANAGRAM hapesire Teksti1 Teksti2')
    print('----------------------------------------------------------------------')
    kerkesa = input("I/e nderuara klient/e ju sapo jeni lidhur me serverin,ju lutem shkruani kerkesen tuaj: ")


    while True:#unaza e pafundme
        if (kerkesa == ""): #Nese kerkesa eshte ENTER
            soketi.close() #Soketi do te mbyllet
            print('Lidhja me serverin eshte mbyllur') #Lajmerimi qe lidhja me serverin eshte mbyllur
            break
        else:
            #Dergimi i kerkeses tek serveri(gjegjesishte ne localhost me portin qe e kemi percaktuare tek serverPort)
            soketi.sendall(kerkesa.encode())#Default encoding=utf-8
            #Variabla pergjigja nenkupton pergjigjen nga serverin ne baze te kerkesave te parashtruara 
            pergjigjja = soketi.recv(128).decode()#Default decoding=utf-8
            print(pergjigjja) #Printimi i pergjigjes
            kerkesa = input('Ju lutem shkruani kerkesen tuaj: ') 
    soketi.close()

else:
    soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Ky rresht krijon soketin e klientit te quajtur soketi dhe permban dy parametra.
    #Parametri i pare AF_INET-tregon se rrjeti perdore IPv4
    #Parametri i dyte SOCK_STREAM-tregon se soketi eshte i tipit SOCK STREAM qe nenkupton qe oshte TCP soket

    soketi.connect((serverName,serverPort))#Komunikimi mes Klientit dhe Serverit
    #Parametri i metodes connect eshte adresa e anes se komunikimit te Serverit

    print('---------------------------SOKETI TCP_Klienti-------------------------')
    print('Kerkesat e mundshme:\nIP\nNRPORTIT\nNUMERO hapesire Teksti\nANASJELLTAS hapesire Teksti\nPALINDROM hapesire Teksti\nKOHA\nLOJA\nKONVERTO opcioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) hapesire Numri\nGCF hapesire Nr1 hapesire Nr2')
    print('----------------------------------------------------------------------')
    print('Kerkesat shtese:\nPRIM hapesire Numri\nANAGRAM hapesire Teksti1 Teksti2')
    print('----------------------------------------------------------------------')
    kerkesa = input("I/e nderuara klient/e ju sapo jeni lidhur me serverin,ju lutem shkruani kerkesen tuaj: ")


    while True:#unaza e pafundme
        if (kerkesa == ""): #Nese kerkesa eshte ENTER
            soketi.close() #Soketi do te mbyllet
            print('Lidhja me serverin eshte mbyllur') #Lajmerimi qe lidhja me serverin eshte mbyllur
            break
        else:
            #Dergimi i kerkeses tek serveri(gjegjesishte ne localhost me portin qe e kemi percaktuare tek serverPort)
            soketi.sendall(kerkesa.encode())#Default encoding=utf-8
            #Variabla pergjigja nenkupton pergjigjen nga serverin ne baze te kerkesave te parashtruara 
            pergjigjja = soketi.recv(128).decode()#Default decoding=utf-8
            print(pergjigjja) #Printimi i pergjigjes
            kerkesa = input('Ju lutem shkruani kerkesen tuaj: ') 
    soketi.close()