# import some Python dependencies

import urllib.request
import json
import datetime
import csv
import time

access_token = ""

def testFacebookPageData(fileName, access_token, request):

    has_next_page = True;
    
    # construct the URL string
    base = "https://graph.facebook.com/v2.12"
    node = "/me/" + request
    parameters = "&access_token=%s" % access_token
    url = base + node + parameters

    #print(url)

    f = open(fileName,'w')
    

    while has_next_page:
        
    
        #print(url)
        # retrieve data
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        
        info = json.dumps(data, indent=4, sort_keys=True)
        f.write(info);
        #print(info);
        
        if 'paging' in data.keys() and 'next' in data['paging']:
                url = data['paging']['next']
        else:
            has_next_page = False

    f.close()


def cleanUpData(file):

    file1 = open(file, "r")
    file2 = open("destination.txt", "w")


    for line in file1: 
        tempLine = line.replace('"', '').replace(':', '').strip(' ')
        if tempLine.startswith("about"):
            file2.write("\n" + tempLine[6:].strip('\n'))
        if tempLine.startswith("mission"):
            file2.write(" " + tempLine[8:].strip('\n'))
        if tempLine.startswith("general_info"):
            file2.write(" " + tempLine[13:].strip('\n'))



    file1.close()
    file2.close()


    

testFacebookPageData("CuylerTest.txt", access_token, "?fields=likes%7Bname%2Cabout%2Cmission%2Cgeneral_info%7D")
cleanUpData("CuylerTest.txt")

