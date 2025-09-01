import datetime

curr_date = datetime.datetime.now()
print(curr_date)

# create object
create_date = datetime.datetime(2025, 9, 1)
print(create_date)

import requests

r = requests.get("https://w3schools.com/python/demopage.htm")
print(r)
print(r.status_code)
print(r.text)