import requests

url = 'https://gnaa.africa/api/niggermail/v2/liberate'
response = requests.post(url, json={'target': 'walterminb@gmail.com', 'nmail-api-key': '288ff1d648da844ca5c7fdd96cf0e4387848e866143ca960993a6143aa2dca64'})
print(response.json())
