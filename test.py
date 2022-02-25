import requests
import json

BASE = 'http://127.0.0.1:5000/'
header = {'content-type':'application/json'}

response = requests.get(BASE + 'api/vocab')
print(response.json())

payload = {'vocab':['ambassador']}
response = requests.post(BASE + 'api/vocab', json.dumps(payload), headers=header)
print(response.json())

#sponsored
payload = {'post_text':'#ad Love these cool toys at #ToysRUs. Go check them out'}
response = requests.post(BASE + 'api/prediction', json.dumps(payload), headers=header)
print(response.json())

#non-sponsored
payload = {'post_text':'My new year resolution is to stay fit and healthy'}
response = requests.post(BASE + 'api/prediction', json.dumps(payload), headers=header)
print(response.json())

payload = {'vocab':['ambassador', 'blogger', 'snapchatter', 'instagrammer']}
response = requests.post(BASE + 'api/vocab', json.dumps(payload), headers=header)
print(response.json())

response = requests.get(BASE + 'api/vocab')
print(response.json())

#sponsored
payload = {'post_text':'This is a product endosored by our ambassador'}
response = requests.post(BASE + 'api/prediction', json.dumps(payload), headers=header)
print(response.json())

#sponsored
payload = {'post_text':'A blogger migrated to a new website'}
response = requests.post(BASE + 'api/prediction', json.dumps(payload), headers=header)
print(response.json())

#sponsored
payload = {'post_text':'A new instagrammer has recently just joined our program'}
response = requests.post(BASE + 'api/prediction', json.dumps(payload), headers=header)
print(response.json())

#non-sponsored
payload = {'post_text':'#ad#sponsoredadvertisement'}
response = requests.post(BASE + 'api/prediction', json.dumps(payload), headers=header)
print(response.json())

#non-sponsored
payload = {'post_text':''}
response = requests.post(BASE + 'api/prediction', json.dumps(payload), headers=header)
print(response.json())

