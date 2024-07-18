
import requests
from pprint import pprint as print

# # 무작위 유저 정보 요청 경로
# # API_URL = 'https://jsonplaceholder.typicode.com/users/2'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

for i in range (1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    requests.get(API_URL).json()
    print(parsed_data['name'])
