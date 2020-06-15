import urllib3
import facebook
import requests
import json
from dotenv import load_dotenv
load_dotenv()

import os
token = os.getenv("FB_ACCESS_TOKEN")
secret = os.getenv("FB_APP_SECRET")

graph = facebook.GraphAPI(token)

profile = graph.get_object('me',fields='first_name,location,link,email')	
#return desired fields
print(json.dumps(profile, indent=4))

page_name = "Metallica"
	
# list of required fields
fields = ['id','name','about','likes','link','band_members']

fields = ','.join(fields)

page = graph.get_object(page_name, fields=fields)
    
print(json.dumps(page,indent=4))