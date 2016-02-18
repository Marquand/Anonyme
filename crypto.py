#!/usr/bin/python3.5
# -*- coding: Latin-1 -*-
import math
import string
import re
import encodings

print("Bienvenue sur mon crypter/decrypter de message,")
print("vous devez partagé une clefs avec un destinataire.")
print("Vous rentrez 2 nombres pour un chiffrement sécurisé retenez les")
print("c'est important.")
print("")
a=int(input("{1/4} Rentrez votre 1er clef :"));
b=int(input("{2/3}-Rentrez votre 2ème clef :"));
while a-b<0 or a-b==0:
    print("Vos clefs ne sont pas accepté");
    a=int(input("{1/4} Rentrez votre 1er clef :"));
    b=int(input("{2/4} Rentrez votre 2ème clef :"));

tab=[" ","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","à","ç","£",]
count=0
#for i in range(0,len(tab)):
#    count=count+1
#    print(count)
#    print(tab[i])
def code():
    message = str(input("{3/3}-Rentrez-votre message : "));
    message.replace('"', "'")
    for c in message :
        tab=[" ","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","à","ç","£"]
        for i in range(0,len(tab)):
            if tab[i]==c:
                r=(i+(a-b)*2)%95 #Clef de crytage.
                #print(r)
                res = print(tab[r],end="");
print("Rappellez-vous, vos clefs !")

def decode():
    message = str(input("{3/3}-Rentrez-votre message : "));
    for c in message :
        tab=[" ","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~","à","ç","£"]
        for i in range(0,len(tab)):
            if tab[i]==c:
                s=(a-b)*2%95
                r=(i-(a-b)*2)%95
                print(tab[r],end="")
                print(r)
def clef():
    a=0
    a=int(input("{1/3}-Rentrez votre 1er clef :"));
    b=int(input("{2/3}-Rentrez votre 2ème clef :"));
print("Maintenant vous devez choisir une option")
print("- Vous pouvez codé un message en tapant : code()")
print("- Vous pouvez décodé un message en tapant : decode()")
print("- Vous pouvez retapé vos clefs : clef()")
