food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

# for a in range (len(food_list)):
    
#     if food_list[a]['이름'] == '토마토':
#        del food_list[a]['종류']
#        food_list[a]['종류'] = '과일'       
#     if food_list[a]['이름'] == '자장면':
#         print('자장면엔 고춧가루지')
#     print(f"{food_list[a]['이름']} 은/는 {food_list[a]['종류']} (이)다.")
    
# for b in range (len(food_list)):
#     print(food_list[b], end = ', ')


i = 0
while i < 3:
    if food_list[i]['이름'] == '토마토':
       food_list[i]['종류'] = '과일'
       print(f"{food_list[i]['이름']} 은/는 {food_list[i]['종류']} (이)다.")
       i = i+1
    elif food_list[i]['이름'] == '자장면':
        print('자장면엔 고춧가루지')
        print(f"{food_list[i]['이름']} 은/는 {food_list[i]['종류']} (이)다.")
        i = i+1
    else:
        print(f"{food_list[i]['이름']} 은/는 {food_list[i]['종류']} (이)다.")
        i = i+1    
y=0
while y < len(food_list):
    print(food_list[y], end = ', ')
    y += 1
