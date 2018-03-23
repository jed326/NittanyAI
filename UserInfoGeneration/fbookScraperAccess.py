# import some Python dependencies

import urllib2
import json
import datetime
import csv
import time

access_token = "access token here"

def testFacebookPageData(access_token):

    has_next_page = True;
    
    # construct the URL string
    base = "https://graph.facebook.com/v2.12"
    node = "/me/posts"
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    while has_next_page:
        
    
        # retrieve data
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = json.loads(response.read())
        
        info = json.dumps(data, indent=4, sort_keys=True)
        print(info);


        if 'paging' in data.keys():
                url = data['paging']['next']
        else:
            has_next_page = False

testFacebookPageData(access_token)

