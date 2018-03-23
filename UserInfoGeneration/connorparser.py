import re

#file must exist
textfile = open('cuyler_posts_accessed.txt','r', encoding = 'latin-1')

message = "message"
story = "story"
photos = re.compile("")
#file must exist
newfile = open("cuylerprocessed.txt","w", encoding = 'latin-1')
for line in textfile:
    
    if (line.find(message) != -1):
        line = line.replace('"message":','')
        newfile.write(line)
  
newfile.close()
    
    
    
textfile.close()
    
