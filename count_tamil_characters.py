#in tamil, the alphabets are catagorized in 3 types as Vallinam, Mellinam and Idaiyinam
#linguistics research proves that Vallinam are the most used and Mellinam are the least used characters. 
#Idaiyinam characters count is always between Vallinam and Mellinam counts
#study by researchers, proves that this structure is has not changed from Ancient Tamil text to modern newspapers
list={}
f=open("1.txt", encoding="utf8") #1.txt is the name of the file; add the path and filename
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
