#in tamil, the alphabets are catagorized in 3 types as Vallinam, Mellinam and Idaiyinam
#linguistics research proves that Vallinam are the most used and Mellinam are the least used characters. 
#Idaiyinam characters count is always between Vallinam and Mellinam counts
#study by researchers, proves that this structure is has not changed from Ancient Tamil text to modern newspapers

f=open("1.txt", encoding="utf8") #1.txt is the name of the file; add the path and filename
t=f.read()
vali=0              #count of valinam occurance 
meli=0              #count of melinam occurance
idai=0              #count of idaiyinam occurance
list ={}            #a dictionary type variable, used to store the list of characters that occur in the text
                    #we use dictionary to avoid duplicates
                    #this dictionary contains the characters as key and their count as variables
valinam=["க", "ச", "ட", "த","ப","ற"]                #list of valinam characters
melinam=["ங", "ஞ","ண", "ந", "ம", "ன"]            #list of melinam characters
idaiyinam=["ய", "ர", "ல", "வ", "ழ", "ள"]           #list of idaiyinam characters

#the below for loop counts one character at a time incrementally, till the end of the document
for i in t:
    try:
        list[i]=list[i]+1         #increments the count of a character that already exists in the dictionary 
    except:
        list[i]=1                 #when new character occur for the 1st time, its added to the dictionary and the count is set to 1

for i in sorted(list):
    print(i,",",list[i])          #prints the key(tamil characters) and value(count of their occurance)

#below loop counts the total occurance of the valinam characters
for j in list:
    if j in valinam:
        vali=vali+list[j]
    if j in melinam:
        meli = meli +list[j]
    if j in idaiyinam:
        idai = idai+list[j]
print("வல்லினம் count", vali)
print("இடையினம் count", idai)
print("மெல்லினம் count", meli)
