#Cuyler Luck, 3/23/18

#goes through messy keyword file from IBM Watson and returns all keywords and relevances for each subject separated into individual rows
#output: .csv with course keywords and course relevances in columns

library(readxl)
library(DataComputing)
library(stringr)


#read in data and choose only the columns we want for this script
courseKeywords=read_excel(path="courseKeywords.xlsx")
courseKeywords=select(courseKeywords,c("course","keywords"))

#construct column names for output
coursenames=courseKeywords$course
output=vector(mode="list",length=length(coursenames)*2)
outputItemNames=rep(coursenames,each=2)

#still constucting column names
for(i in seq(1:length(outputItemNames))){
  if(i%%2==1){
    outputItemNames[i]=paste(outputItemNames[i],"_Keywords",sep="")
  }
  else{
    outputItemNames[i]=paste(outputItemNames[i],"_Relevance",sep="")
  }
}

#assign column names to the output columns
names(output)=outputItemNames

#extracting keywords and corresponding relevances for each subject
for(i in seq(1,length(courseKeywords$course))){
  allcurrentKeyRel=stringr::str_extract_all(courseKeywords$keywords[i],"'keyword': [^\\}]*") 
  addToCourseKeywords=NULL
  addToCourseRel=NULL
  for(set in allcurrentKeyRel[[1]]){
    splitted=strsplit(set,split=",")
    keyword=substr(splitted[[1]][1],13,nchar(splitted[[1]][1])-1)
    rel=substr(splitted[[1]][2],15,nchar(splitted[[1]][2])-1)
    addToCourseKeywords=c(addToCourseKeywords,keyword)
    addToCourseRel=c(addToCourseRel,rel)
  }  
  output[[2*i-1]]=addToCourseKeywords
  output[[2*i]]=addToCourseRel
}

#find maxlength of keywords"
maxlength=0
for(i in seq(1,length(output),by=2)){
  if(length(output[[i]])>maxlength){
    maxlength=length(output[[i]])
  }
}

#fill NAs where needed to allow write.csv to work
for(i in seq(1,length(output))){
  if(length(output[[i]])!=maxlength){
    diffToMakeUp=maxlength-length(output[[i]])
    NAtoAdd=rep(NA,diffToMakeUp)
    output[[i]]=c(output[[i]],NAtoAdd)
  }
}

write.csv(output,file="extractedKeywordsAndRelevances.csv")
