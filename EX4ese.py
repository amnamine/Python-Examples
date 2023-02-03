def calcul(ch,cr):
    ch= input("donner une chaine de charactere")
    cr= input("donner une chaine de charactere a rajouter")
    lc=len(ch)
    nch=ch[0]
    i=1
    while i<lc:
        nch=nch+cr+ch[i]
        i=i+1     
    return nch    
   
print(calcul("a","a"))  