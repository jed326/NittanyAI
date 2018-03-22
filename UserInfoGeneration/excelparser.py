import pandas as pd

def parseexcel(filename):
    xls = pd.ExcelFile(filename)
    #sheet1 = xls.parse(1)
    #var1 = sheet1['course']
    df = xls.parse(xls.sheet_names[0])
    return df





