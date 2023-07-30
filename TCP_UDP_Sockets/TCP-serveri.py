#Programimi FIEK Serveri permes protokollit TCP

#Importimi i librarive te nevojshme 
import socket
from datetime import datetime
import random
import math
import threading

serverName = '127.0.0.1' #IP Adresa e localhostit
serverPort = 14000 #NUMRI I PORTIT te serverit

serverS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Ky rresht krijon soketin e serverit te quajtur serverS dhe permban dy parametra.
#Parametri i pare AF_INET-tregon se rrjeti perdore IPv4
#Parametri i dyte SOCK_STREAM-tregon se soketi eshte i tipit SOCK STREAM qe nenkupton qe oshte TCP soket
serverS.bind((serverName, serverPort))#Percaktimi i serverName dhe serverPort per lidhje
print('Serveri eshte startuar ne localhost ne portin ' + str(serverPort))
serverS.listen(5) #Serveri pret kerkesat e klientit 

print('----------------------------TCP_Serveri--------------------------')
print('Server eshte duke punuar dhe eshte duke pritur per ndonje kerkese!')

#Funksioni IP
def IP():
    return socket.gethostbyname(serverName)
    #return str(address[0])
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
    for i in range(0,len(teksti)):
        if teksti[i] in listazanoreve:
            zanoret=zanoret+1;#numeruesi i zanoreve rritet per 1 
        elif teksti[i] in listabashketingelloreve :
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
    

def ThreadTCP(connection):
    
    while True:
        try:
            pergjigjjaa = connection.recv(128).decode()
        except socket.error:
            print("Te dhenat nuk jane derguar ne server!!")
            break
        vargu = str(pergjigjjaa).rsplit(" ") #Ndani vargun, duke perdorur hapesiren-space
        i = ""
        gjatesiaevargut = len(vargu)
        for j in range(1, gjatesiaevargut):
            i += vargu[j]
            if(j != gjatesiaevargut):
                i += " "
        if not pergjigjjaa:
            break
        elif(vargu[0]=="IP"):
            pergjigjjaa = "IP adresa e klientit eshte : " + IP()
        elif(vargu[0]=="NRPORTIT"):
            pergjigjjaa = "Klienti eshte duke perdorur portin " + NRPORTIT()
        elif(vargu[0]=="NUMERO"):
            try:
                pergjigjjaa = str(NUMERO(vargu[1])) 
            except:
                pergjigjjaa = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
        elif(vargu[0]=="ANASJELLTAS"):
            try:
                pergjigjjaa = str(ANASJELLTAS(vargu[1]))
            except:
                pergjigjjaa = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
        elif(vargu[0]=="PALINDROM"):
            try:
                pergjigjjaa = str(PALINDROM(vargu[1]))
            except:
                pergjigjjaa = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")

        elif(vargu[0]=="KOHA"):
            pergjigjjaa = KOHA()
        elif(vargu[0]=="LOJA"):
            pergjigjjaa = LOJA()
        elif(vargu[0]=="ANAGRAM"):
            try:
                Teksti1=str(vargu[1])
                Teksti2=str(vargu[2])
                pergjigjjaa = ANAGRAM(Teksti1,Teksti2)
            except:
                pergjigjjaa = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
        elif (vargu[0] == "GCF"):
            try:
                vlera1 = int(vargu[1])
                vlera2 = int(vargu[2])
                pergjigjjaa = str(GCF(vlera1, vlera2))
            except:
                pergjigjjaa = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")

        elif(vargu[0]=="KONVERTO"):
            try:
                numri = float(vargu[2])
                pergjigjjaa = str(KONVERTO(vargu[1], numri))
            except:
                pergjigjjaa = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
        elif (vargu[0]=="PRIM"):
            try:
                Numri1=int(vargu[1])
                pergjigjjaa = str(PRIM(Numri1))
            except:
                pergjigjjaa = str("Kerkesa juaj nuk eshte shkruar ne menyren e duhur.Rishikoni udhezimet e dhena me larte.")
        
        else:
            pergjigjjaa = "Serveri nuk mund te jep pergjigje per kete kerkese!!"
        connection.send(pergjigjjaa.encode())
    connection.close()


while True:
    print('-----------------------------------------------------------------')
    connection, address = serverS.accept()
    print("Serveri është lidhur me klientin me IP Adresë %s, në portin %s" % address)
    threading._start_new_thread(ThreadTCP,(connection,))#Krijimi i thredave
serverS.close()







