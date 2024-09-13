import requests
from pprint import pprint as print

# for i in range (1, 6):
#     API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
#     response = requests.get(API_URL)
#     parsed_data = response.json()
#     requests.get(API_URL).json()
#     print(parsed_data)


dummy_data =[]
for i in range (1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    requests.get(API_URL).json()
    dummy_data.append(parsed_data.items(['company']['name']))
#     dummy_data.append(parsed_data['name'])
#     if (float(parsed_data['address']['geo']['lat'])< 80 and float(parsed_data['address']['geo']['lat'])>-80):
#         dummy_data.append(parsed_data['address']['geo']['lat'])
#     if (float(parsed_data['address']['geo']['lng'])< 80 and float(parsed_data['address']['geo']['lng'])>-80):
#         dummy_data.append(parsed_data['address']['geo']['lng'])
   
print(dummy_data)