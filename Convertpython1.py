import numpy as np
import matplotlib.pyplot as plt
import math as mt

d = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(d)

f=900
Hb=30
Hm=2

#Okumura-Hata
#Grande ville

AHm=3.2*((mt.log10(11.75*Hm))**2)-4.97
Ls=69.55+26.16*mt.log10(f)-13.82*mt.log10(Hb)-AHm+(44.9-6.55*mt.log10(Hb))*mt.log10(d)
plt.subplot(3, 1, 1)
plt.plot(Ls)
plt.title("Okumura-Hata (Grande ville)")
plt.show()

#Ville petite et moyenne
AHmp=((1.11*mt.log10(f)-0.7)*Hm)-((1.56*mt.log10(f))-0.8)
Lsp=69.55+26.16*mt.log10(f)-13.82*mt.log10(Hb)-AHmp+(44.9-6.55*mt.log10(Hb))*mt.log10(d);
plt.subplot(3,1,2)
plt.plot(Lsp)
plt.title("Okumura-Hata (Ville petite et moyenne)")
plt.show()

#espace-libre
Ls=92.4+20*mt.log10(d)+20*mt.log10(d)
plt.subplot(3,1,3)
plt.plot(Ls)
plt.title("Espace libre")
plt.show()

#d=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]