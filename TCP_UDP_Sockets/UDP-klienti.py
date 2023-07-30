#Programimi FIEK Klienti permes protokollit UDP

import socket #Importi i te gjitha moduleve nga libraria socket

server_name = 'localhost'#IP Adresa e localhostit
server_port = 14000 #NUMRI I PORTIT te serverit
print("Adresa e klientit eshte :",server_name)
print("NR i portit eshte:",server_port)
print('----------------------------------------------------------------------')
pyetje=input("A deshironi ta nderroni NR e portit(PO ose JO):")
if(pyetje=='PO' or pyetje=='Po' or pyetje=='po' or pyetje=='pO'):
    server_name=input("Shkruaj IP adresen:")
    sP=input("Shkruaj NR e portit:")
    server_port=int(sP)

    soketiK = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#Ky rresht krijon soketin e klientit te quajtur soketiK dhe permban dy parametra.
    #Parametri i pare AF_INET-tregon se rrjeti perdore IPv4
    #Parametri i dyte SOCK_STREAM-tregon se soketi eshte i tipit SOCK DGRAM qe nenkupton qe oshte UDP soket

    print('---------------------------SOKETI UDP_Klienti-------------------------')
    print('Kerkesat e mundshme:\nIP\nNRPORTIT\nNUMERO hapesire Teksti\nANASJELLTAS hapesire Teksti\nPALINDROM hapesire Teksti\nKOHA\nLOJA\nKONVERTO opcioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) hapesire Numri\nGCF hapesire Nr1 hapesire Nr2')
    print('----------------------------------------------------------------------')
    print('Kerkesat shtese:\nPRIM hapesire Numri\nANAGRAM hapesire Teksti1 Teksti2')
    print('----------------------------------------------------------------------')
    kerkesa = input("I/e nderuara klient/e ju sapo jeni lidhur me serverin,ju lutem shkruani kerkesen tuaj: ")


    #Dergimi i kerkeses tek serveri(gjegjesishte ne localhost me portin qe e kemi percaktuare tek serverPort)
    soketiK.sendto(kerkesa.encode(), (server_name, server_port))
    pergjigjja = soketiK.recv(128).decode()#Default decoding=utf-8
    print(pergjigjja) #Printimi i pergjigjes

    soketiK.close()
else:
    soketiK = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#Ky rresht krijon soketin e klientit te quajtur soketiK dhe permban dy parametra.
    #Parametri i pare AF_INET-tregon se rrjeti perdore IPv4
    #Parametri i dyte SOCK_STREAM-tregon se soketi eshte i tipit SOCK DGRAM qe nenkupton qe oshte UDP soket

    print('---------------------------SOKETI UDP_Klienti-------------------------')
    print('Kerkesat e mundshme:\nIP\nNRPORTIT\nNUMERO hapesire Teksti\nANASJELLTAS hapesire Teksti\nPALINDROM hapesire Teksti\nKOHA\nLOJA\nKONVERTO opcioni(cmNeInch,inchNeCm,kmNeMiles,mileNeKm) hapesire Numri\nGCF hapesire Nr1 hapesire Nr2')
    print('----------------------------------------------------------------------')
    print('Kerkesat shtese:\nPRIM hapesire Numri\nANAGRAM hapesire Teksti1 Teksti2')
    print('----------------------------------------------------------------------')
    kerkesa = input("I/e nderuara klient/e ju sapo jeni lidhur me serverin,ju lutem shkruani kerkesen tuaj: ")


    #Dergimi i kerkeses tek serveri(gjegjesishte ne localhost me portin qe e kemi percaktuare tek serverPort)
    soketiK.sendto(kerkesa.encode(), (server_name, server_port))
    pergjigjja = soketiK.recv(128).decode()#Default decoding=utf-8
    print(pergjigjja) #Printimi i pergjigjes

    soketiK.close()

