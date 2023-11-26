import requests
import json

r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
data = r.json()
  
def clean_json(obj):
  if isinstance(obj, dict):
    for key, value in list(obj.items()):
      if value in ["N/A","-",""]:
        del obj[key]
      else:
        clean_json(value)

  elif isinstance(obj, list):
    for item in list(obj):
      if item in ["N/A","-",""]:
        obj.remove(item)
      else:
        clean_json(item)

clean_json(data)

print(data)
