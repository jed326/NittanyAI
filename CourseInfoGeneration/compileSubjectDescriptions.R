#Cuyler Luck, 03/05/2018

setwd("~/Desktop/Official College/PSU '17-'18/GenEdHelper") #setting working directory
library(readxl)
library(glue)


fullCourses<-read_excel("CourseCat.xlsm") #read in data

fullCourses$`Subject Long`<-as.factor(fullCourses$`Subject Long`) #set abbreviations to factor
courseLong<-levels(fullCourses$`Subject Long`) #pull out levels of abbreviations

SubjectList=vector("list",length(courseLong)) #initializes list of same length as number of levels in abbreviations
names(SubjectList)=courseLong

collapsedDescripts=data.frame(course=courseLong,desc=NA) #result dataframe

for(count in 1:length(SubjectList)){ #pull out the descriptions of a subject and collapse them into corresponding row of dataframe
  currentSub=courseLong[count]
  currentDescriptions=fullCourses[fullCourses$`Subject Long`==currentSub,c("Subject Long","Course Number","Course Description")]
  longDescription=collapse(currentDescriptions$`Course Description`,sep=" ")
  collapsedDescripts[count,2]=longDescription
}

write.csv(collapsedDescripts,file="FullDescriptions.csv")
