
#
#    Copyright 2019 Google LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

import sys
import json

from googleapiclient import sample_tools
from googleapiclient.http import build_http

discovery_doc = "gmb_discovery.json"

def main(argv):
    # Use the discovery doc to build a service that we can use to make
    # MyBusiness API calls, and authenticate the user so we can access their
    # account
    service, flags = sample_tools.init(argv, "mybusiness", "v4", __doc__, __file__, scope="https://www.googleapis.com/auth/business.manage", discovery_filename=discovery_doc)

    # Get the list of accounts the authenticated user has access to
    output = service.accounts().list().execute()
    print("List of Accounts:\n")

    #for account in output["accounts"]:
        #print(account["name"])
        #print(account["accountName"])
        #print()


    #print(json.dumps(output, indent=1) + "\n")

    firstAccount = output["accounts"][2]["name"]

    # Get the list of locations for the first account in the list
    print("List of Locations for Account " + firstAccount)
    locationsList = service.accounts().locations().list(parent=firstAccount).execute()
    print(json.dumps(locationsList, indent=1))

    location = 'accounts/102137775607626164366/locations/7402701046655805337'

    post =  {
    "languageCode": "en-US",
	"media": [{
            "mediaFormat": "PHOTO",
            "sourceUrl": "https://content.homenetiol.com/2000292/2126784/0x0/162dc648af7a444eb624efe6c7a54085.jpg",
        },
    ],
	"event": {
        "title": "Halloween Spook-tacular!",
        "schedule": {
            "startDate": {
                "year": 2020,
                "month": 10,
                "day": 31,
            },
            "startTime": {
                "hours": 9,
                "minutes": 0,
                "seconds": 0,
                "nanos": 0,
            },
            "endDate": {
                "year": 2020,
                "month": 10,
                "day": 31,
            },
            "endTime": {
                "hours": 17,
                "minutes": 0,
                "seconds": 0,
                "nanos": 0,
            },
        }
    },
	
    "summary": "This is a new Post",
	"offer": {
       "couponCode": "BOGO-JET-CODE",
       "redeemOnlineUrl": "https://www.google.com/redeem",
       "termsConditions": "Offer only valid if you can prove you are a time traveler"
	},
    #"callToAction": ,
    #"createTime": "2020-05-20T17:20:50.52Z",
    "topicType": "OFFER",
	
    
}
            

    #service.accounts().locations().localPosts().create(parent=location, body=post).execute()

#https://content.homenetiol.com/2000292/2126784/0x0/162dc648af7a444eb624efe6c7a54085.jpg

if __name__ == "__main__":
  main(sys.argv)