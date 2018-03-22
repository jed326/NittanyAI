import re

#file must exist
textfile = open('luckComments.txt','r', encoding = 'latin-1')
print("*****************************************")
regex = re.compile("<.*?>")
birthday = "BIRTHDAY"
spotify = "SPOTIFY"

#file must exist
newfile = open("cuylernew.txt","w", encoding = 'latin-1')
for line in textfile:
    line = line.upper()
    line = re.sub(regex,'',line)
    if (line.find(birthday) == -1 and line.find(spotify) == -1):
        newfile.write(line)
newfile.close()
    
    
    
textfile.close()
    
