list={}
f=open("1.txt", encoding="utf8")
t=f.read()
for i in t:
    try:
        list[i]=list[i]+1
    except:
        list[i]=1
for i in sorted(list):
    print(i,",",list[i])

valinam=["க", "ச", "ட", "த","ப","ற"]
melinam=["ங", "ஞ","ண", "ந", "ம", "ன"]
idaiyinam=["ய", "ர", "ல", "வ", "ழ", "ள"]

vali=0
meli=0
idai = 0


for j in list:
    if j in valinam:
        vali=vali+list[j]
    if j in melinam:
        meli = meli +list[j]
    if j in idaiyinam:
        idai = idai+list[j]
print("valinam", vali)
print("melinam", meli)
print("idaiinam", idai)
