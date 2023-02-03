#1
nom = str(input("nom="))
prénom = str(input("prénom="))
note1 = float(input("note1="))
note2 = float(input("note2="))
note3 = float(input("note3="))
#2
moy=(note1+note2+note3)/3
#3
if moy >= 10:
    print ("admi")
else:
    print("ajorne")
#4
def moyenne(note):
    m=0
    for n in note:
        m=m+n
    m=m/3
    if moy >= 10:
        print ("admi")
    else:
        print("ajorne")
note=[note1,note2,note3]
moyenne(note)
    
    
    