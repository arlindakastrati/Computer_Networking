#Programimi FIEK Serveri permes protokollit UDP

#Importimi i librarive te nevojshme 
import socket
from datetime import datetime
import random
import math
import threading
import calendar

server_name = 'localhost' #IP Adresa e localhostit
server_port = 14000 #NUMRI I PORTIT te serverit


soketiS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#Ky rresht krijon soketin e serverit te quajtur serverS dhe permban dy parametra.
#Parametri i pare AF_INET-tregon se rrjeti perdore IPv4
#Parametri i dyte SOCK_STREAM-tregon se soketi eshte i tipit SOCK DGRAM qe nenkupton qe oshte UDP soket
soketiS.bind((server_name, server_port))#Percaktimi i serverName dhe serverPort per lidhje
print('Serveri eshte startuar ne localhost ne portin ' + str(server_port))
print('----------------------------UDP_Serveri--------------------------')

print('Server eshte duke punuar dhe eshte duke pritur per ndonje kerkese!')

#Funksioni IP
def IP():
    return socket.gethostbyname(server_name)
#Funksioni NRPORTIT
def NRPORTIT():
    return str(address[1])
#Funksioni NUMERO 
def NUMERO(Teksti):
    teksti=str(Teksti)
    zanoret=0
    bashketingelloret=0
    listazanoreve =('a','e','ë','i','o','u','y','A','E','Ë','I','O','U','Y' )
    listabashketingelloreve =('b','c','ç','d','dh','f','g','gj','h','j','k','l','ll','m','n','nj','p','q','r','rr','s','sh','t','th','v','x','xh','z','zh',
        'B','C','Ç','D','Dh','F','G','Gj','H','J','K','L','Ll','M','N','Nj','P','Q','R','Rr','S','Sh','T','Th','V','X','Xh','Z','Zh')
    for i in range(0,len(Teksti)):
        if Teksti[i] in listazanoreve:
            zanoret=zanoret+1;#numeruesi i zanoreve rritet per 1 
        elif Teksti[i] in listabashketingelloreve :
            bashketingelloret=bashketingelloret+1 #numeruesi i bashketingelloreve rritet per 1
    x=str(zanoret)
    z=str(bashketingelloret)  
    return str("Teksti ka "+x +" zanore dhe " +z +" bashketingellore.")
#Funksioni ANASJELLTAS
def ANASJELLTAS(Teksti):
    return Teksti[::-1]
#Funksioni PALINDROM
def PALINDROM(Teksti):
    if Teksti==Teksti[::-1]:
        return ("Teksti i dhene eshte palindrome.")
    else:
        return("Teksti i dhene nuk eshte palindrome.")
#Funksioni KOHA
def KOHA():
    kohatani=datetime.now()
    return (kohatani.strftime("%m.%d.%Y %H:%M:%S %p") )
#Funksioni LOJA
def LOJA():
    rendomlista = random.sample(range(1, 35), 5)
    listasortuar = []
    listasortuar = sorted(rendomlista)
    nrsortuar=str(listasortuar)
    return str('p.sh ' +nrsortuar+' 5 numra te rastesishem nga 35.')
#Funksioni GCF
def GCF (Nr1,Nr2):
    x=math.gcd(Nr1,Nr2)
    return str(x)

    
#Funksioni KONVERTO
def KONVERTO(opcioni,Numri):
    if opcioni=='cmNeInch':
        rez = Numri/2.54
    elif opcioni=='inchNeCm':
        rez = 2.54*Numri
    elif opcioni=='kmNeMiles':
        rez = Numri*0.621371
    elif opcioni =='mileNeKm':
        rez = Numri*1.60934
    else:
        rez='Gabim'
    return str(round(rez,2))#Rrumbullakesimi i rez me vetem dy numra pas presjes

#Funksioni PRIM
def PRIM(Num1):
   if Num1 <= 1 or Num1 % 1 > 0:
      return False
   for i in range(2, Num1//2):
      if Num1 % i == 0:
         return False
   return True
#Funksioni ANAGRAM
def ANAGRAM(Teksti1,Teksti2):
    Teksti1=Teksti1.lower()
    Teksti2=Teksti2.lower()
    if(len(Teksti1)==len(Teksti2)):
        sortimiTeksti1=sorted(Teksti1)
        sortimiTeksti2=sorted(Teksti2)
        if(sortimiTeksti1 == sortimiTeksti2):
           return (Teksti1 + " dhe "+Teksti2+" jane anagrame.")
        else:
           return (Teksti1 + " dhe "+Teksti2+" nuk jane anagrame.")
    else:
        return (Teksti1 + " dhe "+Teksti2+" nuk jane anagrame.")
    
    
def ThreadUDP(input, address):
    try:
        pergjigjjja = input.decode()
    except socket.error:
        print("Nuk jane derguar te dhenat ne server!!")
    vargu = str(pergjigjjja).rsplit(" ") #Ndani vargun, duke perdorur hapesiren-space
    i = ""
    gjatesiaevargut = len(vargu)
    for j in range(1, gjatesiaevargut):
        i += vargu[j]
        if(j != gjatesiaevargut):
             i += " "
    if not pergjigjjja:
        return
    elif(vargu[0]=="IP"):
        pergjigjjja = "IP adresa e klientit është : " + IP()
    elif(vargu[0]=="NRPORTIT"):
        pergjigjjja = "Klienti eshte duke perdorur portin " + NRPORTIT()
    elif(vargu[0]=="NUMERO"):
        try:
            pergjigjjja = str(NUMERO(i)) 
        except:
            pergjigjjja = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
    elif(vargu[0]=="ANASJELLTAS"):
        try:
            pergjigjjja = str(ANASJELLTAS(i))
        except:
            pergjigjjja = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
    elif(vargu[0]=="PALINDROM"):
        try:
            pergjigjjja = str(PALINDROM(i))
        except:
            pergjigjjja = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
    elif(vargu[0]=="KOHA"):
        pergjigjjja = KOHA()
    elif(vargu[0]=="LOJA"):
        pergjigjjja= LOJA()
    elif (vargu[0]=="PRIM"):
        try:
            Numri1=int(vargu[1])
            pergjigjjja = str(PRIM(Numri1))
        except:
            pergjigjjja = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
    elif (vargu[0] == "GCF"):
        try:
            vlera1 = int(vargu[1])
            vlera2 = int(vargu[2])
            pergjigjjja= str(GCF(vlera1, vlera2))
        except:
            pergjigjjja = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
    elif(vargu[0]=="KONVERTO"):
        try:
            numri = float(vargu[2])
            pergjigjjja = str(KONVERTO(vargu[1], numri))
        except:
            pergjigjjja = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
    elif(vargu[0]=="ANAGRAM"):
        try:
            Teksti1=str(vargu[1])
            Teksti2=str(vargu[2])
            pergjigjjja=ANAGRAM(Teksti1,Teksti2)
        except:
            pergjigjjja = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
    else:
        pergjigjjja = "Serveri nuk mund te jep pergjigje per kete kerkese!!"
    soketiS.sendto(pergjigjjja.encode(),address)
    

while True:
    print('-----------------------------------------------------------------')
    pergjigjjja, address = soketiS.recvfrom(128)#Kerkesa,kontollimi i bajtave te mesazhit varesisht kerkeses dhe procesimi i tyre 
    print('Klienti eshte lidhur me server %s ne portin %s ' %address)
    print('Kerkesa nga klienti: ' + str(pergjigjjja.decode('utf-8')))
    threading._start_new_thread(ThreadUDP,(pergjigjjja,address,))#Krijimi i thredave
soketiS.close()
    
    