
string= """nabila.aaaa / 087810822478
ariefnoob123 / 082114601824
tarissa_mutia_ / 085891385999
suriyasayud
trcod2/085966182953
m.azzam05/087765108040
vianfrzn/08115555427
@jeremiarng / 08172319393
indoadrin/082160954550
am.zariifa/082120921590
freiaz / 081806430764
nabeelmuhammad
kae20ilyasa
s.yasman
82293675579
rafie_bejo/081776532879
132645978/082261300533
scarryanda
daffaabhipraya
line: rafansya05
@nabilrakaiza/085247524076
fikar_adhrevi
pink_evo
diodavis/081285206059
nisrinaannaisha
felitazhr/081218149379
na-62
alviandi8 / 087812279194
vmuhfarhan
radiraf2005/087883440073
zufar280405
farrel3008
farrellzidane
85711429067
1a1n1n1e
preciousaccount/081294772245
mirfakn/081510224557
stevenpks17
niaalw_ / 087734085063
sherwyns2/085342172700
fadhliard/082249070511
thunderzxz / 082110665030

crln_rvlz/089673885149
@_reyhanardian
aileenpop
aliyahnhsa / 081283959362
nisrina_alya / 085381833742
zahra_sabila
mawlaraditya/082230549634
qwertys9
nowweburnit1250
yudaynarif/081315661250
85695081289
himuggles.
emanuella.s/08138227701
hfachri42/081317001778
87775217132
81219917913
Id line: halosayaluthfi
shasi14juni/081315000206
syarfnaila
nayaaary - 085319335740
85813758317
daniel.oke/088902068861
apenih./087731618166
felaza123
venia16_/081281921492
meutiia
sitishofie300605/081377811706
naaaamira/081328288355
rizqyazhr/081294852350"""

ls = string.split("\n")

line = []
whatsapp = []
others = []

for item in ls:
    if item.isnumeric():
        whatsapp.append(item)
    else:
        if item.__contains__("/"):
            line.append(item[0:item.find("/")])
        else:
            others.append(item)

for i in line:
    print(i)
for i in whatsapp:
    print(i)
for i in others:
    print(i)