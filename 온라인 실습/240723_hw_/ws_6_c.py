data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

# for i in data:
#     print(data[i][key_list[i]])

# print(data[0]['name'])
# print(key_list[0])

for i in range(5):
    print('\n')
    for j in range(3):
        print(f'{key_list[j]}은/는 {data[i].get(key_list[j],"unknown")}입니다.')