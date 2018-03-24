import csv
import re

keyword = re.compile("'keyword': '.*?'")
colon = re.compile(": '.*?'")
finish = []
with open('CuylerTestOutput.csv', newline='') as csvfile:
    keyreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in keyreader:
        comborow = ' '
        comborow = comborow.join(row)
        keylist = re.findall(keyword,comborow)
        for word in keylist:
            daf = ','
            finish.append((daf.join(re.findall(colon, word)).replace('"','').replace(':','').replace("'",'')))
with open('cuylercleaned.csv', 'w', newline='') as csvfile:
    for key in finish:
        csvfile.write(key)
        csvfile.write('\n')
            
