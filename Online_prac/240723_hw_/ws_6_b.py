data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.
print(data.items())

# 2. data가 가진 벨류 목록들만 모아서 출력한다.

print(data.keys())


# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
print(data.get('without','unknown'))

# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
for key, value in plus_data.items():
    data[key] = value

# 5. 변경된 data를 출력한다.
print(data)