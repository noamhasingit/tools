import requests
from requests_ntlm import HttpNtlmAuth

session = requests.Session()
#session.auth = HttpNtlmAuth('NICE_SYSTEMS\\noamha', 'Shlomit12')


#http://tracker/tracker/login_page.php?return=%2Ftracker%2Fmain_page.php

general_search_url = "http://tracker/tracker/login_page.php?return=%2Ftracker%2Fsearch_global_page.php%3F_searched%3Don%26fulltext%3D%26bugs%3Don%26docs%3Don%26kb%3Don%26fulltext%3Dvar1"
# importing the requests library

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'fulltext': "var1"}
# sending get request and saving the response as response object
r = session.get(url=general_search_url, params=PARAMS)
print(r.text,r.status_code,r.is_redirect)
# # extracting data in json format
# data = r.json()
#
# # extracting latitude, longitude and formatted address
# # of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']
#
# # printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#       % (latitude, longitude, formatted_address))