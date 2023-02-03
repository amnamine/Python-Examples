import math as mt

Hb=30;
Hm=2;
f=900;
AHm=(3.2*(mt.log10(11.75*Hm**2))-4.97);
Ls=117;
Dmax=10**((Ls-92.4-(20*mt.log10(f*(10**(-3))))/20))
Ls1=171.2;
Dmax1=10**((Ls1-69.55-(26.16*mt.log10(f))+(13.82*mt.log10(Hb))+AHm))/(44.9-(6.55*mt.log10(Hb)))
Ls2=160.35;
Dmax2=10**((Ls2-69.55-(26.16*mt.log10(f))+(13.82*mt.log10(Hb))+AHm))/(44.9-(6.55*mt.log10(Hb)))

print(Dmax)
print(Dmax1)
print(Dmax2)