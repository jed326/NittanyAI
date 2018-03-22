from excelparser import parseexcel
import pandas as pd
import json
from logininfo import coursekeyworduser, coursekeywordpass
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username=coursekeyworduser,
  password=coursekeywordpass,
  version='2017-02-27')

makeexcel = True

class Coursekeyword:

    def __init__(self, coursename, description):
        self.coursename = coursename
        self.description = description

    def __str__(self):
        return "coursename = " + str(self.coursename) + " description = " + self.description

    def getkeywords(self):
        response = natural_language_understanding.analyze(
            text= self.description,
            features=Features(
                keywords=KeywordsOptions(
                    sentiment=True,
                    emotion=True,
                    limit=15)))
        keywordsfound = []
        for i in range(len(response['keywords'])):
            keyworddict = {}
            keyworddict["keyword"] = response['keywords'][i]['text']
            keyworddict["relevance"] = response['keywords'][i]['relevance']
            keywordsfound.append(keyworddict)
        self.keywords = keywordsfound
        print(self.keywords)
        print('success!')




if makeexcel:
    #df = parseexcel("FullDescriptions.csv.xlsx")
    dfexcel = pd.DataFrame(columns=['course', 'keywords', 'description'])

    with open("changedDengComments.txt") as fp:
        #completeFile = fp.read()
        lines = fp.readlines()
        fp.close()

    counter = 0
    for l in lines:
    #for index, row in df.iterrows():
        #print(row['course'], row['desc'] + '\n')
        course = Coursekeyword(counter, l)
        try:
            course.getkeywords()
            dfexcel = dfexcel.append(pd.DataFrame([[course.coursename, course.keywords, course.description]],
                                              columns=['course', 'keywords', 'description']), ignore_index=True)
        except:
            pass
    writer = pd.ExcelWriter('dengOutputLines.xlsx')
    dfexcel.to_excel(writer, 'Sheet1')
    writer.save()



