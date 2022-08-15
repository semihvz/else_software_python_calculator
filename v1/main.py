####python console hesap makinesi
import time
import colorama
from colorama import Fore,Back,Style

print("TEK SATIRDA İŞLEM YAPAN KONSOL HESAP MAKİNESİ")
print("EĞER ÇIKMAK İSTERSENİZ 'q' yazınız")
while True:
    print(Fore.RED)
    islem=input("İşlemi giriniz ")

    if islem!="q":

        islemListe=list(islem)
        for i in range(len(islemListe)):
                
                sayi1=0
                sayi2=0
                if islemListe[i]=="+":
                    islemListeTers1=[]
                    islemListeTers2=[]
                    k=-1
                    while True:
                        islemListeTers1.append(islemListe[0:i][k])
                        k=k-1
                    
                        if k==(len(islemListe[0:i])+1)*-1:
                            break
                    k=-1
                    while True:
                        islemListeTers2.append(islemListe[i+1:][k])
                        k=k-1
                        
                        if k==(len(islemListe[i+1:])+1)*-1:
                            break

                    for i in range(len(islemListeTers1)):
                        x=pow(10,i)
                        sayi1=sayi1+int(islemListeTers1[i])*x
                    
                    for i in range(len(islemListeTers2)):
                        x=pow(10,i)
                        sayi2=sayi2+int(islemListeTers2[i])*x
                    print(Fore.BLUE)
                    print(sayi1,"+",sayi2,"=",sayi1+sayi2)

                elif islemListe[i]=="-":
                    islemListeTers1=[]
                    islemListeTers2=[]
                    k=-1
                    while True:
                        islemListeTers1.append(islemListe[0:i][k])
                        k=k-1
                    
                        if k==(len(islemListe[0:i])+1)*-1:
                            break
                    k=-1
                    while True:
                        islemListeTers2.append(islemListe[i+1:][k])
                        k=k-1
                        
                        if k==(len(islemListe[i+1:])+1)*-1:
                            break

                    for i in range(len(islemListeTers1)):
                        x=pow(10,i)
                        sayi1=sayi1+int(islemListeTers1[i])*x
                    
                    for i in range(len(islemListeTers2)):
                        x=pow(10,i)
                        sayi2=sayi2+int(islemListeTers2[i])*x
                    print(Fore.YELLOW)
                    print(sayi1,"-",sayi2,"=",sayi1-sayi2)

                elif islemListe[i]=="*":
                    islemListeTers1=[]
                    islemListeTers2=[]
                    k=-1
                    while True:
                        islemListeTers1.append(islemListe[0:i][k])
                        k=k-1
                    
                        if k==(len(islemListe[0:i])+1)*-1:
                            break
                    k=-1
                    while True:
                        islemListeTers2.append(islemListe[i+1:][k])
                        k=k-1
                        
                        if k==(len(islemListe[i+1:])+1)*-1:
                            break

                    for i in range(len(islemListeTers1)):
                        x=pow(10,i)
                        sayi1=sayi1+int(islemListeTers1[i])*x
                    
                    for i in range(len(islemListeTers2)):
                        x=pow(10,i)
                        sayi2=sayi2+int(islemListeTers2[i])*x
                    print(Fore.WHITE)
                    print(sayi1,"*",sayi2,"=",sayi1*sayi2)

                elif islemListe[i]=="/":
                    islemListeTers1=[]
                    islemListeTers2=[]
                    k=-1
                    while True:
                        islemListeTers1.append(islemListe[0:i][k])
                        k=k-1
                    
                        if k==(len(islemListe[0:i])+1)*-1:
                            break
                    k=-1
                    while True:
                        islemListeTers2.append(islemListe[i+1:][k])
                        k=k-1
                        
                        if k==(len(islemListe[i+1:])+1)*-1:
                            break

                    for i in range(len(islemListeTers1)):
                        x=pow(10,i)
                        sayi1=sayi1+int(islemListeTers1[i])*x
                    
                    for i in range(len(islemListeTers2)):
                        x=pow(10,i)
                        sayi2=sayi2+int(islemListeTers2[i])*x
                    print(Fore.GREEN)
                    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
                elif islemListe[i]=="%":
                    islemListeTers1=[]
                    islemListeTers2=[]
                    k=-1
                    while True:
                        islemListeTers1.append(islemListe[0:i][k])
                        k=k-1
                    
                        if k==(len(islemListe[0:i])+1)*-1:
                            break
                    k=-1
                    while True:
                        islemListeTers2.append(islemListe[i+1:][k])
                        k=k-1
                        
                        if k==(len(islemListe[i+1:])+1)*-1:
                            break

                    for i in range(len(islemListeTers1)):
                        x=pow(10,i)
                        sayi1=sayi1+int(islemListeTers1[i])*x
                    
                    for i in range(len(islemListeTers2)):
                        x=pow(10,i)
                        sayi2=sayi2+int(islemListeTers2[i])*x
                    print(Fore.GREEN)
                    print(sayi1,"%",sayi2,"=",sayi1%sayi2)
                elif islemListe[i]=="ü":
                    islemListeTers1=[]
                    islemListeTers2=[]
                    k=-1
                    while True:
                        islemListeTers1.append(islemListe[0:i][k])
                        k=k-1
                    
                        if k==(len(islemListe[0:i])+1)*-1:
                            break
                    k=-1
                    while True:
                        islemListeTers2.append(islemListe[i+1:][k])
                        k=k-1
                        
                        if k==(len(islemListe[i+1:])+1)*-1:
                            break

                    for i in range(len(islemListeTers1)):
                        x=pow(10,i)
                        sayi1=sayi1+int(islemListeTers1[i])*x
                    
                    for i in range(len(islemListeTers2)):
                        x=pow(10,i)
                        sayi2=sayi2+int(islemListeTers2[i])*x
                    print(Fore.GREEN)
                    print(sayi1,"üssü",sayi2,"=",pow( sayi1, sayi2))
                
    elif islem=="q":
        print("HOŞÇAKALIN TEKRAR GÖRÜŞMEK ÜZERE")
        
        time.sleep(1)
        break
