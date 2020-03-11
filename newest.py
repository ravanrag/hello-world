#in tamil, the alphabets are catagorized in 3 types as Vallinam, Mellinam and Idaiyinam
#linguistics research proves that Vallinam are the most used and Mellinam are the least used characters.
#Idaiyinam characters count is always between Vallinam and Mellinam counts
#study by researchers, proves that this structure is has not changed from Ancient Tamil text to modern newspapers

f=open("C:/Users/Raghavaraj/PycharmProjects/1st project/1.txt", encoding="utf8")
t=f.read()+"0"
i=t.__len__()
vali=0              #count of valinam occurance
meli=0              #count of melinam occurance
idai=0              #count of idaiyinam occurance
kuril=0             #count of kuril yeluthukal
nedil=0             #count of nedil yeluthukal
dot=0
vow=0

valinam=["க", "ச", "ட", "த","ப","ற"]                #list of valinam characters
melinam=["ங", "ஞ","ண", "ந", "ம", "ன"]            #list of melinam characters
idaiyinam=["ய", "ர", "ல", "வ", "ழ", "ள"]           #list of idaiyinam characters
alp=valinam+melinam+idaiyinam
kuril_yeluthu=["ி","ு","ெ","ொ","அ","இ","உ", "எ", "ஒ"]
nedil_yeluthu=["ா","ீ","ூ","ே","ை","ோ","ௌ","ஆ","ஈ","ஊ","ஏ","ஐ","ஓ","ஔ"]
vowels=["அ","இ","உ", "எ", "ஒ","ஆ","ஈ","ஊ","ஏ","ஐ","ஓ","ஔ"]
mei=["்"]

for j in range (0,i):
    c=j+1
    if c<i:
        if t[j] in valinam:
            vali = vali+1
            if t[c] in alp:
                kuril+=1
        if t[j] in melinam:
            meli=meli+1
            if t[c] in alp:
                kuril+=1
        if t[j] in idaiyinam:
            idai=idai+1
            if t[c] in alp:
                kuril+=1
        if t[j] in kuril_yeluthu:
            kuril=kuril+1
        if t[j] in nedil_yeluthu:
            nedil+=1
        if t[j] in mei:
            dot+=1
        if t[j] in vowels :
            vow+=1
print("உயிரெழுத்து எண்ணிக்கை", vow)
print("மெய்யெழுத்துக்கள் எண்ணிக்கை", dot)
print("வல்லினம் எண்ணிக்கை", vali)
print("இடையினம் எண்ணிக்கை", idai)
print("மெல்லினம் எண்ணிக்கை", meli)
print("குறில் எழுத்துக்கள் எண்ணிக்கை", kuril)
print("நெடில் எழுத்துக்கள் எண்ணிக்கை", nedil)
