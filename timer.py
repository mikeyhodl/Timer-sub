import requests

url = "https://api.etherscan.io/api?module=stats&action=ethsupply&apikey=9EDFVVEZ83DIU3R6IR3N3HAAVSAVTDRSNA"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

dataa = response.text



file = open("readme.md", 'w')
# file.write("Kenyan Time is: ")
file.write(str(dataa))
file.close()
