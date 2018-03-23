# import some Python dependencies

import urllib.request
import json
import datetime
import csv
import time

access_token = ""

def testFacebookPageData(access_token, request):

    has_next_page = True;
    
    # construct the URL string
    base = "https://graph.facebook.com/v2.12"
    node = "/me/" + request
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    #print(url)

    while has_next_page:
        
    
        #print(url)
        # retrieve data
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        
        info = json.dumps(data, indent=4, sort_keys=True)
        print(info);
        
        if 'paging' in data.keys() and 'next' in data['paging']:
                url = data['paging']['next']
        else:
            has_next_page = False


#posts, likes, feed
testFacebookPageData(access_token, "likes")



